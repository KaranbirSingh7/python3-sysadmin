#!/usr/bin/env python3.6

import argparse
import sys

# Build Parser
parser = argparse.ArgumentParser(
    description='Read a file in reverse', prog='String Reverser')

parser.add_argument('filename', help='the file to read text from')
parser.add_argument('--limit', '-l', type=int, help='number of lines to read')
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s 1.0')

# Parse all arguments
args = parser.parse_args()


# Reverse all the lines
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
