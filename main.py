#!/usr/local/bin/python

from lib.validator import Validator
from lib.argparser import parser
import lib.logger


def main():
    # parser our command line arguments
    args = parser.parse_args()

    # initialize a validator object with the command line arguments
    v = Validator(workbooks=args.workbook,
                  api_url=args.api_url,
                  api_token=args.api_token)

    validated_rows = v.validate_workbook_rows()
    v.export_validated_rows(validated_rows)


if __name__ == '__main__':
    main()
