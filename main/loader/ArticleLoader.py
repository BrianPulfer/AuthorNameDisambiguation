import definitions

from bs4 import BeautifulSoup

from main.model.Article import Article

from main.info_retrievers import AffiliationRetriever, AuthorsRetriever, DateRetriever, EMailRetriever,\
    KeyWordsRetriever, LocationRetriever, EntitiesRetriever, LanguageRetriever

PATH_TO_ARTICLES = definitions.ROOT_DIR + '/dataset/articles/'
PATH_TO_ARTICLES_ENTITIES = definitions.ROOT_DIR + '/dataset/articles_entities/'


def load_article(pmid):
    """Given the PMID, creates and returns an article full of all its retrievable informations."""

    file = open(PATH_TO_ARTICLES+str(pmid)+'.xml', 'r')
    article_content = file.read()
    file.close()

    # Converting raw string into an object
    soup = BeautifulSoup(article_content, 'xml')

    affiliation = AffiliationRetriever.find_affiliation(soup)
    language = LanguageRetriever.find_language(soup)
    authors = AuthorsRetriever.find_authors(soup)
    date = DateRetriever.find_date(soup)
    mail = EMailRetriever.find_email(soup)
    keywords = KeyWordsRetriever.find_keywords(soup)
    country = LocationRetriever.find_country(soup)
    city = LocationRetriever.find_city(soup)
    entities = EntitiesRetriever.find_entities(pmid, dir_path=PATH_TO_ARTICLES_ENTITIES)

    return Article(PMID=pmid, authors=authors, language=language, e_mail=mail, date=date, affiliation=affiliation,
                   country=country, city=city, key_words=keywords, entities=entities)
