from .constants import DESCRIPTION, MOCK_DNC_URL
import argparse

parser = argparse.ArgumentParser(description=DESCRIPTION)

parser.add_argument('--workbook', '-wb',
                    action='append',
                    help='path to workbook; you can use multiple of these',
                    required=True
                    )

parser.add_argument('--api-token', '-at',
                    help='real validation api_token',
                    required=True
                    )

parser.add_argument('--api-url', '-au',
                    help='real validation api_url; defaults to {}'
                         .format(MOCK_DNC_URL),
                    default=MOCK_DNC_URL,
                    )
