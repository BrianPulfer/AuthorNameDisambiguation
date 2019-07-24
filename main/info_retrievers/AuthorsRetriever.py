from main.model.Author import Author


def find_authors(article_content):
    """Given an article's raw text, extracts all the article's authors (Last name, forename and initials)"""

    if article_content.AuthorList is None:
        return list()

    authors = list()
    authors_tags = article_content.find_all('Author')

    lastname, forename, initials = "", "", ""

    for data in authors_tags:
        if data.LastName:
            lastname = data.LastName.string

        if data.ForeName:
            forename = data.ForeName.string

        if data.Initials:
            initials = data.Initials.string

        authors.append(Author(lastname, forename, initials))

    return authors

