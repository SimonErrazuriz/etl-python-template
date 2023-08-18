# -*- coding: utf-8 -*-
from main.utilities.config_properties import ConfigProperties
import logging
import os


class ConfigLogger:

    def __init__(self, class_name: str):
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.__properties = ConfigProperties().properties
        log_file_path = os.path.join(
            self.__properties['path']['base'],
            self.__properties['etl']['name'],
            self.__properties['path']['resources'],
            f'''{self.__properties['etl']['name']}.log'''
        )

        logging.basicConfig(
            filename=log_file_path,
            level=logging.DEBUG,
            filemode='a',
            format=log_format,
            datefmt="%d-%m-%Y %H:%M:%S",
            encoding='utf-8',
        )

        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter(log_format))

        self.__logger = logging.getLogger(class_name)
        self.__logger.addHandler(console)

    @property
    def logger(self):
        return self.__logger
