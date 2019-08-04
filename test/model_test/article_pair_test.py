import unittest
import datetime

from main.model.author import Author
from main.model.affiliation import Affiliation
from main.model.article import Article
from main.model.article_pair import ArticlePair


class TestArticlePair(unittest.TestCase):
    def test_Levenshtein_scores(self):
        """Tests that all the scores which uses the levensthein distance (email, affiliation) work properly"""

        author1 = Author('lastname', 'firstname', 'L.F.')
        author2 = Author('test', 'name', 'T.N.')

        email1 = 'samemail@test.com'
        email2 = 'somemail@best.com'

        article1 = Article(e_mail=email1, main_author=author1)
        article2 = Article(e_mail=email1, main_author=author1)
        article3 = Article(e_mail=email2, main_author=author2)

        ap1 = ArticlePair(article1, article2)
        ap2 = ArticlePair(article1, article3)

        # Testing e-mail score
        self.assertEqual(1, ap1.get_email_score())
        self.assertEqual(0, ap2.get_email_score())

        # Testing affiliation score
        self.assertEqual(0, ap1.get_firstname_score())
        self.assertEqual(5, ap2.get_firstname_score())

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
        self.assertEqual(1, real_pair1.get_date_score())
        self.assertEqual(1, real_pair2.get_date_score())

    def test_location_score(self):
        """Tests that the score is 1 for articles of the same country, 0 otherwise"""

        c1 = 'France'
        c2 = '  france '
        c3 = 'Greece'

        a1 = Article(loc_list=[c1])
        a2 = Article(loc_list=[c2])
        a3 = Article(loc_list=[c3])

        ap1 = ArticlePair(a1, a2)
        ap2 = ArticlePair(a1, a3)

        self.assertEqual(1, ap1.get_location_score())     # Countries are equal
        self.assertEqual(0, ap2.get_location_score())     # Countries are different

    def test_authors_score(self):
        """Tests that the authors scores are correctly retrieved, checking that lower/upper-case letters are ignored."""
        author1 = Author("Testing", "Test", "T.T.")
        author2 = Author("Resting", "Rest", "R.R.")
        author3 = Author("John", "Doe", "J.D.")

        article1 = Article(main_author=author1, authors=[author1, author2, author3])
        article2 = Article(main_author=author1, authors=[author1, author2, author3])
        article3 = Article(main_author=author1, authors=[author1, author2])

        self.assertEqual(2, ArticlePair(article1, article2).get_coauthors_score())
        self.assertEqual(1, ArticlePair(article1, article3).get_coauthors_score())

    def test_mesh_score(self):
        """Tests that the number of shared keywords by the articles are correctly
        retrieved by ignoring lower/upper-case letters"""

        article1 = Article(mesh_terms=['test', 'Testing', 'unittest'])
        article2 = Article(mesh_terms=['test', 'TESTING'])
        article3 = Article(mesh_terms=[])

        self.assertEqual(2, ArticlePair(article1, article2).get_mesh_score())
        self.assertEqual(0, ArticlePair(article1, article3).get_mesh_score())

    def test_jdst_score(self):
        """Tests that the number of shared Journal Descriptors and Semantic Types are correctly computed"""
        article1 = Article(jds=['A', 'B', 'C'], sts=['X', 'Y', 'Z'])
        article2 = Article(jds=['A', 'C'], sts=['Z'])

        self.assertEqual(3, ArticlePair(article1, article2).get_jdst_score())

    def test_language_score(self):
        """Tests that the language comparison is correctly implemented"""

        article1 = Article(language='eng')
        article2 = Article(language='eng')
        article3 = Article(language='ENG')

        self.assertEqual(1, ArticlePair(article1, article2).get_language_score())
        self.assertEqual(1, ArticlePair(article1, article3).get_language_score())

    def test_initials_score(self):
        """Tests that the binary information (authors initials match) is correctly detected"""
        author1 = Author("Lastname", "Forename", "L.F.")
        author2 = Author("Lastname", "Test", "L.T.")

        article1 = Article(main_author=author1)
        article2 = Article(main_author=author2)
        article3 = Article()

        self.assertEqual(1, ArticlePair(article1, article1).get_initials_score())
        self.assertEqual(0, ArticlePair(article1, article2).get_initials_score())
        self.assertEqual(-1, ArticlePair(article1, article3).get_initials_score())

    def test_ambiguity_score(self):
        """Tests that the ambiguity score is correctly averaged"""

        article1 = Article(ambiguity=0.10)
        article2 = Article(ambiguity=0.20)

        ambiguity = ArticlePair(article1, article2).get_ambiguity_score()
        error = ambiguity - 0.15

        # Approximation error is 2.77e-17
        self.assertTrue(float(0.0000000000000001) > error)

    def test_lnlength_score(self):
        """Tests that the articles lastnames lengths are correctly averaged"""

        author1 = Author('Pulfer', 'Brian', 'P.B.')
        author2 = Author('Doe', 'John', 'DJ')
        author3 = Author('Case', 'Test', 'C.T.')

        article1 = Article(authors=[author1, author2])
        article2 = Article(authors=[author1, author3])
        article3 = Article(authors=[author2, author3])

        ap1 = ArticlePair(article1, article2)
        ap2 = ArticlePair(article1, article3)
        ap3 = ArticlePair(article2, article3)

        self.assertEqual(6, ap1.get_lnlength_score())
        self.assertEqual(4.5, ap2.get_lnlength_score())
        self.assertEqual(4.5, ap3.get_lnlength_score())


if __name__ == '__main__':
    unittest.main()
