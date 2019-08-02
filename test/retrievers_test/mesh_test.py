import unittest

from bs4 import BeautifulSoup

from main.retrievers import mesh
from main.eutilities import e_utilities


class TestMeshTermsRetriever(unittest.TestCase):
    def test_find_keywords(self):
        """Tests that the 'find_mesh_terms' finds the mesh terms of a real article.'"""

        # Fetching article
        pmid = "20113659"
        query = e_utilities.Query(any_terms=[pmid])
        article = e_utilities.fetch(e_utilities.DATABASES.PubMed, query, 'xml')

        soup = BeautifulSoup(article.content.decode('utf-8'), "xml")

        # Extracting mesh terms from article's content
        keys = mesh.find_mesh_terms(soup)

        # Checking mesh terms content
        self.assertEqual(13, len(keys))
        self.assertEqual('Airway Resistance', keys[0])


if __name__ == '__main__':
    unittest.main()