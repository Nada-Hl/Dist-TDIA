#! /usr/bin/env python3
import sys
import json
import logging

import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)
with open("/etc/actualUser",'r') as file:
    datauser=json.load(file)
    file.close()
user=datauser["Utilisateur"]
userd=datauser["Repertoire"]
logging.basicConfig(filename="/var/logging",filemode="a",level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s ")
logger=logging.getLogger(user)

commands ={
    'accio':'Le chemin du fichier donne',
    'calendar':'Afficher le calendrier',
    'change':'Changer le chemin du fichier ou repertoire',
    'class':'classer un fichier',
    'clock':'Horloge/Chrono',
    'concat':'Concatenation des fichiers',
    'copy':'Copier repertoire ou fichier du chemin source vers chemin destinee',
    'count':'ccompter le nombre de lignes/mots/caracteres du fichier ',
    'crf':"Creation d'un fichier",
    'cruser':"Creation d'un utilisateur ",
    'edit':"editer fichier ",
    'eraseusr':'efacer un utilisateur',
    'evanesco':'Supprime un fichier ou repertoire',
    'flgf':'Trouve les fichiers larges',
    'ftranslate':'Traduction de fichier',
    'rendition':'Traduction de mot',
    'getdate':'Recupperer la date',
    'gethostname':'Le nom de la machine',
    'hat':'Liste les 10 premiers lignes du fichier',
    'lock':"lock/Unlock fichier",
    'rdf':'Read file',
    'search':'Cherche un fichier',
    'sl':'Liste le contenu du repertoire',
    'switch':'changement a un autre utilisateur',
    'tache':'Progression de CPU ou GPU',
    'toe':'Liste les 10 derniers lignes du fichier',
    'whereami':'Chemin actuel',
    'go':'Changement du direction',
    'alterego':'modification des informatioins dUtilisateur',
    'creatdir':'Creer des repertoires',
}
if len(sys.argv)==2:
    if sys.argv[1] in commands.keys():
        comm=Fore.MAGENTA +"{}{}".format(sys.argv[1],Style.DIM)
        print(comm,end=" ")
        print(commands[sys.argv[1]])
    else:
        print("Cette commande n'existe pas")
else:
    for i in commands.keys():
        comm = Fore.MAGENTA + "{}{}".format(i,Style.DIM)
        print(comm, end=" ")
        print(commands[i])