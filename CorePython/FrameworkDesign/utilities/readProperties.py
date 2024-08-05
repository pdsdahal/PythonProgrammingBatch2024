import configparser
import os

config_file_path = os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini')
configparser = configparser.ConfigParser()
configparser.read(config_file_path)


class ReadConfig:

    @staticmethod
    def get_base_url():
        return configparser.get("commonInfo", "base_url")

    @staticmethod
    def get_username():
        return configparser.get("commonInfo", "username")

    @staticmethod
    def get_password():
        return configparser.get("commonInfo", "password")
