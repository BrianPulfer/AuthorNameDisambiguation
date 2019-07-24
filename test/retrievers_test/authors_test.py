import unittest

from bs4 import BeautifulSoup

from main.retrievers import authors
from main.eutilities import e_utilities


class TestAuthorsRetriever(unittest.TestCase):
    def test_find_authors(self):
        """Tests that all authors are retrieved from the article (method 'find_authors')"""

        # Extracting article
        pmid = "20113659"
        q = e_utilities.Query(any_terms=[pmid])

        article = e_utilities.fetch(e_utilities.DATABASES.PubMed, q, "xml")

        # Extracting article's authors
        auths = authors.find_authors(BeautifulSoup(article.content.decode('utf-8'), "xml"))

        self.assertEqual(3, len(auths))

        # Checking that authors data is correct
        self.assertEqual('He', auths[0].lastname)
        self.assertEqual('Mei-Juan', auths[0].forename)
        self.assertEqual('MJ', auths[0].initials)

        self.assertEqual('Chen', auths[1].lastname)
        self.assertEqual('Qiang', auths[1].forename)
        self.assertEqual('Q', auths[1].initials)

        self.assertEqual('Liu', auths[2].lastname)
        self.assertEqual('Jian-Mei', auths[2].forename)
        self.assertEqual('JM', auths[2].initials)


if __name__ == '__main__':
    unittest.main()
