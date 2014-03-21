#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter
import codecs
import sys
from bs4 import BeautifulSoup
import re
import json
import requests
import sys




def parse_result(text):
    soup = BeautifulSoup(text)

    for i in soup.find_all('div', 'txt-nota'):
        text = re.sub('<[^<]+?>', '', str(i)).strip()
        return text

def download_note(filename):
    with codecs.open(filename, "r", "utf8") as data:
        lines = data.readlines()
        for line in lines:
            line = json.loads(line)
            if 'url' in line and line['url'] != False:
                url = line['url']
                r = requests.get(url)
                data = parse_result(r.text)
                line['text'] = data
                print line


def main():
    description = u"""Este script que extrae el cuerpo de la noticia a partir
    del link contenido en un objeto JSON"""

    parser = argparse.ArgumentParser(description=description,formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--filename', action='store',
            metavar='output.txt',
            help=u'''Archivo conteniendo objetos JSON.''',
            required=True, dest='filename')

    args = parser.parse_args()
    filename = args.filename.strip()

    download_note(filename)



if __name__ == "__main__":
    main()
