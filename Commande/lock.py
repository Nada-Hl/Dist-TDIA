#! /usr/bin/env python3
import logging
import json
from argparse import ArgumentParser,Namespace
import getpass
import os
with open("/etc/actualUser","r") as file:
    datauser=json.load(file)
    file.close()
user=datauser["Utilisateur"]
userd=datauser["Repertoire"]
start_point="/home/{}".format(userd)
logger=logging.getLogger(user)
logging.basicConfig(filename="/var/logging",filemode="a",level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s ")
parser=ArgumentParser(description="Verrouiller un fichier ")
parser.add_argument('-u','--unlock',help="Deverrouiller un fichier",type=str)
args,arg1=parser.parse_known_args()
try:
    def search_file(filename,star_point):
        for i,j,k in os.walk(star_point):
            if filename in k:
                return 1
        return None
    def lock(filename,password):
        with open("/etc/usersfile","r") as file:
            datafile=json.load(file)
            file.close()
        datafile[userd][filename]=password
        with open("/etc/usersfile", "w") as file:
            json.dump(datafile,file,indent=2)
            file.close()
    def check_empty_password(filename):
        with open("/etc/usersfile.json","r") as file:
            datafile=json.load(file)
            file.close()
        comp=str(datafile[userd][str(filename)])
        if comp=="":
            return 1
        return None
    def unlock(filename):
        with open("/etc/usersfile.json","r") as file:
            datafile=json.load(file)
            file.close()
        datafile[userd][filename]=""
        with open("/etc/usersfile.json", "w") as file:
            json.dump(datafile,file,indent=2)
            file.close()
    if args.unlock:
        if search_file(str(args.unlock),start_point):
            if check_empty_password(args.unlock):
                print("Ce fichier a déjà été déverrouillé")
            else:
                password = getpass.getpass(prompt="Voudrais-vous donner le mot de passe pour déverrouiller")
                with open("/etc/usersfile.json", "r") as file:
                    datafile = json.load(file)
                    file.close()
                if datafile[userd][args.unlock]== password:
                    unlock(args.unlock)
                    print("Le {} est déverrouille ".format(args.unlock))
                    logger.info("Le {} est déverrouille ".format(args.unlock))
                else:
                    print("ERREUR: Le mot de passe est incorrect")
                    logger.error("échec du déverrouillage de {} mot de passe incorrect".format(args.unlock))
        else:
            print("{} nexiste pas  ".format(str(args.unlock)))
            logger.error("{} nexiste pas ".format(str(args.unlock)))
    if arg1:
        file=arg1[0]
        if search_file(file,start_point):
            password=getpass.getpass(prompt="choisirais-vous un mot de passe")
            password1=getpass.getpass(prompt="re-entrer le mot de passe ")
            while password!=password1 :
                password1 = getpass.getpass(prompt="re-enter le mot de passe")
            lock(file,password)
            print("{} est verrouillé avec succès".format(file))
            logger.info("{}.est verrouillé avec succès".format(file))
        else:
            print("{} nexiste pas ".format(file))
            logger.error("{} n'existe pas ".format(file))


except KeyboardInterrupt:
    logger.error("interruption du clavier")
    exit(0)





