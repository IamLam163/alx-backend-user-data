#!/usr/bin/env python3
"""
function filter_datum
"""
import re
from typing import List
import logging


PII_FIELDS: tuple = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters incoming log records"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return (super().format(record))


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    # pattern = re.compile(
    #     "(?<={0})(?:{1}[^{0}]+)+".format(separator, "|".join(fields)))
    # return pattern.sub(redaction, message)
    return re.sub('|'.join('(?<={}=).*?(?={})'.format(field, separator)
                           for field in fields), redaction, message)


def get_logger() -> logging.Logger:
    """returns logging.Logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
