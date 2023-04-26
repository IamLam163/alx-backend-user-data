#!/usr/bin/env python3
"""
function filter_datum
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    pattern = re.compile(
        "(?<={0})(?:{1}[^{0}]+)+".format(separator, "|".join(fields)))
    return pattern.sub(redaction, message)
