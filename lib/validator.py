from .workbook import Workbook
from .api import Api
from .utils import write_rows_to_workbook

import itertools


class Validator:
    def __init__(self, workbooks, api_url, api_token):
        self.api = Api(url=api_url, token=api_token)
        self.workbooks = [Workbook(workbook, self.api)
                          for workbook in workbooks]

    def get_workbook_rows(self):
        values = [workbook.get_sheet_rows() for workbook in self.workbooks]
        return itertools.chain.from_iterable(values)

    def validate_workbook_rows(self):
        values = [workbook.validate_sheet_rows()for workbook in self.workbooks]
        return list(itertools.chain.from_iterable(values))

    def sort_validated_rows(self, rows):
        valid = []
        invalid = []
        undetermined = []

        for row in rows:
            if True in row:
                valid.append(row)
            elif False in row:
                invalid.append(row)
            else:
                undetermined.append(row)

        return dict(valid=valid, invalid=invalid)

    def export_validated_rows(self, rows):
        sorted_rows = self.sort_validated_rows(rows)

        write_rows_to_workbook(sorted_rows.get('invalid'), './', 'invalid')
        write_rows_to_workbook(sorted_rows.get('valid'), './', 'valid')
