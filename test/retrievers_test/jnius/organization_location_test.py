import unittest
import bs4

import definitions

from main.retrievers.jnius.ner import organization_location


class OrganizationLocationTest(unittest.TestCase):
    def test_find_organization_location(self):
        """Tests that the organization infos are correctly retrieved"""
        pmid = 25582491

        file = open(definitions.PATH_TO_ARTICLES + str(pmid) + '.xml', 'r')
        article_content = file.read()
        file.close()

        soup = bs4.BeautifulSoup(article_content, 'xml')

        loc = organization_location.find_location(soup)
        org = organization_location.find_organization(soup)

        self.assertEqual(['Hefei', 'PR', 'China'], loc)
        self.assertEqual(['Anhui', 'Medical', 'University'], org)


if __name__ == '__main__':
    unittest.main()