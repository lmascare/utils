#!/usr/local/bin/python3
"""Object Oriented Programming."""
from lank import obj_utils


def main():
    """OO Programming."""
    mylog = obj_utils.LogMe()
    mylog.error('ERROR Message', 1)
    mylog.warning('WARNING Message', 1)
    mylog.debug('DEBUG Message', 0)
    mylog.info('INFO Message', 0)
    # mylog.critical('Critical Message')


if __name__ == "__main__":
    main()
