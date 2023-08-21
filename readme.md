# ETL Python Template

This repository contains an ETL (Extract, Transform, Load) script developed in Python that extracts data from a PostgreSQL table, transforms it into JSON format, sends a request to an API, saves the JSON to a file, and sends it via email. The ETL process is designed to handle errors and notify stakeholders via email in case of any failures.

## Template
This repository serves as a versatile template that can be reused as a starting point for various ETL scenarios. Whether you need to communicate data between APIs, integrate data from an API into a database, or adapt the flow to your specific requirements, this template provides a structured foundation to build upon.

## Features
The ETL process performs the following steps:
- Extraction: Data is extracted from a PostgreSQL table using the provided database connection parameters. The SQL query used for extraction is defined in the config_dev or config_prd properties file.
- Transformation: The extracted data is transformed into JSON format.
- API Request: The transformed JSON data is sent as a request to the specified API endpoint.
- File Saving: The transformed JSON data is saved to a file in the specified directory.
- Email: After the ETL process is completed, an email is sent using the configured SMTP server. The email contains a report on the process, including success or failure status. In case of an error, additional information is provided in the email.

## Usage
- Clone this repository to your local machine.
- Configure the config_dev or config_prd properties file according to your environment, example:
```yaml
extract:
  db:
    server: localhost
    user: postgres
    pass: postgres
    port: 5432
    database: bd_test
    query: SELECT * FROM test
```
- Configure class ConfigProperties in main/utilities/config_properties to choose config properties:
```python
self.__environment = 'prd' # or dev
```
- Install the required packages using the provided requirements.txt file.
```
pip install -r requirements.txt
```
- Run the ETL script using the command: 
```
python main.py
```
