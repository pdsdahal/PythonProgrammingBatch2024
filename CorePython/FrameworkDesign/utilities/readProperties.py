import configparser
import os

cwd = os.getcwd()
parent = os.path.dirname(p=cwd)
configparser = configparser.RawConfigParser()
configparser.read(filenames=parent + "/Configurations/config.ini")


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
