import re


def find_email(article_content):
    """Given an article content (raw text), extracts and returns the first e-mail address found.
    None string if nothing is found."""

    match = re.search(r'[\w\.-]+@[\w\.-]+', article_content)

    if match is not None:
        result = match.group(0)

        if result[-1] == '.':
            result = result[:len(result) - 1]

        return result
    return None


def find_emails(article_content):
    """Given an article content (raw text), extracts and returns all the e-mail addresses found."""

    matches = re.findall(r'[\w\.-]+@[\w\.-]+', article_content)

    for i in range(len(matches)):
        if matches[i][-1] == '.':
            matches[i] = matches[i][:len(matches[i])-1]

    return matches
