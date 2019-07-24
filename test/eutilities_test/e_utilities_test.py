import unittest
from main.eutilities import e_utilities


class TestQueries(unittest.TestCase):

    def test_query_class(self):
        """Tests all the Query class methods: construction, parameters settings/adding and 'to string' method"""

        # Creating an empty query and filling it afterwards
        q1 = e_utilities.Query()
        q1.add_mesh_term('mt1')
        q1.add_mesh_term('mt2')
        q1.set_pubblication_date('2011')

        # Testing that the query is correctly created for the REST request
        self.assertEqual('mt1[mesh]+AND+mt2[mesh]+AND+2011[pdat]', q1.to_string())

        # Testing that the set_mesh_terms method overwrites the older ones
        q1.set_mesh_terms(['mt3', 'mt4'])
        self.assertEqual('mt3[mesh]+AND+mt4[mesh]+AND+2011[pdat]', q1.to_string())

        # Testing query creation with all parameters
        q2 = e_utilities.Query('2009', ['cancer', 'asthma'])
        self.assertEqual('cancer[mesh]+AND+asthma[mesh]+AND+2009[pdat]', q2.to_string())

        q2.add_any_terms(20180383)
        self.assertEqual('20180383+AND+cancer[mesh]+AND+asthma[mesh]+AND+2009[pdat]', q2.to_string())

    def test_search(self):
        """Tests that a valid result is returned for a valid GET request."""
        # IMPORTANT: This tests fails when executed with all the other tests. Run the test alone to check if successful.

        q = e_utilities.Query()
        q.set_pubblication_date('2009')
        q.add_mesh_term('asthma')
        q.add_mesh_term('leukotrienes')

        result = e_utilities.search(e_utilities.DATABASES.PubMed, q)
        self.assertIsNotNone(result)

        # Checking that at least 10 articles are found
        self.assertTrue(10 < len(result.content.decode('utf-8').split('<Id>')))

    def test_fetch(self):
        """Tests that data is fetched giving only a query"""

        # Creating the query
        q = e_utilities.Query(pdat="2009", mesh=['asthma', 'leukotrienes'])

        # Fetching result from PubMed database based on the query
        result = e_utilities.fetch(e_utilities.DATABASES.PubMed, q)

        # Checking that the fetched data's content is longer that 109'000 characters (109'286 when checked manually)
        self.assertTrue(len(str(result.content)) > 109000)

        # Creating a query that only specifies the PMID
        q2 = e_utilities.Query(any_terms=["20113659"])

        # Fetching result with new query
        result2 = e_utilities.fetch(e_utilities.DATABASES.PubMed, q2)

        # Checking that the result's content only contains one publication
        self.assertEqual(2, len(str(result2.content).split('[Indexed for MEDLINE]')))

        # Checking that the result is what's excpected to be
        self.assertTrue("OBJECTIVE: Cysteinyl leukotriene (CysLTs) plays an important role in airway" in str(result2.content).split('[Indexed for MEDLINE]')[0])

    def test_fetch_articles(self):
        """Tests that article can be retrieved correctly"""

        # Creating a query that only contains the PubMed ID
        q = e_utilities.Query(any_terms=["20113659"])

        # Fetching articles
        articles = e_utilities.fetch_articles(e_utilities.DATABASES.PubMed, q)

        # Checking that fetched article is what expected (checked manually via browser)
        self.assertEqual(1, len(articles))
        self.assertTrue("Zhongguo Dang Dai Er Ke Za Zhi" in articles[0].get_raw_text())

    def test_search_by_pmid(self):
        """Tests that method 'search_with_pmid(pmid)' returns the correct data"""

        # Retrieving the response from searching an article given it's ID
        response = e_utilities.search_by_pmid(20180383)

        # Verifying that the response only contains one result
        self.assertTrue("<eSearchResult><Count>1</Count>" in str(response.content))

        # Verifying that the response's content only contains the selected response's ID
        self.assertTrue("<IdList>\n<Id>20180383</Id>\n</IdList>" in response.content.decode('utf-8'))

    def test_extract_ids(self):
        """Tests that 'extract_ids(response)' correctly returns a list of denotation IDs given a request's response"""

        # Creating the query
        q = e_utilities.Query('2009', ['cancer', 'asthma'])

        # Getting the response
        response = e_utilities.search(e_utilities.DATABASES.PubMed, q)

        # Extracting the IDs given the response's content
        ids = e_utilities.extract_ids(str(response.content))

        # Testing that the response contains all expected ids (verified manually via browser)
        expected_response = [20180383, 20128434, 20110007, 20044861, 20016028, 19995140, 19960035, 19926424, 19917947,
                             19863293, 19858390, 19851534, 19831405, 19817310, 19812684, 19808918, 19757309, 19737788,
                             19735105]

        for elem in expected_response:
            self.assertTrue(elem in ids)


if __name__ == '__main__':
    unittest.main()
