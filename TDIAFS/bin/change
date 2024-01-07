#!/usr/bin/env python3

import os
import shutil
import sys
import json
import logging
with open("/etc/actualUser","r") as file:
       datauser=json.load(file)
       file.close()
user = datauser["Utilisateur"]
userd=datauser["Repertoire"]
user_directory="/home/{}".format(userd)
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
logger = logging.getLogger(user)
def rename_file_or_directory(old_path, new_name):
    try:
        os.rename(old_path, os.path.join(os.path.dirname(old_path), new_name))
        print(f"Renommé avec succés de {old_path} à {new_name}")
        logger.info(f"Renommé avec succés de {old_path} à {new_name}")
    except Exception as e:
        print(f"Erreur lors du renommage {old_path}: {e}")
        logger.error(f"Erreur lors du renommage {old_path}: {e}")

def move_file_or_directory(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"Transféré avec succés de {source_path} à {destination_path}")
        logger.info(f"Transféré avec succés de {source_path} à {destination_path}")
    except Exception as e:
        print(f"Erreur lors du transfert de {source_path} à {destination_path}: {e}")
        logger.error(f"Erreur lors du transfert de {source_path} à {destination_path}: {e}")

def display_help():
    print("Usage:Cette fonction est utilisée pour changer le nom d'un fichier ou d'un répertoire, ou pour déplacer un fichier ou un répertoire.")
    print(" -r <ancien_chemin> <nouveau_chemin>        : Changer le nom de fichier ou de répertoire")
    print(" -m <chemin_source> <chemin_destinee>       : Transférer un fichier ou un répertoire")
    print(" --help                                     : Montrer le menu d'aide")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Use 'change --help' pour le menu d'information.")
        sys.exit(1)

    if sys.argv[1] == "--help":
        display_help()
        sys.exit(0)
    if len(sys.argv) < 4:
       print("Nombre d'arguments non valide, utilisez 'change --help' pour les informations d'utilisation.")
       sys.exit(1)



    operation = sys.argv[1]
    old_path = sys.argv[2]
    new_path = sys.argv[3]

    if operation == "-r":
        rename_file_or_directory(old_path, new_path)
    elif operation == "-m":
        move_file_or_directory(old_path, new_path)
    else:
        print("Operation invalide")
        display_help()

