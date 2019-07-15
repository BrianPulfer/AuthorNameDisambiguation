import unittest
import datetime

from main.model.Author import Author
from main.model.Affiliation import Affiliation
from main.model.Article import Article
from main.model.ArticlePair import ArticlePair


class TestArticlePair(unittest.TestCase):
    def test_Levenshtein_scores(self):
        """Tests that all the scores which uses the levensthein distance (email, affiliation) work properly"""

        email1 = 'samemail@test.com'
        email2 = 'samemail@test.com'
        email3 = 'somemail@best.com'

        affiliation1_infos = "Istituto Dalle Molle sull'Intelligenza Artificiale"
        affiliation2_infos = "Istituto dalle Molle sull'intelligenza artificiale"
        affiliation3_infos = "Nursing Dept., Xuzhou Children's Hospital, Xuzhou 221006, China."

        affiliation1 = Affiliation(affiliation1_infos)
        affiliation2 = Affiliation(affiliation2_infos)
        affiliation3 = Affiliation(affiliation3_infos)

        article1 = Article(e_mail=email1, affiliation=affiliation1)
        article2 = Article(e_mail=email2, affiliation=affiliation2)
        article3 = Article(e_mail=email3, affiliation=affiliation3)

        ap1 = ArticlePair(article1, article2)
        ap2 = ArticlePair(article1, article3)

        # Testing e-mail score
        self.assertEqual(0, ap1.get_email_score())
        self.assertEqual(2, ap2.get_email_score())

        # Testing affiliation score
        self.assertEqual(0, ap1.get_affiliation_score())
        self.assertEqual(52, ap2.get_affiliation_score())

    def test_date_score(self):
        """Tests that the articles date score matches the distances of the dates (absolute value) in days"""

        d1 = datetime.datetime(2018, 1, 1)
        d2 = datetime.datetime(2019, 1, 1)

        article1 = Article(date=d1)
        article2 = Article(date=d2)

        same_pair = ArticlePair(article1, article1)
        real_pair1 = ArticlePair(article1, article2)
        real_pair2 = ArticlePair(article2, article1)

        self.assertEqual(0, same_pair.get_date_score())
        self.assertEqual(365, real_pair1.get_date_score())
        self.assertEqual(365, real_pair2.get_date_score())

    def test_country_score(self):
        """Tests that the score is 1 for articles of the same country, 0 otherwise"""

        c1 = 'France'
        c2 = '  france '
        c3 = 'Greece'

        a1 = Article(country=c1)
        a2 = Article(country=c2)
        a3 = Article(country=c3)

        ap1 = ArticlePair(a1, a2)
        ap2 = ArticlePair(a1, a3)

        self.assertEqual(1, ap1.get_county_score())     # Countries are equal
        self.assertEqual(0, ap2.get_county_score())     # Countries are different

    def test_city_score(self):
        """Tests that the score is 1 for articles of the same city, 0 otherwise"""
        c1 = 'Montreal'
        c2 = ' montreal  '
        c3 = 'Mont Real'

        a1 = Article(city=c1)
        a2 = Article(city=c2)
        a3 = Article(city=c3)

        ap1 = ArticlePair(a1, a2)
        ap2 = ArticlePair(a1, a3)

        self.assertEqual(1, ap1.get_city_score())      # Cities are equal
        self.assertEqual(0, ap2.get_city_score())      # Cities are different

    def test_authors_score(self):
        article1 = Article(authors=[Author("Testing", "Test", "T.T.")])
        article2 = Article(authors=[Author("testing", "test", "t.t.")])
        article3 = Article(authors=[Author("resting", "test", "T.T.")])

        self.assertEqual(1, ArticlePair(article1, article2).get_authors_score())
        self.assertEqual(0, ArticlePair(article1, article3).get_authors_score())

    def test_keywords_score(self):
        article1 = Article(key_words=['test', 'Testing', 'unittest'])
        article2 = Article(key_words=['test', 'TESTING'])
        article3 = Article(key_words=[])

        self.assertEqual(2, ArticlePair(article1, article2).get_keywords_score())
        self.assertEqual(0, ArticlePair(article1, article3).get_keywords_score())


if __name__ == '__main__':
    unittest.main()
