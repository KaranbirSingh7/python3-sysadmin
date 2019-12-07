#!/usr/bin/env python3

import os

stage = os.getenv("STAGE", default="Development").upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
