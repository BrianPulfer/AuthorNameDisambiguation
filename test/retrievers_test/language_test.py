import unittest

from bs4 import BeautifulSoup

from main.retrievers import language
from main.eutilities import e_utilities


class TestLanguageRetriever(unittest.TestCase):
    def test_find_language(self):
        """Tests that the language information is correctly retrieved"""
        pmid = "12388643"
        article = e_utilities.fetch(e_utilities.DATABASES.PubMed, e_utilities.Query(any_terms=[pmid]), 'xml')

        soup = BeautifulSoup(article.content.decode('utf-8'), 'xml')

        lan = language.find_language(soup)
        self.assertEqual('eng', lan)


if __name__ == '__main__':
    unittest.main()
