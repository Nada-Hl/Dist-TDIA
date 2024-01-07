#! /usr/bin/env python3
import os
import sys
import json
import logging
import re
import subprocess
logging.basicConfig(filename="/var/logging",filemode="a",level=logging.DEBUG,format="%(name)s | %(levelname)s | %(asctime)s | %(message)s ")
try:
    with open("/etc/actualUser","r") as file:
        data=json.load(file)
        file.close()
    user=data["Utilisateur"]
    userd=data["Repertoire"]
    user_directory="/home/{}".format(userd)
    logger=logging.getLogger(user)
    def touch(filename):
        with open(filename,'w') as f:
            f.close()


    def search_file(filename) :
        for i,j,k in os.walk(user_directory):
            if filename in k:
                return 1
        return None

    def check_directory(path):
        for i,j,k in os.walk(user_directory):
            if path in str(i):
                return i
        print("Ce répertoire n'existe pas")
        logger = logging.getLogger(user)
        logger.error("Ce répertoire n'existe pas")
        return None
    def compter(filename):
        match = re.search(r'([a-zA-Z]+)\((\d+)\)', filename)
        if match:
            name=match.group(1)
            num=int(match.group(2))+1
            name="{}({})".format(name,num)
            return name
    def check_file(file):
        if search_file(file):
            file="{}(1)".format(file)
            if not search_file(file):
                print("Ce fichier existe déjà. Le fichier {} est créé".format(file))
                logger = logging.getLogger(user)
                logger.info("ajouter un fichier existant")
                return file
            while search_file(file):
                file=compter(str(file))
            print("Ce fichier existe déjà. Le fichier {} est créé".format(file))
            logger = logging.getLogger(user)
            logger.info("ajouter un fichier existant")
            return file
        print("Le {} est créé".format(file))
        logger = logging.getLogger(user)
        logger.info("créer un nouveau fichier")
        return file


    def f(filename):
        with open("/etc/usersfile", "r") as file:
            data = json.load(file)
            file.close()
        data[user].update({filename: ""})
        with open("/etc/usersfile", "w") as file:
            json.dump(data, file, indent=2)
            file.close()
    def check_system_path(path):
        banned_list = ["/", "/etc", "/var","/var","/dev","/proc","/sys","/run","/usr","/home"]
        case = len(path.split('/'))
        if case >2:
           if '/'.join(path.split('/')[0:2]) in banned_list[0:9]:
              print("désolé, vous ne pouvez pas créer de fichier ici avec cet utilisateur")
              logger = logging.getLogger(user)
              logger.error("essaye de créer un fichier dans le systéme")
              exit(0)
           if '/'.join(path.split('/')[:2])==banned_list[9]:
               if str(path.split('/')[2])!=user:
                   print(path.split('/')[2])
                   print("désolé, vous ne pouvez pas créer de fichier ici avec cet utilisateur")
                   logger = logging.getLogger(user)
                   logger.error("essaye de créer un fichier chez un autre utilisateur")
                   exit(0)
        elif case==2:
            if path in banned_list:
                print("désolé, vous ne pouvez pas créer de fichier ici")
                logger = logging.getLogger(user)
                logger.error("essaye de créer un fichier dans le systéme")
                exit(0)
        else:
            print("Error")
    i=1
    if len(sys.argv)==1:
        print("Usage : crf  nom_fichier | chemin/du/fichier ")
        exit(0)
    while i < len(sys.argv):
        path =sys.argv[i]
        if '/' in path:
            check_system_path(path)
            try:
                path[path.rfind('/') + 1]
            except IndexError:
                print("ce fichier n'existe pas")
                exit(0)
            else:
                if path[0] == '/':
                    path = path[1:]
                dir = path[:path.rfind('/')]
                filename = path[path.rfind('/') + 1:]
                if check_directory(dir):
                    dir = check_directory(dir)
                    filename = check_file(filename)
                    path = os.path.join(dir, filename)
                    touch(path)
                    f(filename)

                i=i+1
        else:
            command=subprocess.run('pwd',shell=True,capture_output=True,text=True)
            r=''.join(command.stdout.split('\n'))
            check_system_path(r)
            file=check_file(path)
            l=[r,file]
            touch('/'.join(l))
            f(file)
            i=i+1






except KeyboardInterrupt:
    logger=logging.getLogger(user)
    logger.debug("Interrompu par clé")
    exit(0)
