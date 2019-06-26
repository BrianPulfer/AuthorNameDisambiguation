import datetime

from main.model.Affiliation import Affiliation


class Article:
    """Class that represents an article.
    Ideally contains all the data needed to be compared to another article."""

    def __init__(self, PMID: int = None, authors: list = list(), e_mail: str = None, date: datetime = None,
                 affiliation: Affiliation = None, country: str = None, city: str = None, key_words: list = list(),
                 entities: list = None, raw_text: str = None):
        self.PMID = PMID
        self.authors = authors
        self.e_mail = e_mail
        self.date = date
        self.affiliation = affiliation
        self.country = country
        self.city = city
        self.key_words = key_words
        self.entities = entities
        self.raw_text = raw_text

    # Getters and Setters
    def get_PMID(self):
        return self.PMID

    def set_PMID(self, pmid):
        self.PMID = pmid

    def get_authors(self):
        return self.authors

    def set_authors(self, authors):
        self.authors = authors

    def add_author(self, author):
        self.authors.append(author)

    def get_e_mail(self):
        return self.e_mail

    def set_e_mail(self, e_mail):
        self.e_mail = e_mail

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_key_words(self):
        return self.key_words

    def set_key_words(self, key_words):
        self.key_words = key_words

    def get_raw_text(self):
        return self.raw_text

    def set_raw_text(self, raw_text):
        self.raw_text = raw_text

    def get_country(self):
        return self.country

    def set_country(self, county):
        self.country = county

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_affiliation(self):
        return self.affiliation

    def set_affiliation(self, affiliation):
        self.affiliation = affiliation

    def get_entities(self):
        return self.entities

    def set_entities(self, entities):
        self.entities = entities

    def has_all_data(self):
        return len(self.authors) > 0 and \
                self.e_mail is not "" and self.e_mail is not None and \
                self.date is not None and \
                len(self.key_words) > 0 and \
                self.country is not "" and self.country is not None and \
                self.city is not "" and self.city is not None and \
                self.affiliation.get_infos() is not "" and self.affiliation.get_infos() is not None and \
                self.entities is not None
