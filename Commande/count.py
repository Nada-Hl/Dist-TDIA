#! /usr/bin/env
import argparse
import sys
import logging
import json

log_file = '/var/logging'

with open ("/etc/actualUser") as file :
       datauser=json.load(file)
user=datauser["Utilisateur"]
logger = logging.getLogger(user)

logging.basicConfig(filename=log_file, level=logging.DEBUG, format=f'{user} | %(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def count(file_path, lignes=True, mots=True, caracteres=True):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        line_count = len(content.splitlines()) if lignes else 0
        word_count = len(content.split()) if mots else 0
        char_count = len(content) if caracteres else 0

        if lignes:
            print(f"Lignes: {line_count}")
            logging.info(f"Compte les lignes de fichier {file_path}")
        if mots:
            print(f"Mots: {word_count}")
            logging.info(f"Compte les mots de fichier {file_path}")
        if caracteres:
            print(f"Caracteres: {char_count}")
            logging.info(f"Compte les caractéres de fichier {file_path}")

    except FileNotFoundError:
        print(f"Erreur: Fichier '{file_path}' n'existe pas.")
        logging.error(f"Le fichier'{file_path}' n'existe pas.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compte les lignes, mots et caractére d'un fichier.")
    parser.add_argument("file", help="Chemin du fichier")
    parser.add_argument("-l", "--lines", action="store_true", help="Comppte les lignes")
    parser.add_argument("-w", "--words", action="store_true", help="Compte les mots")
    parser.add_argument("-c", "--characters", action="store_true", help="Compte les caractéres")

    args = parser.parse_args()

    if not any([args.lines, args.words, args.characters]):
        print("Erreur: Au minimum une option (-l, -w, -c) doit etre specifié.")
        logging.error("La syntaxe est incorrect")
        sys.exit(1)

    count(args.file, args.lines, args.words, args.characters)
