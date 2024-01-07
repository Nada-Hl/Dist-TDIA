#!/usr/bin/env python3
import sys
import shutil     
import logging
import json
from datetime import datetime
with open("/etc/actualUser") as file:
    datauser = json.load(file)
    file.close()
user = datauser["Utilisateur"]
# Configuration du logger
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
logger = logging.getLogger(user)
def copy_files(source, destination):
    try:
        shutil.copy2(source, destination)
        success_message = f"Fichier '{source}' copié avec succès vers '{destination}'."
        print(success_message)
        logger.info(success_message)
    except Exception as e:
        error_message = f"Erreur lors de la copie de '{source}' vers '{destination}': {e}"
        print(error_message)
        logger.error(error_message)

def print_help():
    print("Usage: copy <source> <destination>")
    print("Copie le fichier source vers la destination.")
    print("Options:")
    print("  -h    Affiche cette aide.")

def main():
    if '-h' in sys.argv or len(sys.argv) != 3:
        print_help()
        sys.exit(0)

    source = sys.argv[1]
    destination = sys.argv[2]

    # Enregistrement des informations dans le journal
    log_entry = f"{datetime.now()} - Commande: {' '.join(sys.argv)} - "
    logger.info(log_entry)

    copy_files(source, destination)

if __name__ == "__main__":
    main()

