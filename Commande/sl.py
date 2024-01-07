#! /usr/bin/env python3
import os
import sys
import stat
import datetime
import logging
import json

with open("/etc/actualUser","r") as file:
     data=json.load(file)
     file.close()
logging.basicConfig(filename="/var/logging", level=logging.DEBUG,
                    format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")
user =data["Utilisateur"] 
logger = logging.getLogger(user)


def fct_l(directory='.', long_format=False):
    try:
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if long_format:
                file_info = os.stat(file_path)
                mode = stat.filemode(file_info.st_mode)
                size = file_info.st_size
                mtime = datetime.datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                print(f"{mode} {size:8} {mtime} {file}")
                logger.info("Affichage des informations du contenus de repertoire actuel")
            else:
                print(file)
                logger.info("ce n'est pas un repartoire")
    except FileNotFoundError:
        print(f"Le répertoire '{directory}' n'a pas été trouvé.")
        logger.error("le repertoire n'existe pas")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        logger.error("Erreur")


if len(sys.argv) < 2:
       fct_l()
       logger.info("affichage le contenu du repertoire actuel")

else:
     directory_path = sys.argv[1]
     long_format = '-l' in sys.argv
     fct_l(directory_path, long_format)
     logger.info("Affichage des informations du repertoire choisi")
