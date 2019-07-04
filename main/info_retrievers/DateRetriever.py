import datetime

from bs4 import BeautifulSoup


def find_date(article_content, pubstatus="pubmed"):
    """Finds the publication date of the article string

    :param article_content: the article's raw text as string
    :param pubstatus: can be either 'entrez', 'pubmed' or 'medline'
    :return: the pubblication date as datetime.
    """

    dates = article_content.findAll("PubMedPubDate", {"PubStatus": pubstatus})

    if dates is None or len(dates) == 0:
        return None

    date = dates[0]

    day = int(date.Day.string)
    month = int(date.Month.string)
    year = int(date.Year.string)

    return datetime.datetime(year, month, day)
