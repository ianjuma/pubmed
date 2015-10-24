#!/usr/bin/env python

from Bio import Entrez


def search(query, number_of_articles_):
    Entrez.email = 'wjuma@students.usiu.ac.ke'
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
        target.write('ISSN No: ' + paper['MedlineCitation']['Article']['Journal']['ISSN'] + '\n')

        year = paper['MedlineCitation']['Article']['ArticleDate'][0]['Year']
        month = paper['MedlineCitation']['Article']['ArticleDate'][0]['Month']
        day = paper['MedlineCitation']['Article']['ArticleDate'][0]['Day']

        print 'Date Completed: ', paper['MedlineCitation']['DateCompleted']
        target.write('Date Completed: ' + str(paper['MedlineCitation']['DateCompleted']) + '\n')
        print 'Date published: %s-%s-%s \n' % (year, month, day)
        target.write('Date published: %s-%s-%s \n' % (year, month, day) + '\n')

        print paper['MedlineCitation']['Article']['ArticleTitle']
        target.write(paper['MedlineCitation']['Article']['ArticleTitle'] + '\n')
        print paper['MedlineCitation']['Article']['Abstract']['AbstractText']
        target.write(str(paper['MedlineCitation']['Article']['Abstract']['AbstractText']) + '\n')

        print "\n---------------------- AUTHORS ------------------------ \n"
        for author in paper['MedlineCitation']['Article']['AuthorList']:
            number_of_authors += 1
            print author['LastName'], author['ForeName'], "--", author['AffiliationInfo'][0]['Affiliation']
            target.write(author['LastName'] + author['ForeName'] + "--" +
                         author['AffiliationInfo'][0]['Affiliation'] + '\n')

        print "total author # - %d authors" % number_of_authors
        target.write("total author # - %d authors" % number_of_authors + '\n')
        print "---------------------------  END  ---------------------------------\n"
        target.write("---------------------------  END  ---------------------------------\n")

    # Pretty print the first paper in full to observe its structure
    # import json
    # print(json.dumps(papers[0], indent=2, separators=(',', ':')))
