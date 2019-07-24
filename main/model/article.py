import datetime

from main.model.affiliation import Affiliation


class Article:
    """Class that represents an article.
    Ideally contains all the data needed to be compared to another article."""

    def __init__(self, PMID: int = None, main_author_initials: str = None, language: str = None, authors: list = list(),
                 e_mail: str = None, date: datetime = None, affiliation: Affiliation = None, country: str = None,
                 city: str = None, key_words: list = list(), entities: list = None, jds: list = None, sts: list = None,
                 ambiguity=-1, raw_text: str = None):
        self.PMID = PMID
        self.ambiguity = ambiguity
        self.main_author_initials = main_author_initials
        self.authors = authors
        self.language = language
        self.e_mail = e_mail
        self.date = date
        self.affiliation = affiliation
        self.country = country
        self.city = city
        self.key_words = key_words
        self.entities = entities
        self.jds = jds
        self.sts = sts
        self.raw_text = raw_text


    # Getters and Setters
    def get_PMID(self):
        return self.PMID

    def set_PMID(self, pmid):
        self.PMID = pmid

    def get_ambiguity(self):
        return self.ambiguity

    def set_ambiguity(self, ambiguity):
        self.ambiguity = ambiguity

    def get_main_author_initials(self):
        return self.main_author_initials

    def set_main_author_initials(self, main_author_initials):
        self.main_author_initials = main_author_initials

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language

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

    def get_jds(self):
        return self.jds

    def set_jds(self, jds: list):
        self.jds = jds

    def get_sts(self):
        return self.sts

    def set_sts(self, sts: list):
        self.sts = sts

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
                self.entities is not None and\
                self.jds is not None and\
                self.sts is not None and \
                self.ambiguity is not -1
