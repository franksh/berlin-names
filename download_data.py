"""
This script downloads all data for the project
"""

import urllib.request
from urllib.error import HTTPError
import time


def download_data():
    " Download the data "
    bezirke = [
        'charlottenburg-wilmersdorf',
        'friedrichshain-kreuzberg',
        'lichtenberg',
        'marzahn-hellersdorf',
        'mitte',
        'neukoelln',
        'pankow',
        'reinickendorf',
        'spandau',
        'steglitz-zehlendorf',
        'tempelhof-schoeneberg',
        'treptow-koepenick'
    ]

    years = [2017]
    # years = [2013, 2014, 2015, 2016]

    # Year 2012 has no date in url and filenames are upper case
    for year in years:
        if year == 2012:
            url_base = 'http://www.berlin.de/daten/liste-der-vornamen/'
            urls = [url_base + bezirk.title() + '.csv' for bezirk in bezirke]
        else:
            url_base = ('http://www.berlin.de/daten/liste-der-vornamen-'
                        + str(year) + '/')
            urls = [url_base + bezirk + '.csv' for bezirk in bezirke]
        for url, bezirk in zip(urls, bezirke):
            print(url)
            try:
                urllib.request.urlretrieve(url, 'data/raw/' + str(year) + '-' + bezirk + '.csv')
                time.sleep(2)
            except HTTPError as e:
                print(e)


if __name__ == '__main__':
    download_data()
