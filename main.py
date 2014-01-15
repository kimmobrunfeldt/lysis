# -*- encoding: utf-8 -*-

"""
Parses google spreadsheet

Usage: python analyze_study.py file.csv
"""

import csv
import cgi
import sys
import json


class Analytics(object):
    def __init__(self):
        pass

    def

def find_


def parse_row(row):
    find


def main():
    results = []


    with open(sys.argv[1], 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            results.append(parse_row(row))

    print results


if __name__ == '__main__':
    main()
