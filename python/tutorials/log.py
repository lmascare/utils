#!/usr/bin/python3
#
import logging
import sys
import os

scriptname = os.path.basename(sys.argv[0])
print(scriptname)

LOG_FILENAME = '/tmp/example.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,
        format='%(asctime)s:%(levelname)-8s:%(filename)s:%(process)d:%(message)s',
                    datefmt='%m-%d-%Y %H:%M:%S'
                    )
logging.debug('This DEBUG message should go to the log file')
logging.info('This INFO message should go to the log file')

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.WARNING)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")
