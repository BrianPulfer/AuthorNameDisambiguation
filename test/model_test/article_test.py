import unittest
import datetime
from main.model.author import Author
from main.model.affiliation import Affiliation
from main.model.article import Article


class TestArticle(unittest.TestCase):
    def test_class(self):
        """Tests the Article class in the model_test package."""
        country, city,  = "USA", "New York"
        article = Article(loc_list=[city, country])

        self.assertFalse(article.has_all_data())

        article.set_e_mail("notReal@test.com")
        article.set_date(datetime.datetime(2003, 5, 24))
        article.set_main_author(Author("Test", "Author", "T.A."))
        article.set_authors([Author("Kennedy", "Becker", "K.B.")])
        article.set_mesh_terms(['Asthma', 'Anxiety'])
        article.set_entities(['Test entity 1', 'Test entity 2'])
        article.set_jds(['jd1', 'jd2'])
        article.set_sts(['st1', 'st2', 'st3'])
        article.set_ambiguity(0.1)
        article.set_language('eng')
        article.set_loc(['Berlin', 'Germany'])
        article.set_org(['University', 'of', 'Berlin'])
        article.set_vector([3, 5, 2])

        self.assertTrue(article.has_all_data())


if __name__ == '__main__':
    unittest.main()
