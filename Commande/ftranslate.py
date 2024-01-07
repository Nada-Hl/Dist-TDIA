#! /usr/bin/env python3
from googletrans import Translator
import argparse
import json
import logging

log_file = "/var/logging"

with open ("/etc/actualUser") as file :
       datauser=json.load(file)
user=datauser["Utilisateur"]
logger = logging.getLogger(user)

logging.basicConfig(filename=log_file, level=logging.DEBUG, format=f'{user} | %(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def translate(source_lang, target_lang, text):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def translate_file(source_lang, target_lang, input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    translated_text = translate(source_lang, target_lang, text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

def main():
    parser = argparse.ArgumentParser(description="Trdauction d'une langue a une autre.")
    parser.add_argument("source_lang", help="Langue initiale")
    parser.add_argument("target_lang", help="Langue desiree")
    parser.add_argument("input_file", help="Fichier initiale")
    parser.add_argument("output_file", help="Fichier finale")
    args = parser.parse_args()
    translate_file(args.source_lang, args.target_lang, args.input_file, args.output_file)
    print(f"Traduction ({args.source_lang} vers {args.target_lang}) enregistre dans {args.output_file}")
    logging.info(f"Traduction de {args.input_file} de {args.source_lang} vers {args.target_lang} enregistre dans {args.output_file}")

if __name__ == "__main__":

    main()

