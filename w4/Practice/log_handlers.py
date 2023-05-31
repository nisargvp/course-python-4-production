import logging

## StreamHandler: send log messages to streams such as sys.stdout, sys.stderr or any file-like object
# create a logger object
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# create a StreamHandler and set its level to INFO
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

# create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)

# attach the handler to the logger object
logger.addHandler(sh)

# log some messages
logger.debug('debug message')  # this message won't be shown because its level is lower than INFO
logger.info('info message')  # this message will be shown because its level is INFO
logger.warning('warning message')

## FileHandler: send log messages to a file
# create a logger and set its logging level
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# create a FileHandler and set its logging level
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.DEBUG)

# create a Formatter and add it to the FileHandler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# add the FileHandler to the logger
logger.addHandler(file_handler)

# log some messages
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')

##TimeRotatingFileHandler: send log messages to a file and rotate the log file at certain timed intervals
import time
from logging.handlers import TimedRotatingFileHandler

# create a logger and set its logging level
logger = logging.getLogger('example_timed_logger')
logger.setLevel(logging.DEBUG)

# create a TimedRotatingFileHandler that rotates daily
handler = TimedRotatingFileHandler(filename='example_timed.log', when='D', interval=1, backupCount=7)

# set the logging level of the handler
handler.setLevel(logging.DEBUG)

# create a Formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(handler)

# log some messages
for i in range(10):
    logger.debug('Debug message %d' % i)
    time.sleep(1)