#!/usr/bin/env python3

import argparse
import logging
import getpass
import sys  # Import the sys module
from datetime import datetime
import json

# Configuration du logger
with open("/etc/actualUser") as file:
    datauser = json.load(file)
    file.close()
user = datauser["Utilisateur"]
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
logger = logging.getLogger(user)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            # Include the command in the log entry
            log_entry = f"{datetime.now()} - Commande: {' '.join(sys.argv)} - Contenu du fichier : {content}"
            logger.info(log_entry)
    except FileNotFoundError:
        error_message = f"Le fichier '{file_path}' n'existe pas."
        print(error_message)
        logger.error(error_message)
    except Exception as e:
        error_message1 = f"Une erreur s'est produite : {e}"
        print(error_message1)
        logger.error(error_message1)

def main():
    parser = argparse.ArgumentParser(description="Imite la commande 'cat' en affichant le contenu d'un fichier.")
    parser.add_argument('file_path', help="Chemin complet du fichier à lire")
    
    # Enregistrement des informations dans le journal
    args = parser.parse_args()
    read_file(args.file_path)

if __name__ == "__main__":
    # Move logging outside of the main function to ensure consistent logging
    log_entry = f"{datetime.now()} - Commande: {' '.join(sys.argv)} - Script exécuté."
    logger.info(log_entry)
    main()

