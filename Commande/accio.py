#!/usr/bin/env python3

import os
import sys

def find_file(file_name, start_path="/"):
    for root, dirs, files in os.walk(start_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: accio <nom_fichier>")
        sys.exit(1)

    file_name = sys.argv[1]
    result = find_file(file_name)

    if result:
        print(f"Fichier '{file_name}' se trouve dans le chemin : {result}")
    else:
        print(f"Fichier '{file_name}' ne se trouve pas.")

if __name__ == "__main__":
    main()

