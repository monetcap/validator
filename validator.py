import logging
from openpyxl import load_workbook
import argparse
import re

PHONE_COLUMN_REGEX = r'^phone$'
PHONE_DIGIT_REGEX = r'^\d{10}$'

PHONE_REGEXS = [
    PHONE_COLUMN_REGEX,
    PHONE_DIGIT_REGEX
]

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'DEBUG'

# configure logging
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
log = logging.getLogger("validator")

parser = argparse.ArgumentParser(description='Process an xlsx document.')

parser.add_argument('--xlsx-file-path', '-xfp',
                    help='Path to xlsx document',
                    required=True
                    )


class Sheet:
    phone_column = -1

    def _enumerate_phone_column(self):
        first_row = self.sheet[2]

        cell_values = [str(cell.value) for cell in first_row]

        for i in range(len(cell_values)):
            value = cell_values[i]

            if any(re.match(regex, value, re.IGNORECASE)
                   for regex in PHONE_REGEX):
                self.index = i
                break

    def __init__(self, sheet):
        self.title = sheet.title
        self.sheet = sheet

        self._enumerate_phone_column()

    def validate(self):
        pass


class Workbook:
    def __init__(self, file_path):
        self.workbook = load_workbook(file_path, read_only=True)
        self.sheets = [Sheet(sheet) for sheet in self.workbook]

    def validate(self):
        for sheet in self.sheets:
            sheet.validate()


class Validator:
    sheets = []

    def __init__(self, xlsx_file_path):
        self.workbook = Workbook(xlsx_file_path)

    def validate(self):
        self.workbook.validate()


def main():
    args = parser.parse_args()

    validator = Validator(xlsx_file_path=args.xlsx_file_path)
    validator.validate()


if __name__ == '__main__':
    main()
