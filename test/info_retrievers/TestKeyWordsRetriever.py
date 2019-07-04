import unittest

from bs4 import BeautifulSoup

from main.info_retrievers import KeyWordsRetriever
from main.eutilities import EUtilities


class TestMeshTermsRetriever(unittest.TestCase):
    def test_find_keywords(self):
        """Tests that the 'find_mesh_terms' finds the mesh terms of a real article.'"""

        # Fetching article
        pmid = "20113659"
        query = EUtilities.Query(any_terms=[pmid])
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, query, 'xml')

        soup = BeautifulSoup(article.content.decode('utf-8'), "xml")

        # Extracting mesh terms from article's content
        mesh_terms = KeyWordsRetriever.find_keywords(soup)

        # Checking mesh terms content
        self.assertEqual(13, len(mesh_terms))
        self.assertEqual('Airway Resistance', mesh_terms[0])


if __name__ == '__main__':
    unittest.main()