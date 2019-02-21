import requests
import logging

from .utils import is_value_phone


log = logging.getLogger(__name__)


class Api:
    FORMAT = 'json'

    def __init__(self, url, token):
        self.url = url
        self.token = token

        log.debug('api object initiated url: {}'.format(url))

    def validate_phone(self, phone):
        log.debug('processing phone: {}'.format(phone))

        if not is_value_phone(phone):
            return None

        payload = {
            'token': self.token,
            'phone': phone,
            'format': self.FORMAT
        }

        r = requests.get(self.url, params=payload)

        if r.status_code != requests.codes.ok:
            return None

        resp = r.json()

        log.debug(resp)

        is_valid = True

        if resp['RESPONSECODE'] != 'OK':
            is_valid = False
        if resp['national_dnc'] != 'N':
            is_valid = False
        if resp['state_dnc'] != 'N':
            is_valid = False
        if resp['litigator'] != 'N':
            is_valid = False
        if resp['dma'] != 'N':
            is_valid = False

        return is_valid

    def validate_row(self, row, phone_column_index):
        phone = row[phone_column_index]

        is_valid = self.validate_phone(phone)

        data = row
        data.append(is_valid)

        return data
