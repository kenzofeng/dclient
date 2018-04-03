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

    def delete_image(self):
        pass

    def _add_header(self):
        return {'headers': {'Authorization': 'Basic dGVzdHVzZXI6dGVzdHBhc3N3b3Jk'}, 'verify': False}

    def _get(self, url, **kwargs):
        return self.get(url, **kwargs)


myregistry = Registry()
