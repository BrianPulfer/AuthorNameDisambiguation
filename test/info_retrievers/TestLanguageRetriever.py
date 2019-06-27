import unittest

from main.info_retrievers import LanguageRetriever
from main.eutilities import EUtilities


class TestLanguageRetriever(unittest.TestCase):
    def test_find_language(self):
        """Tests that the language information is correctly retrieved"""
        pmid = "12388643"
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, EUtilities.Query(any_terms=[pmid]), 'xml')

        language = LanguageRetriever.find_language(article.content.decode('utf-8'))
        self.assertEqual('eng', language)


if __name__ == '__main__':
    unittest.main()
