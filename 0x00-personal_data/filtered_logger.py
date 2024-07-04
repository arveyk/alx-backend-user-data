#!/usr/bin/env python3
"""
Filter datum
"""
import csv
import bcrypt
import logging
import mysql.connector
import os
from typing import List

# level=logging.INFO, format='%(asctime)s:%(levelname)s')
PII_FIELDS = {
        "name": '',
        "email": '',
        "ssn": '',
        "phone": '',
        "password": ''
    }
with open('user_data.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        for key in line.keys():
            if key in PII_FIELDS:
                PII_FIELDS[key] = line[key]



def filter_datum(fields, redactions, message, separator):
    """Function to filter data
    Args:
        fields: the fields to redact
        redactions: string to use to redact
        message: the message to filter
        separator: separator to use
    Raturns: the filtered message
    """

    filtered = ''
    tempList = message.split(separator)
    for field in tempList:
        if len(field) == 0:
            continue
        word = field.split('=')
        if word[0] not in fields:
            if len(word) > 1:
                filtered = filtered + word[0] + '=' + word[1] + separator
            else:
                filtered = filtered + word[0] + '=' + redactions + separator

        else:
            filtered = filtered + word[0] + '=' + redactions + separator

    return filtered


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        name = record.name
        logger = logging.getLogger(name)

        # msg = (record.getMessage())
        encr_info = filter_datum(self.fields, self.REDACTION,
                                 record.msg, self.SEPARATOR)
        record.msg = encr_info
        return logger.handle(record)

def get_logger() -> logging.Logger:
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    channel = logging.StreamHandler()
    channel.setLevel(logging.INFO)

    # fmtter = logging.Formatter(RedactingFormatter())
    channel.setFormatter(RedactingFormatter())
    logger.setFormatter(RedactingFormatter)
    logger.addHandler(channel)
    return logger.msg()


def get_db():
    """Get database
    Args: None
    """

    DB_USERNAME = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    DB_PASSWORD = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    DB_HOST = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    DB_NAME = os.environ.get('PERSONAL_DATA_DB_NAME', 'my_db')

    conxn = mysql.connector.connect(
            user = DB_USERNAME,
            password = DB_PASSWORD,
            host = DB_HOST,
            database = DB_NAME
            )
    return conxn


def main():
    """Get database, display
    """

    dbConnection = get_db()
    # display all rowsd

    dbCursor = dbConnection.cursor()
    Rows = dbCursor.execute('SELECT name,\
            email, phone, ssn, password FROM users')
    for email, phone, ssn, password in dbCursor:
        print("{} {}".format(email, phone))



if __name__ == '__main__':
    main()
