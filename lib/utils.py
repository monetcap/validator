from openpyxl import Workbook
from .constants import PHONE_DIGIT_REGEX, PHONE_COLUMN_REGEX
import re


def is_value_phone_identifier(value):
    return any(re.match(regex, value, re.IGNORECASE)
               for regex in [PHONE_DIGIT_REGEX, PHONE_COLUMN_REGEX])


def is_value_phone(value):
    return re.match(PHONE_DIGIT_REGEX, value)


def write_rows_to_workbook(rows, workbook_path, workbook_name):
    wb = Workbook()

    ws = wb.active
    ws.title = workbook_name

    for row in rows:
        ws.append(row)

    file_name = '{0}/{1}.xlsx'.format(workbook_path, workbook_name)

    wb.save(file_name)
