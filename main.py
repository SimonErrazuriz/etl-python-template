# -*- coding: utf-8 -*-
from main.utilities.config_properties import ConfigProperties
from main.utilities.email import Email
from main.extract.database import Database
from main.extract.extract import Extract
from main.transform.transform import Transform
from main.load.save_data import SaveData
from main.load.load import Load


class Main:

    def main(self) -> None:

        ############################################################### EXTRACT - DATABASE ###################################################################

        database = Database()
        connection = database.main()

        extract = Extract()
        data = extract.main(connection)

        ################################################################### TRANSFORM  #######################################################################

        transform = Transform()
        data_transformed = transform.main(data)

        ###################################################################### LOAD ##########################################################################

        save_data = SaveData()
        file_path = save_data.main(data_transformed)

        load = Load()
        response = load.main(data_transformed, file_path)

        ###################################################################### EMAIL #########################################################################

        email = Email()
        email.send_email(f'{response.status_code}', f'{response.status_code} - {response.text}', file_path, file_path.split('\\')[2])


# EXECUTE
main = Main()
main.main()
