#! /usr/bin/env python3
import argparse
import sys
import json
import logging

log_file = '/var/logging'

with open ("/etc/actualUser") as file :
       datauser=json.load(file)
user=datauser["Utilisateur"]
logger = logging.getLogger(user)

logging.basicConfig(filename=log_file, level=logging.DEBUG, format=f'{user} | %(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def custom_sort(file_path, reverse=False, numeric=False):
    try:
        sort_type = "renverse" if reverse else "normal"
        sort_type += " (numerique)" if numeric else ""

        logging.info(f"Le fichier {file_path} est classé en ordre {sort_type} .")
        with open(file_path, 'r') as file:
            lines = file.readlines()

        def key_func(x):
            if numeric:
                return (float(x) if x.strip().lstrip('-').replace('.', '').isdigit() else float('inf'), x)

            else:
                return (0 if x.strip().lstrip('-').replace('.', '').isdigit() else 1, x.lower())

        sorted_lines = sorted(lines, key=key_func, reverse=reverse)

        for line in sorted_lines:
            print(line, end="")

    except FileNotFoundError:
        print(f"Fichier '{file_path}' n'existe pas.")
        logging.error(f"Le fichier'{file_path}' n'existe pas.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classer le fichier par ordre lexicographique.")
    parser.add_argument("file", help="Chemin du fichier")
    parser.add_argument("-r", "--reverse", action="store_true", help="Classer en ordre inverse")
    parser.add_argument("-n", "--numeric", action="store_true", help="Classer par ordre numérique")
    
    args = parser.parse_args()

    custom_sort(args.file, args.reverse, args.numeric)






