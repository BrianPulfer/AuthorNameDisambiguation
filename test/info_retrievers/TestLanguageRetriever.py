import unittest

from bs4 import BeautifulSoup

from main.info_retrievers import LanguageRetriever
from main.eutilities import EUtilities


class TestLanguageRetriever(unittest.TestCase):
    def test_find_language(self):
        """Tests that the language information is correctly retrieved"""
        pmid = "12388643"
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, EUtilities.Query(any_terms=[pmid]), 'xml')

        soup = BeautifulSoup(article.content.decode('utf-8'), 'xml')

        language = LanguageRetriever.find_language(soup)
        self.assertEqual('eng', language)


if __name__ == '__main__':
    unittest.main()
