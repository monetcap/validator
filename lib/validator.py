from .workbook import Workbook
from .api import Api

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
