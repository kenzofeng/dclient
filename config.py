import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = "config.ini"

config = configparser.ConfigParser()
config.read()