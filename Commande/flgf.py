#!/usr/bin/env python3
import os
import sys
import logging
import getpass
from datetime import datetime
import json

# Configuration du logger
with open("/etc/actualUser") as file:
    datauser = json.load(file)
    file.close()
user = datauser["Utilisateur"]
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
logger = logging.getLogger(user)

def afficher_grands_fichiers_et_sous_repertoires(chemin, taille_seuil):
    """
    Affiche les grands fichiers et les sous-répertoires à partir du chemin spécifié.
    :param chemin: Le chemin du répertoire à explorer.
    :param taille_seuil: La taille minimale (en octets) pour qu'un fichier soit considéré comme "grand".
    """
    logger.info(f"- Commande: {' '.join(sys.argv)} - Exploration du répertoire : {chemin}",)

    for repertoire_courant, sous_repertoires, fichiers in os.walk(chemin):
        # Afficher les sous-répertoires
        for nom_sous_repertoire in sous_repertoires:
            chemin_complet_sous_repertoire = os.path.join(repertoire_courant, nom_sous_repertoire)
            logger.info(f"- Commande: {' '.join(sys.argv)} - Sous-répertoire : {chemin_complet_sous_repertoire}")

        # Afficher les grands fichiers
        for nom_fichier in fichiers:
            chemin_complet_fichier = os.path.join(repertoire_courant, nom_fichier)
            taille_fichier = os.path.getsize(chemin_complet_fichier)
            if taille_fichier > taille_seuil:
                print(f"Grand fichier : {chemin_complet_fichier} ({taille_fichier} octets)")
                logger.info(f"- Commande: {' '.join(sys.argv)} - Grand fichier : {chemin_complet_fichier} ({taille_fichier} octets)")

if __name__ == "__main__":
    # Vérifier si les arguments sont fournis
    if len(sys.argv) != 3:
        print("Usage: script <chemin> <taille_seuil>")
        sys.exit(1)

    # Récupérer le chemin et la taille seuil à partir des arguments
    chemin_utilisateur = sys.argv[1]
    taille_seuil_utilisateur = int(sys.argv[2])

    # Vérifier si le chemin existe
    if os.path.exists(chemin_utilisateur):
        # Appeler la fonction pour afficher les grands fichiers et les sous-répertoires
        afficher_grands_fichiers_et_sous_repertoires(chemin_utilisateur, taille_seuil_utilisateur)
    else:
        logger.error(f"- Commande: {' '.join(sys.argv)} - Le chemin spécifié n'existe pas.")
        print("Le chemin spécifié n'existe pas.")

