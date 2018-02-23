from docker import APIClient

client = APIClient(base_url='unix://var/run/docker.sock')

print (client)
def build_images(projectpath, dockerfile):
    global client
    for line in client.build(path=projectpath, fileobj=dockerfile, tag="1.2.2"):
        print(line)
