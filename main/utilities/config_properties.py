# -*- coding: utf-8 -*-
import os
import yaml


class ConfigProperties:

    def __init__(self):
        self.__environment = 'prd'
        self.__properties = self.load_properties(self.__environment)

    def load_properties(self, environment):
        path_root = os.path.dirname(os.path.realpath(__name__))
        path_properties = f'resources/config_{environment}.yaml'
        with open(os.path.join(path_root, path_properties), 'r') as yaml_file:
            properties = yaml.safe_load(yaml_file)
        return properties

    @property
    def properties(self):
        return self.__properties
