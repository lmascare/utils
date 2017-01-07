#!/usr/bin/env python3
#
import fileinput

with fileinput.input(files='/etc/passwd') as f:
    # with fileinput.input() as f:
    for line in f:
        print(f.filename(),f.lineno(), line, end='')

