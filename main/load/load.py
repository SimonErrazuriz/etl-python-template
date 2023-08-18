# -*- coding: utf-8 -*-
from main.utilities.config_properties import ConfigProperties
from main.utilities.config_log import ConfigLogger
from main.utilities.email import Email
import sys
import requests


class Load:

    def __init__(self):
        self.__logger = ConfigLogger(type(self).__name__).logger
        self.__properties = ConfigProperties().properties
        self.__url_load = self.__properties['load']['api']['url']
        self.__authorization = self.__properties['load']['api']['authorization']
        self.__content_type = self.__properties['load']['api']['content_type']

    def main(self, data_transformed: str, file_path: str) -> requests.Response:
        headers = {
            "Authorization": self.__authorization,
            "Content-Type": self.__content_type
        }
        try:
            response = requests.post(self.__url_load, data=data_transformed, headers=headers)
        except Exception as e:
            error = "Error al generar la petición"
            error_detail = str(e)
            self.__logger.info(error)
            self.__logger.info(error_detail)
            email = Email()
            email.send_email(error, error_detail, file_path, file_path.split('\\')[1])
            sys.exit(2)
        self.__logger.info(response.status_code)
        self.__logger.info(response.text)

        return response
