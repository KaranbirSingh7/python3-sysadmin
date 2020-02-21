#!/usr/bin/env python3

import requests
import argparse
import os
import sys

# PARSE LOCATION
parser = argparse.ArgumentParser(
    description='Get current weather forecast for your city')
parser.add_argument('--location', '-l',
                    help='location/city for which you want to check weather for', required=True)
parser.add_argument('--country', '-c', default='canada',
                    help='country where city belongs, default is canada')
args = parser.parse_args()


# GET ENV API KEY VALUE
owm_api_key = os.getenv('OWM_API_KEY')

if not owm_api_key:
    print("Error: no API key specified for environment variable OWM_API_KEY")
    sys.exit(1)

# MAKE REQUEST
url = f"https://api.openweathermap.org/data/2.5/weather?q={args.location},{args.country}&appid={owm_api_key}"
r = requests.get(url)

if r.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")


# SHOW DATA TO USER
print(r.json())
