from .constants import PHONE_DIGIT_REGEX, PHONE_COLUMN_REGEX
import re


def is_value_phone_identifier(value):
    return any(re.match(regex, value, re.IGNORECASE)
               for regex in [PHONE_DIGIT_REGEX, PHONE_COLUMN_REGEX])


def is_value_phone(value):
    return re.match(PHONE_DIGIT_REGEX, value)
