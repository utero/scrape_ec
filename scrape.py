#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter
import codecs
import sys

def parse_result(text):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text)

    for i in soup.find_all('div', 'bloq_news'):
        url = False
        tags = []
        for child in i.descendants:
            if child.name == 'a' and child.has_attr('target') and url == False:
                url = child['href']
            if child.name == 'p':
                brief = child.string.strip()
            if child.name == 'h3':
                for tag in child.contents:
                    if not tag.string.startswith("http"):
                        tags.append(tag.string.encode("utf8"))
            if child.name == 'div' and 'fecha' in child['class']:
                date = child.string
            if child.name == 'h2':
                title = child.contents[1].string
        print url
        print title.encode("utf8")
        print brief.encode("utf8")
        print tags
        print date
        print "=============="

def scrape(url_web):
    import requests

    url = url_web
    for i in range(0,60000,15):
        if i == 0:
            r = requests.get(url)
        else:
            payload = {'start': i}
            r = requests.get(url, params=payload)
        print r.url
        data = parse_result(r.text)
        sys.exit()



def main():
    description = u"""Este script que extrae información noticiosa de una
    página determinada por el usuario. Ya tu saaaa cual página"""

    parser = argparse.ArgumentParser(description=description,formatter_class=RawTextHelpFormatter)
    parser.add_argument('-u', '--url', action='store',
            metavar='http://pagweb.com',
            help=u'''Página web para scrapear.''',
            required=True, dest='url_web')

    args = parser.parse_args()
    url_web = args.url_web.strip()

    scrape(url_web)



if __name__ == "__main__":
    main()
