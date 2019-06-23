import datetime


def find_date(article_content, pubstatus="pubmed"):
    """Finds the publication date of the article string

    :param article_content: the article's raw text as string
    :param pubstatus: can be either 'entrez', 'pubmed' or 'medline'
    :return: the pubblication date as datetime.
    """

    if len(article_content.split('<PubMedPubDate PubStatus="'+pubstatus+'">')) < 2:
        return None

    pubmeddate =\
        article_content.split('<PubMedPubDate PubStatus="'+pubstatus+'">')[1].split("</PubMedPubDate>")[0]

    day = int(pubmeddate.split('<Day>')[1].split('</Day>')[0])
    month = int(pubmeddate.split('<Month>')[1].split('</Month>')[0])
    year = int(pubmeddate.split('<Year>')[1].split('</Year>')[0])

    return datetime.datetime(year, month, day)
