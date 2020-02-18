#!/usr/bin/env python3

import math
import os

digits = os.getenv("DIGITS", default=2)

print("%.*f" % (int(digits), math.pi))
