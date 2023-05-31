import logging

# Set up logging
logging.basicConfig(filename='myapp.log', level=logging.DEBUG, format=\
    '%(asctime)s %(levelname)s %(message)s [%(pathname)s:%(lineno)d]', 
        filemode='w'
)

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')