#!/usr/bin/env python3

#  FUNCTION


def myPrinter(message, count):
    for c in range(int(count)):
        line = c+1
        print(f"\n#{line}: {message}")


# MAIN EXECUTION
message = input("Favourite sports? ")
count = input("Repeats: ").strip()

myPrinter(message, count)
