import urllib2

from bs4 import BeautifulSoup
import pandas as pd

skeletal_url = 'http://www.citefactor.org/journal-impact-factor-list-2014_%s.html'
alphabet = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def fetch_page_per_index(title):
    index = title[0].capitalize()
    lower_case = index.lower()

    if lower_case not in alphabet:
        url = 'http://www.citefactor.org/journal-impact-factor-list-2014_0-A.html'
    elif lower_case in numbers:
        url = 'http://www.citefactor.org/journal-impact-factor-list-2014_0-A.html'
    else:
        url = skeletal_url % index

    print " .... Fetching from %s" % url

    try:
        page = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print "HTTPError({0}): {1}".format(e.errno, e.strerror)

    soup = BeautifulSoup(page, "lxml")
    tables_ = soup.find_all('table')
    data_tables = tables_[1]

    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []

    for row in data_tables.find_all('tr'):
        cells = row.findAll('td')
        # states = row.findAll('th')
        if len(cells) == 9:
            a.append(cells[0].find(text=True))
            b.append(cells[1].find(text=True))
            c.append(cells[2].find(text=True))
            d.append(cells[3].find(text=True))
            e.append(cells[4].find(text=True))
            f.append(cells[5].find(text=True))
            g.append(cells[6].find(text=True))
            h.append(cells[7].find(text=True))
            i.append(cells[8].find(text=True))

    df = pd.DataFrame(a, columns=['Index'])
    # df['Journal'] = b
    df['ISSN'] = c
    df['2013/2014'] = d
    # df['2012'] = e
    # df['2011'] = f
    # df['2010'] = g
    # df['2009'] = h
    # df['2008'] = i

    return df


def retrieve_impact_factor(issn_, df):
    issn_index = 0
    for el, issn in enumerate(df['ISSN']):
        if issn == str(issn_):
            issn_index = el

    if issn_index == str(0) or issn_index == 0:
        return "Article/ Journal not Found on cite factor"

    for el in range(len(df['ISSN'])):
        if el == issn_index:
            return df['2013/2014'][el]

    return "Article/ Journal not Found on cite factor"
