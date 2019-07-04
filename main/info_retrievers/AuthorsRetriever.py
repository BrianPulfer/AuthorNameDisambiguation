from bs4 import BeautifulSoup
from main.model.Author import Author


def find_authors(article_content):
    """Given an article's raw text, extracts all the article's authors (Last name, forename and initials)"""

    if article_content.AuthorList is None:
        return list()

    authors = list()
    authors_tags = article_content.find_all('Author')

    for data in authors_tags:
        lastname = data.LastName.string
        forename = data.ForeName.string
        initials = data.Initials.string

        authors.append(Author(lastname, forename, initials))

    return authors

