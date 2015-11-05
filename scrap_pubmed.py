#!/usr/bin/env python

from Bio import Entrez
from pub_med import fetch_page_per_index, retrieve_impact_factor

email = 'wjuma@students.usiu.ac.ke'
target_encoding = "utf-8"


def search(query, number_of_articles_):
    Entrez.email = email
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax=number_of_articles_,
                            retmode='xml',
                            term=query)
    results_ = Entrez.read(handle)
    return results_


def fetch_details(id_list_):
    ids = ','.join(id_list_)
    Entrez.email = 'wjuma@students.usiu.ac.ke'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results_ = Entrez.read(handle)
    return results_


if __name__ == '__main__':
    print "Enter keyword to search for: "
    keyword = raw_input()
    print "Enter number # of articles to fetch (number): "
    number_of_articles = raw_input()
    results = search(keyword, number_of_articles)
    id_list = results['IdList']
    papers = fetch_details(id_list)
    filename = 'pubmed.txt'
    target = open(filename, 'w')

    for i, paper in enumerate(papers):
        number_of_authors = 0
        print 'Article ID: ', paper['MedlineCitation']['PMID']
        target.write('Article ID: ' + paper['MedlineCitation']['PMID'] + '\n')

        print 'ISSN No: ', paper['MedlineCitation']['Article']['Journal']['ISSN']
        target.write('ISSN No: ' + paper['MedlineCitation'][
                     'Article']['Journal']['ISSN'] + '\n')

        try:
            year = paper['MedlineCitation']['Article'][
                'ArticleDate'][0]['Year']
        except (IndexError, KeyError):
            year = None

        try:
            month = paper['MedlineCitation']['Article'][
                'ArticleDate'][0]['Month']
        except (IndexError, KeyError):
            month = None

        try:
            day = paper['MedlineCitation']['Article']['ArticleDate'][0]['Day']
        except (IndexError, KeyError):
            day = None

        # print 'Date Completed: ', paper['MedlineCitation']['DateCompleted']
        # target.write('Date Completed: ' + str(paper['MedlineCitation']['DateCompleted']) + '\n')
        print 'Date published: %s-%s-%s' % (year, month, day)
        target.write('Date published: %s-%s-%s \n' % (year, month, day) + '\n')

        # get journal impact factor
        data_frame = fetch_page_per_index(
            paper['MedlineCitation']['Article']['ArticleTitle'])
        impact_factor = retrieve_impact_factor(paper['MedlineCitation']['Article']['Journal']['ISSN'], data_frame)
        print "Impact factor - " + impact_factor + "\n"
        target.write("Impact factor - " + impact_factor + "\n")

        print paper['MedlineCitation']['Article']['ArticleTitle'] + "\n"
        target.write(paper['MedlineCitation']['Article'][
                     'ArticleTitle'].encode('utf-8') + '\n')
        print paper['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
        target.write(str(paper['MedlineCitation']['Article'][
                     'Abstract']['AbstractText']).encode('utf-8') + '\n')

        print "\n---------------------- AUTHORS ------------------------ \n"
        target.write(
            "\n---------------------- AUTHORS ------------------------ \n")
        for author in paper['MedlineCitation']['Article']['AuthorList']:
            number_of_authors += 1
            try:
                last_name = author.get('LastName', None)
            except IndexError:
                last_name = None

            try:
                fore_name = author.get('ForeName', None)
            except IndexError:
                fore_name = None

            try:
                author_affiliation = author[
                    'AffiliationInfo'][0]['Affiliation']
            except IndexError:
                author_affiliation = None

            try:
                last_name = unicode(last_name, 'latin-1')
            except UnicodeDecodeError:
                pass

            try:
                fore_name = unicode(fore_name, 'latin-1')
            except UnicodeDecodeError:
                pass

            author_affiliation = unicode(author_affiliation, 'latin-1')

            print last_name, fore_name, "--", author_affiliation
            target.write(str(last_name) + str(
                fore_name) + "->" + str(author_affiliation) + '\n')

        print "total author # - %d authors" % number_of_authors
        target.write("total author # - %d authors" % number_of_authors + '\n')
        print "---------------------------  END  ---------------------------------\n"
        target.write("---------------------------  END  ---------------------------------\n")

    # Pretty print the first paper in full to observe its structure
    # import json
    # print(json.dumps(papers[0], indent=2, separators=(',', ':')))
