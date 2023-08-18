# -*- coding: utf-8 -*-
from main.utilities.config_log import ConfigLogger
from main.utilities.email import Email
import sys
import json


class Transform:

    def __init__(self):
        self.__logger = ConfigLogger(type(self).__name__).logger

    def main(self, data: str) -> str:

        data_json = []

        for row in data:

            try:
                id_test = row[0]
                description = row[1]
            except Exception as e:
                error = "Error en la captura de datos"
                error_detail = str(e)
                self.__logger.info(error)
                self.__logger.info(error_detail)

            data_json.append({
                "id_test": id_test,
                "description": description
            })

        try:
            data_transformed = json.dumps(data_json)
        except Exception as e:
            error = "Error en la generación del JSON"
            error_detail = str(e)
            self.__logger.info(error)
            self.__logger.info(error_detail)
            email = Email()
            email.send_email(error, error_detail)
            sys.exit(2)

        return data_transformed
