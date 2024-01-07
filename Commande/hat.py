#! /usr/bin/env python3
import sys
import logging
import json
import os
with open("/etc/actualUser","r") as file:
    datauser = json.load(file)
    file.close()
user = datauser["Utilisateur"]
userd=datauser["Repertoire"]
user_directory="/home/{}".format(userd)
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
logger = logging.getLogger(user)
def search_file(filename):
    for i, j, k in os.walk(user_directory):
        if filename in k:
            return os.path.join(i,filename)
    return None
def fct_h(file_path, num_lines=10):
    try:
        with open(file_path, 'r') as file:
            for _ in range(num_lines):
                line = file.readline().rstrip('\n')
                if not line:
                    break
                print(line)
        logger.info("Affichage de {num_lines} lignes premiers du fichier {file_path}")
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' n'a pas été trouvé.")
        logger.error("le fichier {file_path} est introuvable")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        logger.error("Erreur")
if len(sys.argv) < 2:
    print("Utilisation : hat <fichier> [nombre_de_lignes]")
    logger.error("Le nombre d'arguments est invalide.")
    sys.exit(1)
file_path = sys.argv[1]
num_lines = int(sys.argv[2]) if len(sys.argv) > 2 else 10
if '/' in file_path:
    if search_file(file_path.split('/')[-1]):
        fct_h(file_path.split('/')[-1],num_lines)
    else:
        print("Ce fichier n'existe pas")
        logger.error(f"le fichier {file_path} est non trouvable.")
else:
    if search_file(file_path):
        fct_h(search_file(file_path),num_lines)
    else:
        print("Ce fichier n'existe pas ")
        logger.error(f"le fichier {file_path} est non trouvable.")
