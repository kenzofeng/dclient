from cryptography.fernet import Fernet, MultiFernet
import urllib
import requests
from config import myconfig


class Remote(object):

    def get_aws_access(self):
        pass

    @staticmethod
    def dockerfile():
        content = requests.get("http://%s/user/dockerfile/" % myconfig.server, params={'name': myconfig.dockerfile})
        return content.text
