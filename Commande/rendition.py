#! /usr/bin/env python3
from googletrans import Translator
import argparse
import json
import logging

log_file = "/var/logging"

with open ("/etc/actualUser","r") as file :
       datauser=json.load(file)
user=datauser["Utilisateur"]
logger = logging.getLogger(user)

logging.basicConfig(filename=log_file, level=logging.DEBUG, format=f'{user} | %(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def translate(source_lang, target_lang, text):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def main():
    parser = argparse.ArgumentParser(description="Traduction d'une langue a une autre.")
    parser.add_argument("source_lang", help="Langue initiale")
    parser.add_argument("target_lang", help="Langue desiree")
    parser.add_argument("text", help="Le texte a traduire")
    args = parser.parse_args()
    translated_text = translate(args.source_lang, args.target_lang, args.text)
    print(f"Traduction ({args.source_lang} vers {args.target_lang}): {translated_text}")
    logging.info(f"Traduction ({args.source_lang} vers {args.target_lang}): {translated_text}")

if __name__ == "__main__":

    main()


