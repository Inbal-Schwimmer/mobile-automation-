import configparser
import os


class ConfigReader:

    @staticmethod
    def read_config(section, key):
        global config
        root_dir = os.path[0]

        config = configparser.ConfigParser()
        config.read(root_dir + '/config.ini')

        # Check that the Section & key exists
        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")