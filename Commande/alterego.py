#! /usr/bin/env python3
import sys
import os
import crypt
from datetime import datetime
import logging
import json
import shutil

fileps = "/etc/password"
log_file = "/var/log/logging"

with open ("/home/dana/file.json") as file :
       datauser=json.load(file)
user=datauser["Utilisateur"]
logger = logging.getLogger(user)

logging.basicConfig(filename=log_file, level=logging.DEBUG, format=f'{user} | %(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def print_help():
        print("Usage: python3 alterusr.py <username> <option1> <value1> [<option2> <value2> ...]")
        print("Options:")
        print("-a  : Renommer (alias)")
        print("-cp : Changer le mot de passe (change password)")
        print("-cs : Spécifier une date d'expiration (Chrono Seal)")
        print("-i  : Changer l'UID (Identité)")
        print("-d  : Changer le répertoire personnel (Dwelling)")
        logging.info("Affichage du menu")
        sys.exit(0)

def alter_ego(username, options):
    valid_options = ['-a', '-cp', '-cs', '-i', '-d']
    if os.geteuid() != 0:
        print("Vous devriez avoir les droits d'accees de root.")
        logging.error("N'a pas les droits d'acces de root.")
        sys.exit(1)

    with open(fileps, 'r') as f:
        lines = f.readlines()

    option_found = False
    user_exists = False

    for i, line in enumerate(lines):
        if line.startswith(username + ":"):
            user_exists = True
            fields = line.split(':')

            for option in valid_options:
                if option in options:
                    option_found = True

                    if option == '-a':
                        new_alias = options[option]
                        fields[0] = new_alias
                        logging.info(f"{username} (Nom) est change a {new_alias}")

                    elif option == '-cp':
                        new_password = options[option]
                        set_password(username, new_password)

                    elif option == '-cs':
                        chrono_seal = options[option]
                        set_expiration_date(username, chrono_seal)

                    elif option == '-i':
                        new_uid = options[option]
                        fields[2] = str(new_uid)
                        logging.info(f"{username} (UID) est change a {new_uid}")

                    elif option == '-d':
                        new_dwelling = options[option]
                        fields[4] =f"{new_dwelling}"
                        old_home_dir = f"/home/{username}"
                        new_home_dir = f"/home/{new_dwelling}"
                        try:
                             shutil.move(old_home_dir, new_home_dir)
                             logging.info(f"{username} (Repertoire) est change a {new_dwelling}")
                        except Exception as e:
                             print(f"Erreur lors du changement de repertoire: {e}")

            lines[i] = ":".join(fields)

    if not user_exists:
        print(f"L'utilisateur {username} n'existe pas.")
        logging.error(f"L'utilisateur entrer ({username}) n'existe pas.")
        sys.exit(1)

    with open(fileps, 'w') as f:
        f.writelines(lines)

    if not option_found:
        print("L'option que vous avez entrée est invalide.")
        print("Options disponibles :")
        print("-a  : Renommer (alias)")
        print("-cp : Changer le mot de passe")
        print("-cs : Spécifier une date d'expiration (Chrono Seal)")
        print("-i  : Changer l'UID (Identité)")
        print("-d  : Changer le répertoire personnel (Dwelling)")
        logging.error("L'option entrer n'existe pas.")
        sys.exit(1)
def set_password(username, password):
    hashed_password = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

    with open(fileps, "r") as password_file:
        password_lines = password_file.readlines()

    for i, line in enumerate(password_lines):
        if line.startswith(username + ":"):
            fields = line.split(':')
            fields[1] = hashed_password
            password_lines[i] = ":".join(fields)

    with open(fileps, "w") as password_file:
        password_file.writelines(password_lines)
    logging.info(f"Mot de passe de {username} est changé avec succès.")

def set_expiration_date(username, expiration_date):
    expiration_datetime = datetime.strptime(expiration_date, "%Y-%m-%d")
    formatted_expiration_date = expiration_datetime.strftime("%Y-%m-%d")

    with open(fileps, "r") as password_file:
        password_lines = password_file.readlines()

        for i, line in enumerate(password_lines):
            if line.startswith(username + ":"):
                fields = line.split(':')
                fields[3] = formatted_expiration_date
                password_lines[i] = ":".join(fields)

    with open(fileps, "w") as password_file:
        password_file.writelines(password_lines)
    logging.info(f"La date d'expiration de {username} est fixée à {formatted_expiration_date}.")

if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()

    if len(sys.argv) < 4 or (len(sys.argv) - 2) % 2 != 0:
        print("Usage : python3 alterusr.py <username> <option1> <valeur1> [<option2> <valeur2> ...]")
        logging.error("La syntaxe entrer est invalide")
        sys.exit(1)

    username = sys.argv[1]
    options = {sys.argv[i]: sys.argv[i + 1] for i in range(2, len(sys.argv), 2)}

    alter_ego(username, options)

    print(f"L'utilisateur {username} est modifié avec succès.")

