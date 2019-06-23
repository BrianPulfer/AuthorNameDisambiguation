import unittest
from main.info_retrievers import EntitiesRetriever


class TestEntitiesRetriever(unittest.TestCase):
    def test_find_entities(self):
        """Tests that the OGER entities are correctly read from the files."""
        path = './../../dataset/articles_entities/'

        # Trying with an article which entities exist
        pmid = 1255999
        entities = EntitiesRetriever.find_entities(pmid, path)

        self.assertEqual(['disease', 'disease', 'Light', 'disease'], entities)

        # Trying with an empty file (no entities for the article)
        pmid = 191009
        entities = EntitiesRetriever.find_entities(pmid, path)

        self.assertEqual([], entities)


if __name__ == '__main__':
    unittest.main()
