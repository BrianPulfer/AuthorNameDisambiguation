import unittest
import datetime
from main.model.Author import Author
from main.model.Affiliation import Affiliation
from main.model.Article import Article


class TestArticle(unittest.TestCase):
    def test_class(self):
        """Tests the Article class in the model package."""
        country, city,  = "USA", "New York"
        article = Article(country=country, city=city)

        self.assertFalse(article.has_all_data())

        article.set_e_mail("notReal@test.com")
        article.set_date(datetime.datetime(2003, 5, 24))
        article.set_affiliation(Affiliation(infos="Test infos"))
        article.set_authors([Author("Kennedy", "Becker", "K.B.")])
        article.set_key_words(['Asthma', 'Anxiety'])
        article.set_entities(['Test entity 1', 'Test entity 2'])

        self.assertTrue(article.has_all_data())


if __name__ == '__main__':
    unittest.main()
