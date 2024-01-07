#!/usr/bin/env python3

import os
import shutil
import sys
import logging
import json
with open("/etc/actualUser","r") as file :
       datauser=json.load(file)
       file.close()
user = datauser["Utilisateur"]
userd=datauser["Repertoire"]
user_directory="/home/{}".format(userd)
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
logger = logging.getLogger(user)

def delete_directory(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            print(f"Erreur: impossible de supprimer '{path}' n'est pas un répertoire.")
            logger.error(f"Error: impossible de supprimer '{path}' n'est pas un répertoire.")
    except Exception as e:
        print(f"Erreur: {e}")

def delete_file(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
        else:
            print(f"Erreur: impossible de supprimer '{path}' n'est pas un fichier.")
            logger.error(f"Erreur: impossible de supprimer '{path}' n'est pas un fichier.")
    except Exception as e:
        print(f"Error: {e}")

def display_help():
    print("Usage: delete [option] [file]  ")
    print("\nOptions:")
    print("  -r, --recursive  Supprimez les répertoires de manière récursive.")
    print("  -h, --help       Affichez ce message d'aide.")
    sys.exit(0)

def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        display_help()

    if len(sys.argv) < 2:
        print("Erreur : argument manquant. Utilisez 'delete --help' pour plus d'informations")
        sys.exit(0)

    path = sys.argv[-1]
    option = sys.argv[1]

    if os.path.exists(path):

        if option == "-r":
            delete_directory(path)
        else:
            delete_file(path)
    else:
        print(f"Erreur: '{path}' n'existe pas.")


if __name__ == "__main__":
    main()
