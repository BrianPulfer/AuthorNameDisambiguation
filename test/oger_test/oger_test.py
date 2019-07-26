import unittest
import definitions

from main.oger.oger_utility import OgerUtility
from main.oger.ctrl.router import Router, PipelineServer


class TestOrgerUtility(unittest.TestCase):
    def test_library(self):
        """Tests that the OGER library works correctly. Local files are loaded and content is verified.
        2 articles are downloaded from pubmed and their content is verified.
        Entity recognition is run and denotations are verified."""

        conf = Router(termlist_path=definitions.ROOT_DIR + '/main/oger/test/testfiles/test_terms.tsv')
        pl = PipelineServer(conf)

        # Loading articles from local files
        doc = pl.load_one(definitions.ROOT_DIR + '/main/oger/test/testfiles/txt/13373697.txt', 'txt')
        self.assertTrue('The kind and the measure of ventilation disorders in tuberculous' in doc.text)

        # Downloading articles
        coll = pl.load_one(['21436587', '21436588'], fmt='pubmed')

        first_article = coll[0]
        first_article_title = first_article[0]
        first_article_content = first_article[1]
        self.assertEqual('2011', first_article.year)
        self.assertTrue('Human prostate cancer metastases' in first_article_title.text)
        self.assertTrue('HSC homing, quiescence' in first_article_content.text)

        second_article = coll[1]
        second_article_title = second_article[0]
        second_article_content = second_article[1]
        self.assertEqual('2011', second_article.year)
        self.assertTrue('FOXO3 programs tumor-associated DCs' in second_article_title.text)
        self.assertTrue('The limited success of cancer immunotherapy is often ' in second_article_content.text)

        # Running entity recognition
        pl.process(coll)

        entities_iter = first_article.iter_entities()
        entities = []

        for entity in entities_iter:
            entities.append(entity)

        self.assertEqual(28, len(entities))

        # Verifying first article's first entity
        first_entity = entities[0]
        self.assertEqual('Human', first_entity.text)
        self.assertEqual(0, first_entity.start)
        self.assertEqual(5, first_entity.end)
        self.assertEqual('9606', first_entity.cid)
        self.assertEqual(('organism', 'Homo sapiens', 'NCBI Taxonomy', '9606', 'CUI-less'), first_entity.info)

        # Verifying first article's last entity
        last_entity = entities[-1]
        self.assertEqual('disease', last_entity.text)
        self.assertEqual(1253, last_entity.start)
        self.assertEqual(1260, last_entity.end)
        self.assertEqual('D004194', last_entity.cid)
        self.assertEqual(('disease', 'Disease', 'MeSH desc (Diseases)', 'D004194', 'C0012634'), last_entity.info)

    def test_ogerutility(self):
        """Tests the OgerUtility class created to simplify the syntax"""

        utility = OgerUtility(definitions.ROOT_DIR + '/main/oger/test/testfiles/test_terms.tsv')
        entities = utility.get_entities_by_pmids(['21436587', '21436588'])

        # Verifying first article's first entity
        first_entity = entities[0][0]
        self.assertEqual('Human', first_entity.text)
        self.assertEqual(0, first_entity.start)
        self.assertEqual(5, first_entity.end)
        self.assertEqual('9606', first_entity.cid)
        self.assertEqual(('organism', 'Homo sapiens', 'NCBI Taxonomy', '9606', 'CUI-less'), first_entity.info)

        # Verifying first article's last entity
        last_entity = entities[0][-1]
        self.assertEqual('disease', last_entity.text)
        self.assertEqual(1253, last_entity.start)
        self.assertEqual(1260, last_entity.end)
        self.assertEqual('D004194', last_entity.cid)
        self.assertEqual(('disease', 'Disease', 'MeSH desc (Diseases)', 'D004194', 'C0012634'), last_entity.info)


if __name__ == '__main__':
    unittest.main()
