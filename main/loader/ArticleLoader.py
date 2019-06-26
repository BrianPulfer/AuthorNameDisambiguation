import definitions

from main.model.Article import Article

from main.info_retrievers import AffiliationRetriever, AuthorsRetriever, DateRetriever, EMailRetriever,\
    KeyWordsRetriever, LocationRetriever, EntitiesRetriever

PATH_TO_ARTICLES = definitions.ROOT_DIR + '/dataset/articles/'
PATH_TO_ARTICLES_ENTITIES = definitions.ROOT_DIR + '/dataset/articles_entities/'


def load_article(pmid):
    """Given the PMID, creates and returns an article full of all its retrievable informations."""

    file = open(PATH_TO_ARTICLES+str(pmid)+'.xml', 'r')
    article_content = file.read()
    file.close()

    affiliation = AffiliationRetriever.find_affiliation(article_content)
    authors = AuthorsRetriever.find_authors(article_content)
    date = DateRetriever.find_date(article_content)
    mail = EMailRetriever.find_email(article_content)
    keywords = KeyWordsRetriever.find_keywords(article_content)
    country = LocationRetriever.find_country(article_content)
    city = LocationRetriever.find_city(article_content)
    entities = EntitiesRetriever.find_entities(pmid, dir_path=PATH_TO_ARTICLES_ENTITIES)

    return Article(pmid, authors, mail, date, affiliation, country, city, keywords, entities)
