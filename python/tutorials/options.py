#!/usr/bin/python
#
from optparse import OptionParser

usage = "usage: %prog [options] arg1 arg2"

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                 help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                 action="store_false", dest="verbose", default=True,
                 help="don't print status messages to stdout")
parser.add_option("-m", "--mode", 
                 default="intermediate",
                 help="interactive mode: novice intermediate, "
                 "or expert [default: %default]")
parser.add_option("-n", type="int", dest="num")
parser.add_option("-v", action="store_true", dest="verbose")

(options,args) = parser.parse_args()
