# -*- coding: utf-8 -*-
from main.utilities.config_properties import ConfigProperties
from main.utilities.config_log import ConfigLogger
from main.utilities.email import Email
import psycopg2
import sys


class Extract:

    def __init__(self):
        self.__logger = ConfigLogger(type(self).__name__).logger
        self.__properties = ConfigProperties().properties
        self.__query = self.__properties['extract']['db']['query']

    def main(self, connection: psycopg2) -> str:
        try:
            cursor = connection.cursor()
            cursor.execute(self.__query)
            data = cursor.fetchall()

        except psycopg2.Error as e:
            error = "Error al ejecutar la consulta SQL"
            error_detail = str(e)
            self.__logger.info(error)
            self.__logger.info(error_detail)
            email = Email()
            email.send_email(error, error_detail)
            sys.exit(2)

        finally:
            connection.close()
            cursor.close()

        if len(data) == 0:
            error = "Proceso sin registros"
            self.__logger.info(error)
            email = Email()
            email.send_email(error, 'Sin registros del día anterior')
            sys.exit(2)

        return data
