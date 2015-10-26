
"""
import requests

# parsing cite factor
# from lxml import etree
# import StringIO
# from lxml.html import parse


from lxml import html


doc = parse('http://www.ncbi.nlm.nih.gov/pubmed/?term=cancer').getroot()

for link in doc.cssselect('div.rprt'):
    print '%s: %s' % (link.text_content(), link.get('href'))


# parser = etree.HTMLParser()
# tree = etree.parse(StringIO.StringIO(page.content), parser)


page = requests.get('http://www.ncbi.nlm.nih.gov/pubmed/?term=cancer')

parsed_body = html.fromstring(page.content)
print parsed_body.xpath('//title/text()')[0].split(' - ')[0]  # search query

print parsed_body.xpath("//div[contains(@class, 'rprt')]/text()")

# print parsed_body.cssselect("div[class='header']")[0].text
"""

import urllib2

wiki = "http://www.citefactor.org/journal-impact-factor-list-2014_T.html"

page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup


soup = BeautifulSoup(page)

tables_ = soup.find_all('table', { "class": ''})

A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []

for row in soup.find_all('tr'):
	cells = row.findAll('td')
	states = row.findAll('th')
	if len(cells) == 10:
		A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
        H.append(cells[6].find(text=True))
        I.append(cells[7].find(text=True))
