#!/usr/bin/env python3

users = [
    {
        'admin': False,
        'active': False,
        'name': 'A'
    },
    {
        'admin': True,
        'active': True,
        'name': 'B'
    },
    {
        'admin': True,
        'active': False,
        'name': 'C'
    }, {
        'admin': False,
        'active': True,
        'name': 'D'
    }
]

line = 1

for user in users:
    prefix = f"{line}"

    if user['admin'] == True and user['active'] == True:
        prefix += "ACTIVE - (ADMIN)"
    elif user['admin'] == True:
        prefix += "(ADMIN)"
    elif user['active'] == True:
        prefix += "ACTIVE - "

    print(prefix + " " + user['name'])
    line += 1
