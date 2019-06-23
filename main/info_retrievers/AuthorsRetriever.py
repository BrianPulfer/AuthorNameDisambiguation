from main.model.Author import Author


def find_authors(article_content):
    """Given an article's raw text, extracts all the article's authors (Last name, forename and initials)"""

    if len(article_content.split('<AuthorList')) < 2:
        return list()

    authorlist = article_content.split('<AuthorList')[1].split('</AuthorList>')[0]

    authors_data = authorlist.split('<Author')
    authors_data = authors_data[1:]

    authors = list()

    lastname, forename, initials = "", "", ""

    for data in authors_data:
        if len(data.split('<LastName>')) >= 2:
            lastname = data.split('<LastName>')[1].split('</LastName>')[0]
        if len(data.split('<ForeName>')) >= 2:
            forename = data.split('<ForeName>')[1].split('</ForeName>')[0]
        if len(data.split('<Initials>')) >= 2:
            initials = data.split('<Initials>')[1].split('</Initials>')[0]
        authors.append(Author(lastname, forename, initials))

    return authors
