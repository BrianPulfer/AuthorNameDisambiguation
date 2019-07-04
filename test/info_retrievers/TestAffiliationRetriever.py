import unittest

from bs4 import BeautifulSoup

from main.info_retrievers import AffiliationRetriever
from main.eutilities import EUtilities


class TestAffiliationRetriever(unittest.TestCase):
    def test_find_affiliation_name(self):
        """Tests that the affiliation name is retrieved correctly in method 'find_affiliation_name()'"""

        # Fetching article and storing raw_content as string
        pmid = '20113659'
        query = EUtilities.Query(any_terms=[pmid])

        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, query, 'xml')
        raw_article_content = article.content.decode('utf-8')

        soup = BeautifulSoup(raw_article_content, "xml")

        # Obtaining affiliation infos
        affiliation = AffiliationRetriever.find_affiliation_infos(soup)

        # Checking that information over affiliation is correct
        self.assertEqual("Department of Respiratory Medicine, Jiangxi Children's Hospital, Nanchang 330006, China.",
                         affiliation)


if __name__ == '__main__':
    unittest.main()
