# -*- encoding: utf-8 -*-

"""
Parses google spreadsheet

Usage: python main.py file.csv
"""

import csv
import json
import sys
import shutil

import pystache

import lysis.utils as utils
import lysis.path as path
from youranalysis import Analysis


def write_analysis(html):
    with open(path.get_path('output/index.html'), 'w') as f:
        if isinstance(html, unicode):
            html = html.encode('utf-8')
        f.write(html)


def copy_static():
    try:
        shutil.rmtree(path.get_path('output'))
    except OSError:
        # Silently fail if output directory does not exist
        pass

    shutil.copytree(path.get_path('{static}'), 'output')


def main():
    with open(sys.argv[1], 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        analysis = Analysis([row for row in spamreader])

    results = analysis.execute()
    template = open(path.get_path('{static}/index.html')).read().decode('utf-8')

    header, description = utils.split_analysis_doc(analysis.__doc__)

    html = pystache.render(template, {
        'results': results,
        'resultsJson': json.dumps(results).replace("'", "\\'"),
        'header': header,
        'description': description
    })

    copy_static()
    write_analysis(html)


if __name__ == '__main__':
    main()
