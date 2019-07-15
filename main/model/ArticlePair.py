import copy
import Levenshtein
import random

from main.model.Article import Article


class ArticlePair:
    """Represents a pair of articles. Offers method to retrieve similarity between two articles.
    A similarity method which returns -1 as score means that informations about that field are missing."""

    def __init__(self, article1: Article, article2: Article, label: int = None):
        """Initialization by giving the pair of articles"""
        self.article1 = article1
        self.article2 = article2
        self.label = label

    @staticmethod
    def binary_scores():
        """Static method which returns a list of true's and false's.
        The list indicates if the scores in a particular column are binary or not."""
        return [False, False, False, False, True, True, False, False, False, False, False]

    def scores(self):
        """Returns all the similarity scores between the pair of articles"""
        return [self.get_authors_score(), self.get_email_score(), self.get_date_score(), self.get_keywords_score(),
                self.get_county_score(), self.get_city_score(), self.get_affiliation_score(), self.get_entities_score(),
                self.get_jds_score(), self.get_sts_score(), self.get_ambiguity_score()]

    def get_email_score(self):
        """Returns the Levenshtein distance between the articles e-mail addresses"""
        mail1 = self.article1.get_e_mail()
        mail2 = self.article2.get_e_mail()

        if mail1 is None or mail2 is None:
            return -1

        return Levenshtein.distance(mail1.lower(), mail2.lower())

    def get_authors_score(self):
        """Returns the number of matching authors (forename, lastname, initials without considering the lower/upper
        case and blank spaces) in the article"""
        a1 = copy.copy(self.article1.get_authors())
        a2 = copy.copy(self.article2.get_authors())

        for i in range(len(a1)):
            a1[i].lastname = a1[i].lastname.lower().strip()
            a1[i].forename = a1[i].forename.lower().strip()
            a1[i].initials = a1[i].initials.lower().strip()

        for i in range(len(a2)):
            a2[i].lastname = a2[i].lastname.lower().strip()
            a2[i].forename = a2[i].forename.lower().strip()
            a2[i].initials = a2[i].initials.lower().strip()

        same_authors = 0

        for author1 in a1:
            for author2 in a2:
                if author1.lastname == author2.lastname and author1.forename == author2.forename \
                        and author1.initials == author2.initials:
                    same_authors = same_authors + 1

        return same_authors

    def get_date_score(self):
        """Returns the distance (in days, absolute value) between the two articles dates"""
        if self.article1.get_date() is None or self.article2.get_date() is None:
            return -1

        delta = self.article1.get_date() - self.article2.get_date()
        days = delta.days

        if days < 0:
            return -1*days
        return days

    def get_keywords_score(self):
        """Returns the number of matching keywords between the articles"""
        kw1 = copy.copy(self.article1.get_key_words())
        kw2 = copy.copy(self.article2.get_key_words())

        # Normalizing keywords
        for i in range(len(kw1)):
            kw1[i] = kw1[i].lower().strip()

        for i in range(len(kw2)):
            kw2[i] = kw2[i].lower().strip()

        all_kws = list()
        all_kws.extend(kw1)
        all_kws.extend(kw2)

        kws_set = set(all_kws)

        return len(all_kws) - len(kws_set)

    def get_county_score(self):
        """Compares the two articles countries and returns 1 if they are equal, 0 otherwise."""
        country1 = self.article1.get_country()
        country2 = self.article2.get_country()

        if country1 is None or country2 is None:
            return -1

        if country1.lower().strip() == country2.lower().strip():
            return 1
        return 0

    def get_city_score(self):
        """Compares the two articles cities and returns 1 if they are equal, 0 otherwise."""
        city1 = self.article1.get_city()
        city2 = self.article2.get_city()

        if city1 is None or city2 is None:
            return -1

        if city1.lower().strip() == city2.lower().strip():
            return 1
        return 0

    def get_affiliation_score(self):
        """Returns the Levenshtein distance between the two articles affiliation informations"""
        infos1 = self.article1.get_affiliation().get_infos()
        infos2 = self.article2.get_affiliation().get_infos()

        if infos1 is None or infos2 is None:
            return -1
        return Levenshtein.distance(infos1.lower(), infos2.lower())

    def get_entities_score(self):
        """Returns the number of matching entities between the articles"""
        all_entities = list()
        all_entities.extend(self.article1.get_entities())
        all_entities.extend(self.article2.get_entities())

        entities_set = set(all_entities)

        return len(all_entities) - len(entities_set)

    def get_language_score(self):
        """Returns 1 if the articles share the same language, 0 otherwise"""

        # NOTE: This score isn't used because to date (07.2019) all the article pairs in the training set always share
        # the same language.

        language1 = self.article1.get_language()
        language2 = self.article2.get_language()

        if language1 is not None and language2 is not None:
            language1 = self.article1.get_language().lower().strip()
            language2 = self.article1.get_language().lower().strip()

            if language1 == language2:
                return 1
            return 0
        return -1

    def get_initials_score(self):
        """Returns 1 if the articles share the same main author's initials, 0 otherwise"""
        initials1 = self.article1.get_main_author_initials()
        initials2 = self.article2.get_main_author_initials()

        if isinstance(initials1, str) and isinstance(initials2, str):
            initials1 = self.article1.get_main_author_initials().lower().strip()
            initials2 = self.article1.get_main_author_initials().lower().strip()

            if initials1 == initials2:
                return 1
            return 0
        return -1

    def get_jds_score(self):
        """Returns the number of matching Journal Descriptors between the articles"""
        jds1 = self.article1.get_jds()
        jds2 = self.article2.get_jds()

        if jds1 is None or jds2 is None:
            return -1

        matches = 0

        for jd1 in jds1:
            for jd2 in jds2:
                if jd1 == jd2:
                    matches = matches + 1
        return matches

    def get_sts_score(self):
        """Returns the number of matching Semantic Types between the articles"""
        sts1 = self.article1.get_sts()
        sts2 = self.article2.get_sts()

        if sts1 is None or sts2 is None:
            return -1

        matches = 0

        for st1 in sts1:
            for st2 in sts2:
                if st1 == st2:
                    matches = matches + 1
        return matches

    def get_ambiguity_score(self):
        """Returns an average the two article's ambiguity"""
        return (self.article1.get_ambiguity() + self.article2.get_ambiguity()) / 2

    # Getters
    def get_article_1(self):
        return self.article1

    def get_article_2(self):
        return self.article2

    def get_label(self):
        return self.label

    def has_all_data(self):
        if self.article1.has_all_data() and self.article2.has_all_data():
            return True
        return False
