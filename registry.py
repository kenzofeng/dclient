import requests
from config import myconfig
import json
import urllib3

urllib3.disable_warnings()


class Registry(requests.Session):
    base_url = "https://" + myconfig.docker_server

    def __init__(self):
        super(Registry, self).__init__()

    def repositories_list(self):
        url = "{}/v2/_catalog".format(self.base_url)
        response = self._get(url, **self._add_header())
        return json.loads(response.content)['repositories']

    def image_tags_list(self, image_name):
        url = "{}/v2/{}/tags/list".format(self.base_url, image_name)
        response = self._get(url, **self._add_header())
        return json.loads(response.content)['tags']

    def delete_image(self, image_name, tag):
        url = "{}/v2/{}/manifests/{}".format(self.base_url, image_name, tag)
        response = self._get(url, **self._add_header(Accept='application/vnd.docker.distribution.manifest.v2+json'))
        layers = json.loads(response.content)['layers']
        docker_content_digest = response.headers['docker-content-digest']
        for layer in layers:
            url = "{}/v2/{}/blobs/{}".format(self.base_url, image_name, layer['digest'])
            self._delete(url, **self._add_header())
        url = "{}/v2/{}/manifests/{}".format(self.base_url, image_name, docker_content_digest)
        response = self._delete(url, **self._add_header())
        return response.status_code

    def _add_auth_header(self, **kwargs):
        kwargs['headers']['Authorization'] = 'Basic dGVzdHVzZXI6dGVzdHBhc3N3b3Jk'
        return kwargs

    def _add_header(self, **kwargs):
        mykwargs = {}
        mykwargs['headers'] = {}
        mykwargs['verify'] = False
        for key, value in kwargs.items():
            mykwargs['headers'][key] = value
        mykwargs = self._add_auth_header(**mykwargs)
        return mykwargs

    def _get(self, url, **kwargs):
        return self.get(url, **kwargs)

    def _delete(self, url, **kwargs):
        return self.delete(url, **kwargs)


myregistry = Registry()
# registry.delete_image('bestwestern', '1.1.4')
