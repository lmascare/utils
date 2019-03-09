#!/usr/local/bin/python3
"""Object Oriented Programming."""
from lank import obj_utils


def main():
    """OO Programming."""
    mylog = obj_utils.logme()
    # mylog.critical('Critical Message')
    mylog.error('Error Message')
    mylog.warning('Warning Message')
    mylog.debug('DEBUG Message')
    mylog.info('INFO Message')


if __name__ == "__main__":
    main()
