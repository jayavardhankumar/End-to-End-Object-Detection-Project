from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys
#ty

#logging.info("welcome to the project ")

try:
    a = 7/'9'

except Exception as e:
    raise SignException(e,sys) from e
