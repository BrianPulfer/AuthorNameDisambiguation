import unittest
import datetime

from bs4 import BeautifulSoup

from main.info_retrievers import DateRetriever
from main.eutilities import EUtilities


class TestDateRetriever(unittest.TestCase):
    def test_find_date(self):
        """Tests that the date is correctly retrieved in method 'find_date()'"""

        # Fetching an article
        pmid = "20113659"
        query = EUtilities.Query(any_terms=[pmid])

        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, query, rettype="xml")
        soup = BeautifulSoup(article.content.decode('utf-8'), "xml")

        # Getting 2/3 dates from the article
        pubmed_date = DateRetriever.find_date(soup)
        medline_date = DateRetriever.find_date(soup, pubstatus='medline')

        # Checking that the retrieved dates are correct
        self.assertEqual(datetime.datetime(2010, 2, 2), pubmed_date)
        self.assertEqual(datetime.datetime(2010, 3, 3), medline_date)


if __name__ == '__main__':
    unittest.main()
