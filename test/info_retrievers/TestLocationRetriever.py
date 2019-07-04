import unittest

from bs4 import BeautifulSoup

from main.eutilities import EUtilities
from main.info_retrievers import LocationRetriever


class TestLocationRetriever(unittest.TestCase):

    def test_find_country(self):
        """Tests that the country name is retrieved correctly from an article."""

        pmid = '31161595'
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, EUtilities.Query(any_terms=[pmid]), 'xml')

        country = LocationRetriever.find_country(BeautifulSoup(article.content.decode('utf-8'), 'xml'))

        self.assertEqual('India', country)

    def test_find_city(self):
        """Tests that the city name is retrieved correctly from an article"""

        pmid = '20528593'
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, EUtilities.Query(any_terms=[pmid]), 'xml')

        city = LocationRetriever.find_city(BeautifulSoup(article.content.decode('utf-8'), 'xml'))

        self.assertEqual('Osaka', city)

    def test_find_location_infos(self):
        """Tests that the location infos are correctly retrieved"""
        pmid = '2673539'
        article = EUtilities.fetch(EUtilities.DATABASES.PubMed, EUtilities.Query(any_terms=[pmid]), 'xml')
        location_infos = LocationRetriever.get_affiliation_infos(BeautifulSoup(article.content.decode('utf-8'), 'xml'))

        self.assertEqual('Department of Pediatrics, Howard Hughes Medical Institute, Denver, Colorado 80206.',
                         location_infos)


if __name__ == '__main__':
    unittest.main()
