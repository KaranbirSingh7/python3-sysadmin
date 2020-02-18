#!/usr/bin/env python3

import argparse

import sys

# BUILD COMMAND PARSER
parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='The file to read data from')
parser.add_argument('--line_number', '-l', type=int,
                    help='Line number to read')
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s 1.0')

# PARSE ALL ARGUMENTS
args = parser.parse_args()

try:
    lines = open(args.file_name, 'r').readlines()
    line = lines[args.line_number-1]
except IndexError:
    print(
        f"Error: file '{args.file_name}' doesn't have {args.line_number} lines.")
except FileNotFoundError:
    print(f"Cannot find file: {args.file_name}")
else:
    print(line)
