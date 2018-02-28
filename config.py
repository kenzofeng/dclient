import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = "config.ini"


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
print (myconfig)