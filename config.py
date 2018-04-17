import configparser
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
elif __file__:
    BASE_DIR = os.path.dirname(__file__)

CONFIG_FILE = "config.ini"

secret_key = b'XQYfjn2t4BkYHsTpkPZDzfSlLQqAJGzEzF8GPkEYjfc='


class MyConifg(object):
    def __init__(self):
        self.server = ""
        self.config = None
        self.config_file = os.path.join(BASE_DIR, CONFIG_FILE)
        self.init_config()

    def init_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        self.server = self.config.defaults()['server']
        self.set_value()

    def set_value(self):
        for op in self.config.options('CACHE'):
            setattr(self, op, self.config.get('CACHE', op))

    def save_config(self):
        self.config['CACHE']['project'] = self.project
        self.config['CACHE']['tag'] = self.tag
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)


myconfig = MyConifg()
