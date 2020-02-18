#!/usr/bin/env python3
import os

################### SIMPLE SOLUTION #######################

file_name = input("What do you want to name your file?: ")
file_path = f"/tmp/{file_name}"

with open(file_path, 'a') as f:
    content = input("Writer your content below:\n")
    f.write(content)

print(f"/tmp/{file_name} has been created.")


############ ROBUST/INSTRUCTOR SOLUTION ######################
def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a file name.")

    file_name = input("Destination file name: ").strip()
    return file_name or get_file_name(True)


file_name = get_file_name()

print(
    f"Please enter your content. Entering an empty line will write the content to {file_name}:\n")

with open(file_name, 'w') as f:
    eof = False
    lines = []

    while not eof:
        line = input()
        if line.strip():
            lines.append(f"{line}\n")
        else:
            eof = True

    f.writelines(lines)
    print(f"Lines written to {file_name}")
