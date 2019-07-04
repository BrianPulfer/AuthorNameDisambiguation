import unittest

from bs4 import BeautifulSoup

from main.info_retrievers import EMailRetriever
from main.eutilities import EUtilities


class TestEmailRetriever(unittest.TestCase):
    def test_find_email(self):
        """Tests that an e-mail is found in a pubblication where e-mail address is present. Also tests that no e-mail
        is found in a pubblication that has no e-mail addresses."""

        # Fetching an article and extracting its content as string
        pmid = '31167205'

        query = EUtilities.Query(any_terms=[pmid])

        xml_article = EUtilities.fetch(EUtilities.DATABASES.PubMed, query, rettype="xml", retmode="text")
        soup = BeautifulSoup(xml_article.content.decode('utf-8'), "xml")

        # Retrieving a mail
        mail = EMailRetriever.find_email(soup)

        # Checking that the mail is correct
        self.assertEqual('yongzhang945@hotmail.com', mail)

        # Testing with an article that contains no e-mail addresses
        pmid = 31167299

        query = EUtilities.Query(any_terms=[pmid])

        xml_article = EUtilities.fetch(EUtilities.DATABASES.PubMed, query, rettype="xml")
        soup = BeautifulSoup(xml_article.content.decode('utf-8'), "xml")

        no_mail = EMailRetriever.find_email(soup)

        self.assertEqual(None, no_mail)


if __name__ == '__main__':
    unittest.main()
