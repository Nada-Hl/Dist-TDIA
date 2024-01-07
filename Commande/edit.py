#! /usr/bin/env python3
import sys
import json
import getpass
import subprocess
import logging
logging.basicConfig(filename="/var/logging",filemode="a",level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s ")
with open("/etc/usersfile","r") as file:
    datafile=json.load(file)
    file.close()
with open("/etc/actualUser","r") as file:
    datauser=json.load(file)
    file.close()
user=datauser["Utilisateur"]
logger=logging.getLogger(user)
try:
    if len(sys.argv)!=2:
        print("ERREUR : sélectionnez un seul argument")
        logger.error("mauvaise utilisation de l'éditeur : plus d'un argument")
    else:
        x=None
        for key ,value in datafile[user].items():
            if sys.argv[1]==key:
                x=1
                break
        if x:
            if datafile[user][sys.argv[1]] == "":
                subprocess.run(['nano',sys.argv[1]])
            else:
                password = getpass.getpass(prompt="would check the password")
                logger.info("{} édité".format(sys.argv[1]))
                if password == datafile[user][sys.argv[1]]:
                    subprocess.run(['nano',sys.argv[1]])
                    logger.info("{} édité".format(sys.argv[1]))
                else:
                    print("ERREUR : mot de passe incorrect ")
                    logger.error("impossible d'ouvrir {} (mot de passe incorrect)".format(sys.argv[1]))
        else:
            print("ERREUR : ce fichier n'existe pas")
            logger.error("Le fichier {} n'existe pas".format(sys.argv[1]))
except KeyboardInterrupt:
    exit(0)
