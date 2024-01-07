#! /usr/bin/env python3
import sys
import os
import sys
import logging
import json
with open("/etc/actualUser","r") as file:
      datauser=json.load(file)
      file.close()
user = datauser["Utilisateur"]
userd=datauser["Repertoire"]
user_directory="/home/{}".format(userd)
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
logger = logging.getLogger(user)


def concatener_fichiers(chemin_sortie, *chemins_entree):
    with open(chemin_sortie, 'wb') as fichier_sortie:
        for chemin_entree in chemins_entree:
            with open(chemin_entree, 'rb') as fichier_entree:
                contenu_entree = fichier_entree.read()
                fichier_sortie.write(contenu_entree)

    logger.info("la concaténation des fichiers")


if len(sys.argv) < 4:
        print("Usage: concat fichier_sortie fichier1 fichier2 ... fichierN")
        logger.error("le nombre d'arguments est invalable")
        sys.exit(1)

fichier_sortie = sys.argv[1]
fichiers_entree = sys.argv[2:]
if len(fichiers_entree) > 10:
    print("Erreur : Vous ne pouvez concaténer que jusqu'à 10 fichiers.")
    logger.error("le nombre d'arguments est invalable")
    sys.exit(1)
else:
    concatener_fichiers(fichier_sortie, *fichiers_entree)
    print("Concaténation réussie.")
