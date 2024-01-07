#!/usr/bin/env python3
import sys
import os
import logging
import json
from datetime import datetime

# Configuration du logger
with open("/etc/actualUser"."r") as file:
    data=json.load(file)
    file.close()
user=data["Utilisateur"]
logging.basicConfig(filename='/var/logging', level=logging.DEBUG,
                    format='%(name)s | %(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
loggger=logging.getLogger(user)
def create_directories(directory_paths):
    for directory_path in directory_paths:
        try:
            # Utiliser la fonction os.makedirs pour créer le dossier s'il n'existe pas
            os.makedirs(directory_path, exist_ok=True)
            success_message = f"Dossier '{directory_path}' créé avec succès."
            print(success_message)
            loggger.info(success_message)
        except Exception as e:
            error_message = f"Erreur lors de la création du dossier '{directory_path}': {e}"
            print(error_message)
            loggger.error(error_message)

def print_help():
    print("Usage: createdir <nom_du_dossier1> [<nom_du_dossier2> ...]")
    print("  Crée les dossiers s'ils n'existent pas.")
    print("  Affiche un message si le dossier existe déjà.")
    print("Options:")
    print("  -h    Affiche cette aide.")

def main():
    if len(sys.argv) < 2 or '-h' in sys.argv:
        print_help()
        sys.exit(0)
    # Enregistrement des informations dans le journal
    log_entry = f"{datetime.now()} - Commande: {' '.join(sys.argv)} - "
    loggger.info(log_entry)
    directory_paths = sys.argv[1:]
    create_directories(directory_paths)

if _name_ == "_main_":
    main()
