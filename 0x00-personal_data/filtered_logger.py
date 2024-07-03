#!/usr/bin/env python3
"""
Filter datum
"""
import bcrypt
import logging
import os
from typing import List

# level=logging.INFO, format='%(asctime)s:%(levelname)s')


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
        msg = (record.getMessage())
        encr_info = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR), record
        return logging.info(encr_info)

def get_db():
    """Get database
    """

    #connect to holberton database
    # read user table
    # environmental vars
    PERSONAL_DATA_DB_USERNAME = "root"
    PERSONAL_DATA_DB_PASSWORD = ''
    PERSONAL_DATA_DB_HOST = 'localhost'

    # databasename stored in PERSONAL_DATA_DB_NAME
    # return connector to database

def main():
    """Get database, display
    """
    db = get_db
    # display all rows


if __name__ == '__main__':
    main()
