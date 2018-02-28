import docker
import sys
import myaws
import os

mswindows = (sys.platform == "win32")

if mswindows:
    docker_client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')
else:
    docker_client = docker.APIClient(base_url='unix://var/run/docker.sock')


def build_images(projectpath, dockerfile, tag):
    open(os.path.join(projectpath, "dockerfile"), 'w').write(dockerfile)
    global docker_client
    for line in docker_client.build(path=projectpath, tag=tag):
        print(line)


def pull(image):
    for line in docker_client.pull(image, stream=True):
        print(line)


def _docker_login_aws():
    authoriziationData = myaws.aws_client.get_authorization_token()['authorizationData'][0]
    authoriziationToken = authoriziationData['authorizationToken']
    proxyEndpoint = authoriziationData['proxyEndpoint']
    docker_client.login("AWS", authoriziationToken, registry=proxyEndpoint)



