DESCRIPTION = 'Processes Workbooks provided through command line arguments.'

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'DEBUG'

PHONE_COLUMN_REGEX = r'^phone$'
PHONE_DIGIT_REGEX = r'^\d{10}$'

MOCK_DNC_URL = 'https://realvalidation-dnc-mock.herokuapp.com/validate'
PROD_DNC_URL = 'https://api.realvalidation.com/rpvWebService/DNCLookup.php'
