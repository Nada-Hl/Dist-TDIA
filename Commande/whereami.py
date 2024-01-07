#!/usr/bin/env python3

import os

def show_current_directory():
    current_directory = os.getcwd()
    print("Répertoire de travail actuel:", current_directory)
if __name__ =="__main__":
    show_current_directory()

