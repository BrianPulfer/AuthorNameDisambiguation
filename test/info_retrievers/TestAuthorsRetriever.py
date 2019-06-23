import unittest

from main.info_retrievers import AuthorsRetriever
from main.eutilities import EUtilities


class TestAuthorsRetriever(unittest.TestCase):
    def test_find_authors(self):
        """Tests that all authors are retrieved from the article (method 'find_authors')"""

        # Extracting article
        pmid = "20113659"
        q = EUtilities.Query(any_terms=[pmid])

        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, q, "xml")

        # Extracting article's authors
        authors = AuthorsRetriever.find_authors(article.content.decode('utf-8'))

        self.assertEqual(3, len(authors))

        # Checking that authors data is correct
        self.assertEqual('He', authors[0].lastname)
        self.assertEqual('Mei-Juan', authors[0].forename)
        self.assertEqual('MJ', authors[0].initials)

        self.assertEqual('Chen', authors[1].lastname)
        self.assertEqual('Qiang', authors[1].forename)
        self.assertEqual('Q', authors[1].initials)

        self.assertEqual('Liu', authors[2].lastname)
        self.assertEqual('Jian-Mei', authors[2].forename)
        self.assertEqual('JM', authors[2].initials)


if __name__ == '__main__':
    unittest.main()
