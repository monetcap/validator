from .utils import is_value_phone_identifier
import logging

log = logging.getLogger(__name__)


class Sheet:
    phone_column_index = -1

    valid_rows = []
    invalid_rows = []

    def _get_cell_values_from_row(self, row):
        return [str(cell.value) for cell in row]

    def _enumerate_phone_column_index_from_row(self, row):
        # initial phone_column_index value
        phone_column_index = -1

        # generate cell values from row
        cell_values = self._get_cell_values_from_row(row)

        # iterate through cell values
        for i in range(len(cell_values)):
            value = cell_values[i]

            # Check if value matches "[Pp]hone || 0000000000"
            if is_value_phone_identifier(value):
                phone_column_index = i
                break

        return phone_column_index

    def _enumerate_phone_column(self):
        # get first two rows from sheet
        rows = self.sheet[1:2]

        # this will loop through the first two rows and set the
        # phone_column_index only when it's first enumerated
        for row in rows:
            value = self._enumerate_phone_column_index_from_row(row)

            if value is not -1 and self.phone_column_index is -1:
                self.phone_column_index = value
                break

        # raise an exception if the value wasn't enumerated
        if self.phone_column_index is -1:
            raise Exception("phone_column_index couldn't be enumerated")

        log.debug('phone_column_index enumerated at {}'
                  .format(self.phone_column_index))

    def __init__(self, sheet, api_object):
        self.sheet = sheet
        self.api = api_object

        self._enumerate_phone_column()

    def get_row_values(self):
        return [self._get_cell_values_from_row(row) for row in self.sheet.rows]

    def validate_row_values(self):
        return [self.api.validate_row(row, self.phone_column_index)
                for row in self.get_row_values()]
