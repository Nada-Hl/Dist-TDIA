#!/usr/bin/env python3
import os
import json
import logging
import sys

with open("/etc/actualUser", "r") as file:
    data = json.load(file)
    file.close()
user = data["Utilisateur"]
userd = data["Repertoire"]
logging.basicConfig(filename='/var/logging', level=logging.DEBUG,
                    format='%(name)s | %(asctime)s | %(levelname)s | %(message)s')
logger = logging.getlogger(user)


def change(directory):
    with open("/etc/c", "w") as file:
        file.write(directory)
        file.close()


def check(usera):
    if usera != userd:
        print("Vous n'avez pas le droit d'acces a ce repertoire")
        with open("/etc/c", "w") as file:
            file.write("no")
            file.close()
            exit()
    return 1


if len(sys.argv) != 2:
    print("usage : aller chemin de repertoire ")
    with open("/etc/c", "w") as file:
        file.write("no")
        file.close()
        exit()
else:
    if '/' in sys.argv[1]:
        if sys.argv[1][0] == '/':
            path = sys.argv[1].split('/')[1]
            if path == "home":
                if check(sys.argv[1].split('/')[2]) == 1:
                    change(sys.argv[1])
        path = os.path.join(os.getcwd(), sys.argv[1])
        if path.split('/')[1] == "home":
            if check(path.split('/')[2]) == 1:
                change(path)
        else:
            change(path)
    else:
        path = os.path.join(os.getcwd(), sys.argv[1])
        if path.split('/')[1] == "home":
            if check(path.split('/')[2]) == 1:
                change(path)
        else:
            change(path)
