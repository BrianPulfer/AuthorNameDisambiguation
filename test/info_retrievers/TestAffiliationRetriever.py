import unittest

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

        # Obtaining affiliation infos
        affiliation = AffiliationRetriever.find_affiliation_infos(raw_article_content)

        # Checking that information over affiliation is correct
        self.assertEqual("Department of Respiratory Medicine, Jiangxi Children's Hospital, Nanchang 330006, China.",
                         affiliation)

    def test_find_org_type(self):
        """Tests that the organisation type is correctly retrieved from the article's xml (as string)"""

        # Fetching article
        pmid = '30882693'
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, EUtilities.Query(any_terms=[pmid]), 'xml')

        # Finding organisation type
        org_type = AffiliationRetriever.find_org_type(article.content.decode('utf-8'))

        # Checking that the organisation type of this article is just a Department (number 8)
        self.assertEqual(AffiliationRetriever.ORG_TYPES.Department.value, org_type)
        self.assertEqual(8, org_type)

    def test_find_res_type(self):
        """Tests that the correct res type is found from the article's xml (as string)"""

        # Fetching article
        pmid = '30680221'
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, EUtilities.Query(any_terms=[pmid]), 'xml')

        # Retrieving the res type
        res_type = AffiliationRetriever.find_res_type(article.content.decode('utf-8'))

        # Checking that the res type is 'Neurological' (number 9)
        self.assertEqual(9, res_type)


if __name__ == '__main__':
    unittest.main()
