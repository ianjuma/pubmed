import urllib2

from bs4 import BeautifulSoup
import pandas as pd

wiki = "http://www.citefactor.org/journal-impact-factor-list-2014_G.html"

all_url = 'http://www.citefactor.org/journal-impact-factor-list-2014_%s.html'
a_url = 'http://www.citefactor.org/journal-impact-factor-list-2014_0-A.html'

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
urls = []


def fetch_per_index(index, url):
    page = urllib2.urlopen(wiki)

    soup = BeautifulSoup(page)
    tables_ = soup.find_all('table', {"class": ''})
    data_tables = tables_[1]
    return data_tables


def extract_data_frame(table_):
    pass


def generate_results():
    for number in range(len(alphabet)):
        urls.append(all_url % alphabet[number])

    try:
        result = urllib2.urlopen(wiki)
    except:
        print 'Error failed to fetch URL'

    return result


# results = generate_results()

page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)

tables_ = soup.find_all('table')
data_tables = tables_[1]

A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []

for row in data_tables.find_all('tr'):
    cells = row.findAll('td')
    # states = row.findAll('th')
    if len(cells) == 9:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))


df = pd.DataFrame(A, columns=['Index'])
# df['Journal'] = B
df['ISSN'] = C
df['2013/2014'] = D
# df['2012'] = E
# df['2011'] = F
# df['2010'] = G
# df['2009'] = H
# df['2008'] = I

# print df

# get article title - pass to url group
# fetch cite factor from ISSN no
# 0065-308X
# 0860-0953

# def retrieve_impact_factor(issn_):
issn_index = 0
print issn_index
for el, issn in enumerate(df['ISSN']):
    if issn == str("0860-0953"):
        issn_index = el

print "ISSN " + str(issn_index)

for el in range(len(df['ISSN'])):
    if el == issn_index:
        print df['2013/2014'][el]
