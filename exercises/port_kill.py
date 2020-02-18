#!/usr/bin/env python3

import subprocess as sb
import argparse
import os

# BUILD PARSER
parser = argparse.ArgumentParser()
parser.add_argument('--port', '-p', required=True,
                    help='PORT to kill', type=int)

args = parser.parse_args()
port = args.port

try:
    result = sb.run(['lsof', '-n', "-i4TCP:%s" %
                     port], stderr=sb.PIPE, stdout=sb.PIPE)
except sb.CalledProcessError:
    print(f"No process listening on port {port}")
else:
    listening = None
    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            break

    if listening:
        # PID is the second column in the output
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print(f"Killed process {pid}")
    else:
        print(f"No process listening on port {port}")
