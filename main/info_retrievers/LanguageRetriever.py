def find_language(article_content):
    """Given an article's xml content as string, returns the article's language"""
    array = article_content.split('<Language')

    if len(array) > 1:
        return array[1].split('</Language>')[0].split('>')[1]
    return None
