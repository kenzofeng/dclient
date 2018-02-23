import docker


def build_images(projectpath, dockerfile):
    # client = APIClient(base_url='unix://var/run/docker.sock')
    client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')
    for line in client.build(path=projectpath, fileobj=dockerfile, tag="1.2.2"):
        print(line)
