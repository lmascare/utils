#!/usr/bin/python
#


'''
Parse arguments list
'''

import argparse

parser = argparse.ArgumentParser(description="Calculate X to the power of Y")

'''
parser.add_argument("square",
                    type=int,
                    help="Display a square of the given number"
                    )
parser.add_argument("-v",
                   "--verbose",
                   type=int,
                   choices=[0,1,2],
                   help="Increase Verbosity",
                   )

answer = args.square**2
if args.verbose >= 2:
    print "The square of {} equals {}".format(args.square,answer)
elif args.verbose >= 1:
    print "{}^2 = {}".format(args.square, answer)
else:
    print answer
'''

'''
parser.add_argument("x", type=int, help="The base")
parser.add_argument("y", type=int, help="The exponent")


parser.add_argument("-v",
                    "--verbose",
                    default=0,
                    action="count",
                    help="Increase Verbosity",
                    )

args = parser.parse_args()
# print args.x
# print args.y
answer = args.x**args.y


if args.verbose >= 2:
    print "The power of {} raised {} equals {}".format(args.x, args.y ,answer)
elif args.verbose >= 1:
    print "{}^{} = {}".format(args.x,args.y, answer)
else:
    print answer
'''

'''
Mutually exclusive arguments
'''

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="The base")
parser.add_argument("y", type=int, help="The exponent")

args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print answer
elif args.verbose:
    print "{} to the power {} equals {}".format(args.x, args.y, answer)
else:
    print "{}^{} = {}".format(args.x, args.y, answer)
