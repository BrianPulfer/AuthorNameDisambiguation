import re


def find_email(article_content):
    """Given an article content (raw text), extracts and returns the first e-mail address found.
    None string if nothing is found."""

    article_content = article_content.prettify()

    match = re.search(r'[\w\.-]+@[\w\.-]+', article_content)

    if match is not None:
        result = match.group(0)

        if result[-1] == '.':
            result = result[:len(result) - 1]

        return result
    return None
