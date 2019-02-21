from openpyxl import load_workbook
from .sheet import Sheet

import itertools


class Workbook:
    def __init__(self, workbook_file_path, api_object):
        self.workbook = load_workbook(workbook_file_path,
                                      read_only=True)

        self.sheets = [Sheet(sheet, api_object) for sheet in self.workbook]

    def get_sheet_rows(self):
        values = [sheet.get_row_values() for sheet in self.sheets]

        return list(itertools.chain.from_iterable(values))

    def validate_sheet_rows(self):
        values = [sheet.validate_row_values() for sheet in self.sheets]

        return list(itertools.chain.from_iterable(values))
