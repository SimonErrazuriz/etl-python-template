# -*- coding: utf-8 -*-
from main.utilities.config_properties import ConfigProperties
from main.utilities.config_log import ConfigLogger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
from email import encoders


class Email:

    def __init__(self):
        self.__logging = ConfigLogger(type(self).__name__).logger
        self.__properties = ConfigProperties().properties
        self.__email_user = self.__properties['email']['credentials']['user']
        self.__email_pass = self.__properties['email']['credentials']['pass']
        self.__email_subject = self.__properties['email']['settings']['subject']
        self.__email_recipients = self.__properties['email']['settings']['recipients'].split(',')
        self.__email_server_smtp = self.__properties['email']['server']['smtp']
        self.__etl_name = self.__properties['etl']['name']

    def send_email(self, subject: str, detail: str, path_file: str = '', name_file: str = 'adjunto') -> None:

        subject = f'{self.__email_subject} {self.__etl_name}: {subject}' if self.__email_subject else f'{self.__etl_name}: {subject}'

        message = f'''
                <div>
                    <h3>{self.__etl_name}:</h3>
                    <p>Detalle: {detail}.</p>
                </div>
                '''

        try:
            server = smtplib.SMTP(self.__email_server_smtp)
            server.starttls()
            server.login(self.__email_user, self.__email_pass)
            email = MIMEMultipart()
            email['From'] = self.__email_user
            email.attach(MIMEText(message, 'html'))
            email['Subject'] = subject

            if (path_file != ''):
                try:
                    path_file = open(path_file, 'rb')
                    attached_mime = MIMEBase('application', 'octet-stream')
                    attached_mime.set_payload((path_file).read())
                    encoders.encode_base64(attached_mime)
                    attached_mime.add_header(
                        'Content-Disposition', "attachment; filename= %s" % name_file)
                    email.attach(attached_mime)
                except Exception as e:
                    self.__logging.error(e)
            server.sendmail(self.__email_user, self.__email_recipients, email.as_string())
            server.quit()
            self.__logging.info('Correo enviado')

        except Exception as e:
            self.__logging.error('Ocurrió un error en el envío del correo')
            self.__logging.error(e)
