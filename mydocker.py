import docker
import sys
import os
from config import myconfig
from remote import remote

mswindows = (sys.platform == "win32")

if mswindows:
    docker_client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')
else:
    docker_client = docker.APIClient(base_url='unix://var/run/docker.sock')


def build_images(projectpath, dockerfile, tag):
    try:
        open(os.path.join(projectpath, "dockerfile"), 'w').write(dockerfile)
        global docker_client
        for line in docker_client.build(path=projectpath, tag="{}/{}".format(myconfig.docker_server, tag)):
            print(str(line, 'utf-8'))
    except Exception as e:
        print(e)


def push_image(tag):
    try:
        for line in docker_client.push("{}/{}".format(myconfig.docker_server, tag), stream=True):
            print(str(line, 'utf-8'))
    except Exception as e:
        print(e)


def pull_image(image, tag):
    try:
        for line in docker_client.pull("{}/{}:{}".format(myconfig.docker_server, image, tag), stream=True):
            print(str(line, 'utf-8'))
    except Exception as e:
        print(e)


# def _docker_login_aws():
#     authoriziationData = myaws.aws_client.get_authorization_token()['authorizationData'][0]
#     authoriziationToken = authoriziationData['authorizationToken']
#     proxyEndpoint = authoriziationData['proxyEndpoint']
#     docker_client.login("AWS", authoriziationToken, registry=proxyEndpoint)


def docker_login_server():
    try:
        docker_client.login(remote.username, remote.password, registry="https://" + myconfig.docker_server)
    except Exception as e:
        print(e)
