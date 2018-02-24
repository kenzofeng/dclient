import docker
import sys
import boto3

mswindows = (sys.platform == "win32")

if mswindows:
    docker_client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')
else:
    docker_client = docker.APIClient(base_url='unix://var/run/docker.sock')

aws_client = boto3.client('ecr', region_name="ap-southeast-1", aws_access_key_id="AKIAJWSXQVIWLPWDDOPQ",
                          aws_secret_access_key="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")


def docker_build_images(projectpath, dockerfile):
    global docker_client
    for line in docker_client.build(path=projectpath, fileobj=dockerfile, tag="1.2.2"):
        print(line)


def docker_pull(image):
    for line in docker_client.pull(image, stream=True):
        print(line)


def list_esc_repositories():
    global aws_client
    aws_client.describe_repositories()

    client = boto3.client('ecr', region_name="ap-southeast-1", aws_access_key_id="AKIAJWSXQVIWLPWDDOPQ",
                          aws_secret_access_key="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")
    print(client.get_authorization_token())


def docker_login_aws():
    authoriziationData = aws_client.get_authorization_token()['authorizationData'][0]
    authoriziationToken = authoriziationData['authorizationToken']
    proxyEndpoint = authoriziationData['proxyEndpoint']
    docker_client.login("AWS", authoriziationToken, registry=proxyEndpoint)


# docker_pull("391292943957.dkr.ecr.ap-southeast-1.amazonaws.com/accor-adapter")
