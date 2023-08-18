# -*- coding: utf-8 -*-
from main.utilities.config_properties import ConfigProperties
from main.utilities.config_log import ConfigLogger
from main.utilities.utilities import Utilities
import os
import sys


class SaveData:

    def __init__(self):
        self.__logger = ConfigLogger(type(self).__name__).logger
        self.__properties = ConfigProperties().properties
        self.__etl_name = self.__properties['etl']['name']

    def main(self, data_transformed: str) -> str:
        try:
            name_file = f'''{self.__etl_name}_{Utilities.get_current_day().strftime('%d_%m_%Y')}.json'''
            dir_path = os.path.join(
                self.__properties['path']['base'],
                self.__etl_name,
                self.__properties['path']['files']
            )

            os.makedirs(dir_path, exist_ok=True)

            path_file = os.path.join(dir_path, name_file)

            with open(path_file, 'w') as file:
                file.write(data_transformed)

        except Exception as e:
            error = "Error al guardar el archivo"
            error_detail = str(e)
            self.__logger.info(error)
            self.__logger.info(error_detail)
            sys.exit(2)

        return path_file
