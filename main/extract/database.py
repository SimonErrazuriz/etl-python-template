# -*- coding: utf-8 -*-
from main.utilities.config_properties import ConfigProperties
from main.utilities.config_log import ConfigLogger
from main.utilities.email import Email
import sys
import psycopg2


class Database:

    def __init__(self):
        self.__logger = ConfigLogger(type(self).__name__).logger
        self.__properties = ConfigProperties().properties
        self.__db_server = self.__properties['extract']['db']['server']
        self.__db_user = self.__properties['extract']['db']['user']
        self.__db_pass = self.__properties['extract']['db']['pass']
        self.__db_port = self.__properties['extract']['db']['port']
        self.__db_database = self.__properties['extract']['db']['database']

    def main(self) -> psycopg2:
        try:
            connection = psycopg2.connect(
                host=self.__db_server,
                port=self.__db_port,
                user=self.__db_user,
                password=self.__db_pass,
                database=self.__db_database
            )
        except psycopg2.Error as e:
            error = "Error al establecer la conexión con la base de datos"
            error_detail = str(e)
            self.__logger.info(error)
            self.__logger.info(error_detail)
            email = Email()
            email.send_email(error, error_detail)
            sys.exit(2)

        return connection
