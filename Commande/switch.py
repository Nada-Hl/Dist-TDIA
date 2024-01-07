#!/usr/bin/env python3
import sys
import subprocess
import getpass
import json
import crypt
import logging
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
def add_file_json(username,directory):
    data_user={"Utilisateur":username,"Repertoire":directory.strip('\n')}
    with open("/etc/actualUser","w") as file:
        json.dump(data_user,file,indent=2)
        file.close()
def authenticate_user(username, password, user_info):
    for line in user_info:
        user_data = line.split(':')
        if user_data[0] == username:
            stored_password = user_data[1]
            if crypt.crypt(password,stored_password)==stored_password:
                print(f"Authentification réussie ! Bienvenue, {username}.")
                logger=logging.getLogger(username)
                logger.info("Changer l'utilisateur a {}".format(username))
                add_file_json(username,user_data[4])
                return user_data[4]  # Return the directory if authentication is successful
            else:
                with open("/etc/b", "w") as file:
                    file.write("no")
                    file.close()
                print("Authentification échouée. Mot de passe incorrect.")
                return None
    print("Utilisateur non trouvé.")
    return None
try:
    def main():
        if len(sys.argv) != 2:
            print("Usage: switch <username>")
            sys.exit(1)

        username = sys.argv[1]
        password = getpass.getpass(prompt="Entrer mot de passe: ")
        with open("/etc/password", "r") as file:
            user_directory = authenticate_user(username, password, file)
            file.close()
            if user_directory:
                try:
                    with open ("/etc/a","w") as file:
                        file.write("/home/{}".format(user_directory))
                        file.close()
                    with open ("/etc/b","w") as file:
                        file.write("yes")
                        file.close()

                    print(user_directory)
                    path = ("/home/{}".format(user_directory)).strip('\n')
                    print(f"Répertoire modifié en: {user_directory}")
                except subprocess.CalledProcessError as e:
                    print(f"Erreur lors du changement du répertoire: {e}")

    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    exit(0)

