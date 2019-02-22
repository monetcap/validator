import logging
import sys

from .constants import LOG_FORMAT, LOG_LEVEL

file_handler = logging.FileHandler('./output/validator.log')
stream_handler = logging.StreamHandler()

handlers = [file_handler, stream_handler]

logging.basicConfig(level=LOG_LEVEL,
                    format=LOG_FORMAT,
                    handlers=handlers)

log = logging.getLogger(__name__).debug('initialized logger')
