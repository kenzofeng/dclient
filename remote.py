from cryptography.fernet import Fernet
import requests
import config
from config import myconfig
import json


class Remote(object):
    dockerfile = ""
    username = ""
    password = ""

    def dockerfile(self):
        try:
            content = requests.get("http://%s/user/dockerfile/" % myconfig.server, params={'name': myconfig.dockerfile})
            self.dockerfile = content.text
            return self.dockerfile
        except Exception as e:
            print(e)

    def getaccess(self):
        try:
            rs = requests.get("http://%s/user/access/" % myconfig.server,
                              params={'docker_registry': myconfig.docker_server})
            content = json.loads(rs.content)
            cipher_suite = Fernet(config.secret_key)
            self.username = cipher_suite.decrypt(str.encode(content['u']))
            self.password = cipher_suite.decrypt(str.encode(content['p']))
        except Exception as e:
            print(e)


remote = Remote()
