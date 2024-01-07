#!/usr/bin/env python3
import logging
import os
from argparse import ArgumentParser,Namespace
import getpass
import random
import json
from tqdm import tqdm
import time
import crypt
iteration_color = '\033[96m'
completion_color = '\033[91m'
progress_bar_color = '\033[92m'
reset_color = '\033[0m'
total_iterations = 100
logging.basicConfig(filename="/var/logging",filemode="a",level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s ")
try :
    def create_user_directory(username):
        path=os.path.join("/home/",str(username))
        try:
            os.makedirs(path)
        except:
            print("Ce répertoire existe déjà")
            logger=logging.getLogger(str(username))
            logger.debug("Le Répertoire {} existe déjà ".format(str(username)))
            return 0
        else:
            logger = logging.getLogger(str(username))
            logger.info("Le répertoire {} a été ajouté avec succès".format(str(username)))
    def check_username(name):
        with open("/etc/password","r") as file :
            lignes=file.readlines()
            for ligne in lignes:
                if name==ligne.split(":")[0]:
                    file.close()
                    return 1
            file.close()
            return 0
    def assign_uid():
        uid =random.randint(1000,32767)
        with open("/etc/password",'r') as f:
            lignes=f.readlines()
            list=[]
            for ligne in lignes:
                list.append(int(ligne.split(':')[2]))
            f.close()
            while uid in list:
                uid = random.randint(1000, 32767)
        return uid

    def add_to_json_file(user):
        with open("/etc/usersfile","r") as file:
            data=json.load(file)
            file.close()
        data[user]={}
        with open("/etc/usersfile", "w") as file:
            json.dump(data,file,indent=2)
            file.close()






    parser=ArgumentParser()
    parser.add_argument('username',type=str,help="The username")
    args:Namespace = parser.parse_args()
    if check_username(args.username):
        print("Cet identifiant existe déjà")
        logger = logging.getLogger(str(args.username))
        logger.error("Cet identifiant {} existe déjà".format(str(args.username)))
    else:
        password=getpass.getpass(prompt="Entrer votre mot de passe :")
        password2=getpass.getpass(prompt="re-entrer votre mot de passe :")
        while password!=password2:
            password2=getpass.getpass(prompt="re-entrer votre mot de passe :")
        password=crypt.crypt(password)
        logger = logging.getLogger(str(args.username))
        logger.info("Mot de passe généré")

        with open("/etc/password","a") as file :
            add=[str(args.username),str(password),str(assign_uid()),"DD-MM-YY",(str(args.username))]
            a=create_user_directory(str(args.username))
            while a==0:
                new_directory=input("Choisissez un autre nom de répertoire")
                a=create_user_directory(new_directory)
                add[4]=new_directory
            line = ':'.join(add)
            line = line+'\n'
            file.write(line)
            file.close()
        add_to_json_file(args.username)
        print("\n")
        for i in tqdm(range(total_iterations), desc=f"{progress_bar_color}Creation{iteration_color}", unit="iteration",
                      bar_format=f"{iteration_color}{{desc}}:{{bar}}{iteration_color} {progress_bar_color}{{percentage:3.0f}}%{reset_color}"):
            time.sleep(0.025)
        print('\n')
        print(f"{progress_bar_color}L'utilisateur {str(args.username)} a été ajouté avec succès{reset_color}")
        logger = logging.getLogger(str(args.username))
        logger.info("L'utilisateur {} a été ajouté avec succès ".format(str(args.username)))
except KeyboardInterrupt:
    print(f"{completion_color}\nEchec de création d'utilisateur{reset_color}")

