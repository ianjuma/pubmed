import requests

# parsing cite factor
# from lxml import etree
# import StringIO
# from lxml.html import parse


from lxml import html

"""
doc = parse('http://www.ncbi.nlm.nih.gov/pubmed/?term=cancer').getroot()

for link in doc.cssselect('div.rprt'):
    print '%s: %s' % (link.text_content(), link.get('href'))


# parser = etree.HTMLParser()
# tree = etree.parse(StringIO.StringIO(page.content), parser)
"""

page = requests.get('http://www.ncbi.nlm.nih.gov/pubmed/?term=cancer')

parsed_body = html.fromstring(page.content)
print parsed_body.xpath('//title/text()')[0].split(' - ')[0]  # search query

print parsed_body.xpath("//div[contains(@class, 'rprt')]/text()")

# print parsed_body.cssselect("div[class='header']")[0].text
