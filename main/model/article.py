import datetime

from main.model.affiliation import Affiliation
from main.model.author import Author


class Article:
    """Class that represents an article.
    Ideally contains all the data needed to be compared to another article."""

    def __init__(self, PMID: int = None, main_author: Author = None, language: str = None, authors: list = None,
                 e_mail: str = None, date: datetime = None, loc_list: list = None, org_list: list = None,
                 mesh_terms: list = None, entities: list = None, jds: list = None, sts: list = None,
                 ambiguity=-1, raw_text: str = None):
        self.PMID = PMID
        self.ambiguity = ambiguity
        self.main_author = main_author
        self.authors = authors
        self.language = language
        self.e_mail = e_mail
        self.date = date
        self.loc_list = loc_list
        self.org_list = org_list
        self.mesh_terms = mesh_terms
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

    def get_main_author(self):
        return self.main_author

    def set_main_author(self, main_author: Author):
        self.main_author = main_author

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

    def get_mesh_terms(self):
        return self.mesh_terms

    def set_mesh_terms(self, mesh_terms):
        self.mesh_terms = mesh_terms

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

    def get_org(self):
        return self.org_list

    def set_org(self, org_list: list):
        self.org_list = org_list

    def get_loc(self):
        return self.loc_list

    def set_loc(self, loc_list: list):
        self.loc_list = loc_list

    def get_entities(self):
        return self.entities

    def set_entities(self, entities):
        self.entities = entities

    def has_all_data(self):
        return self.authors is not None and len(self.authors) > 0 and \
               self.main_author is not None and \
               self.e_mail is not "" and self.e_mail is not None and \
               self.date is not None and \
               self.language is not None and \
               self.loc_list is not None and \
               self.org_list is not None and \
               self.ambiguity is not -1
