#!/usr/bin/env python3


import requests
import sys
import json

from argparse import ArgumentParser

argparse = ArgumentParser("CLI to download URL provided data in html/json")

argparse.add_argument(
    "filename", help="filename where webpage will be downloaded/stored"
)
argparse.add_argument("--url", "-u", help="Full address to webpage")
argparse.add_argument(
    "--type",
    "-t",
    default="html",
    choices=["html", "json"],
    help="The content type of requested URL to save",
)

args = argparse.parse_args()

# MAKE requests
r = requests.get(args.url)

if r.status_code > 400:
    print(f"Unknown error occured: {r.status_code}")
    sys.exit(1)

if args.type == "json":
    try:
        content = json.dumps(r.json())
    except ValueError:
        print("Error: Content is not supported in JSON")
        sys.exit(1)
else:
    content = r.text

with open(args.filename, "w") as f:
    f.write(content)
    print(f"Content written to {args.filename}")
