import unittest
from main.loader import ArticleLoader


class TestArticleLoader(unittest.TestCase):
    def test_load_article(self):
        """Tests that an article content is correctly retrieved"""

        # Loading files
        pmid1 = 36075
        pmid2 = '36075'

        article1 = ArticleLoader.load_article(pmid1)
        article2 = ArticleLoader.load_article(pmid2)

        # Checking that they are the same and that data is contained
        self.assertEqual(article1, article2)
        self.assertIsNotNone(article1)
        self.assertTrue('<PubmedArticle>' in article1)


if __name__ == '__main__':
    unittest.main()
