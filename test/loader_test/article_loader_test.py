import unittest
from main.loader import article_loader


class TestArticleLoader(unittest.TestCase):
    def test_load_article(self):
        """Tests that an article content is correctly retrieved"""

        # Loading files
        pmid1 = 36075
        pmid2 = '36075'

        article1 = article_loader.load_article(pmid1)
        article2 = article_loader.load_article(pmid2)

        # Checking that they are the same and that data is contained
        self.assertIsNotNone(article1)
        self.assertTrue(article1.get_e_mail() == article2.get_e_mail())
        self.assertTrue(article1.get_date() == article2.get_date())
        self.assertTrue(article1.get_jds() == article2.get_jds())
        self.assertTrue(article1.get_sts() == article2.get_sts())

        self.assertTrue(len(article1.get_authors()) == len(article2.get_authors()))

        for i in range(len(article1.get_authors())):
            self.assertTrue(article1.get_authors()[i].lastname == article2.get_authors()[i].lastname)
            self.assertTrue(article1.get_authors()[i].forename == article2.get_authors()[i].forename)
            self.assertTrue(article1.get_authors()[i].initials == article2.get_authors()[i].initials)


if __name__ == '__main__':
    unittest.main()
