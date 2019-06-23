import unittest

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
        xml_article_raw_content = xml_article.content.decode('utf-8')

        # Retrieving a mail
        mail = EMailRetriever.find_email(xml_article_raw_content)

        # Checking that the mail is correct
        self.assertEqual('yongzhang945@hotmail.com', mail)

        # Testing with an article that contains no e-mail addresses
        pmid = 31167299

        query = EUtilities.Query(any_terms=[pmid])

        xml_article = EUtilities.fetch(EUtilities.DATABASES.PubMed, query, rettype="xml")
        xml_article_raw_content = xml_article.content.decode('utf-8')

        no_mail = EMailRetriever.find_email(xml_article_raw_content)

        self.assertEqual(None, no_mail)

    def test_find_emails(self):
        """Tests that all e-mail are retrieved from a string (method 'find_emails()'"""

        mails = EMailRetriever.find_emails("reach me at: first@testmail.com and second@testmail.org. "
                                           "Invalid mail are anythingendingwith@ or @nythingstarting")

        self.assertEqual(['first@testmail.com', 'second@testmail.org'], mails)


if __name__ == '__main__':
    unittest.main()
