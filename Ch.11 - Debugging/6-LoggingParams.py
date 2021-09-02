#Logging levels

import logging

#You can add a file to basicConfig to save log messages to a file
logging.basicConfig(level=logging.DEBUG, 
					format=' %(asctime)s - %(levelname)s - %(message)s',
					filename='programLog.txt')

#This will disable all logging at the specified level and below
#logging.disable(logging.CRITICAL)

logging.debug('Logging debug')
logging.info('logging info')
logging.warning('logging warning')
logging.error('logging error')
logging.critical('logging critical')