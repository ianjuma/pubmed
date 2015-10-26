import urllib2

wiki = "http://www.citefactor.org/journal-impact-factor-list-2014_T.html"

page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(page)

tables_ = soup.find_all('table', {"class": ''})
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
df['Journal'] = B
df['ISSN'] = C
df['2013/2014'] = D
df['2012'] = E
df['2011'] = F
df['2010'] = G
df['2009'] = H
df['2008'] = I

print df
