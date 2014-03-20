#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter
import codecs
import sys


def scrape(url_web):
    import requests

    url = url_web
    for i in range(0,60000,15):
        print i



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
