def find_language(article_content):
    """Given an article's xml content as string, returns the article's language"""
    if article_content.Language is None:
        return None

    return article_content.Language.string

