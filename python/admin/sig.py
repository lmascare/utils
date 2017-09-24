#!/usr/bin/python

"""
Signal Handling Example.

This script shows how to handle various signals in Python.
Note that SIGQUIT and SIGKILL cannot be processed.
"""

import signal
import sys


def sig_handler(signal, frame):
    """Signal handling routine. Display the signal number and exit."""
    print("Signal sent --> {}".format(signal))
    sys.exit(0)


def main():
    """
    Signal Processing.

    -SIGHUP signal. Similar to exit 1.
    -SIGINT signal. CTRL-C signal number 2.
    -SIGTERM signal. Signal number 15.
    -signal.pause(). Wait for a signal. Call sig_handler.
    """
    signal.signal(signal.SIGHUP, sig_handler)

    signal.signal(signal.SIGINT, sig_handler)

    signal.signal(signal.SIGTERM, sig_handler)

    print('Send signal : ')

    signal.pause()


if __name__ == "__main__":
    main()
