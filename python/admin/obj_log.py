#!/usr/local/bin/python3
"""Object Oriented Programming."""
from lank import obj_utils


def main():
    """OO Programming."""
    mylog = obj_utils.LogMe()
    mylog.error('ERROR Message')
    mylog.warning('WARNING Message')
    mylog.debug('DEBUG Message')
    mylog.info('INFO Message')
    # mylog.critical('Critical Message')


if __name__ == "__main__":
    main()
