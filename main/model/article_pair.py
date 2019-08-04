import copy
import Levenshtein
import math

from main.model.article import Article


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
        return [False, True, False, False, False, True, True, True, False, False, True, False,
                False, False, False]

    def scores(self):
        """Returns all the similarity scores between the pair of articles"""
        return [self.get_firstname_score(), self.get_initials_score(), self.get_coauthors_score(),
                self.get_mesh_score(), self.get_jdst_score(), self.get_city_score(), self.get_county_score(),
                self.get_language_score(), self.get_date_score(), self.get_affiliation_score(), self.get_email_score(),
                self.get_org_type_descr_score(),
                self.get_entities_score(), self.get_ambiguity_score(), self.get_lnlength_score()]

    def get_firstname_score(self):
        """Checks if the articles main authors first names matches"""
        if self.article1.get_main_author() is not None and self.article2.get_main_author() is not None:
            if self.article1.get_main_author().get_forename() is not None and \
                    self.article2.get_main_author().get_forename() is not None:
                return Levenshtein.distance(self.article1.get_main_author().get_forename(),
                                            self.article2.get_main_author().get_forename())
        return -1

    def get_initials_score(self):
        """Returns 1 if the articles share the same main author's initials, 0 otherwise"""
        if self.article1.get_main_author() is None or\
                self.article2.get_main_author() is None:
            return -1

        initials1 = self.article1.get_main_author().get_initials()
        initials2 = self.article2.get_main_author().get_initials()

        if isinstance(initials1, str) and isinstance(initials2, str):
            initials1 = self.article1.get_main_author().get_initials().lower().strip()
            initials2 = self.article2.get_main_author().get_initials().lower().strip()

            if initials1 == initials2:
                return 1
            return 0
        return -1

    def get_coauthors_score(self):
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
            # Main authors are not considered
            if not author1.lastname == self.article1.get_main_author().lastname:
                for author2 in a2:
                    if not author2.lastname == self.article2.get_main_author().lastname:
                        if author1.lastname == author2.lastname and author1.forename == author2.forename \
                                and author1.initials == author2.initials:
                            same_authors = same_authors + 1
        return same_authors

    def get_mesh_score(self):
        """Returns the number of matching keywords between the articles"""
        mt1 = copy.copy(self.article1.get_mesh_terms())
        mt2 = copy.copy(self.article2.get_mesh_terms())

        # Normalizing keywords
        for i in range(len(mt1)):
            mt1[i] = mt1[i].lower().strip()

        for i in range(len(mt2)):
            mt2[i] = mt2[i].lower().strip()

        all_ms = list()
        all_ms.extend(mt1)
        all_ms.extend(mt2)

        ms_set = set(all_ms)

        return len(all_ms) - len(ms_set)

    def get_jdst_score(self):
        """Counts the number of Journal Descriptors and Semantic Types shared by the articles"""
        jds1, sts1 = self.article1.get_jds(), self.article1.get_sts()
        jds2, sts2 = self.article2.get_jds(), self.article2.get_sts()

        if jds1 is None or sts1 is None or jds2 is None or sts2 is None:
            return -1

        retval = 0

        # Counting shared Journal Descriptors
        for jd1 in jds1:
            for jd2 in jds2:
                if jd1 == jd2:
                    retval = retval + 1

        # Counting shared Semantic Types
        for st1 in sts1:
            for st2 in sts2:
                if st1 == st2:
                    retval = retval + 1

        return retval

    def get_city_score(self):
        """Compares the two articles cities and returns 1 if they are equal, 0 otherwise."""
        city1 = self.article1.get_city()
        city2 = self.article2.get_city()

        if city1 is None or city2 is None:
            return -1

        if city1.lower().strip() == city2.lower().strip():
            return 1
        return 0

    def get_county_score(self):
        """Compares the two articles countries and returns 1 if they are equal, 0 otherwise."""
        country1 = self.article1.get_country()
        country2 = self.article2.get_country()

        if country1 is None or country2 is None:
            return -1

        if country1.lower().strip() == country2.lower().strip():
            return 1
        return 0

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

    def get_date_score(self):
        """Returns the distance (in years, absolute value) between the two articles dates"""
        if self.article1.get_date() is None or self.article2.get_date() is None:
            return -1

        delta = self.article1.get_date() - self.article2.get_date()
        years = int(delta.days / 365)

        if years < 0:
            return -1*years
        return years

    def get_affiliation_score(self):
        """Returns the Levenshtein distance between the two articles affiliation informations"""
        infos1 = self.article1.get_affiliation().get_infos()
        infos2 = self.article2.get_affiliation().get_infos()

        if infos1 is None or infos2 is None:
            return -1
        return Levenshtein.distance(infos1.lower(), infos2.lower())

    def get_email_score(self):
        """Returns the Levenshtein distance between the articles e-mail addresses"""
        mail1 = self.article1.get_e_mail()
        mail2 = self.article2.get_e_mail()

        if mail1 is not None and mail2 is not None:
            if mail1 == mail2:
                return 1
            return 0
        return -1

    def get_org_type_descr_score(self):
        """Returns the cosine between the articles vectors [org_desc, org_type]"""
        t1, d1 = self.article1.get_affiliation().get_type(), self.article1.get_affiliation().get_descriptor()
        t2, d2 = self.article2.get_affiliation().get_type(), self.article2.get_affiliation().get_descriptor()

        if t1 and t2 and d1 and d2:
            num = (d1.value * d2.value) + (t1.value * t2.value)
            denum = math.sqrt((d1.value**2 + t1.value**2) + (d2.value**2 + t2.value**2))
            return num/denum
        return -1

    """                                 UNUSED METHODS IN BASELINE VERSION                                           """
    def get_entities_score(self):
        """Returns the number of matching entities between the articles"""
        all_entities = list()
        all_entities.extend(self.article1.get_entities())
        all_entities.extend(self.article2.get_entities())

        entities_set = set(all_entities)

        return len(all_entities) - len(entities_set)

    def get_ambiguity_score(self):
        """Returns an average the two article's ambiguity"""
        return (self.article1.get_ambiguity() + self.article2.get_ambiguity()) / 2

    def get_lnlength_score(self):
        """Returns an average between the authors lastnames length"""

        if self.article1.authors and self.article2.authors:
            return (len(self.article1.authors[0].lastname) + len(self.article2.authors[0].lastname)) / 2
        return -1

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
