import unittest
from main.retrievers import entities


class TestEntitiesRetriever(unittest.TestCase):
    def test_find_entities(self):
        """Tests that the OGER entities are correctly read from the files."""
        path = './../../dataset/articles_entities/'

        # Trying with an article which entities exist
        pmid = 1255999
        ents = entities.find_entities(pmid, path)

        self.assertEqual(['D004194', 'D004194', 'CHEBI:30212', 'D004194'], ents)

        # Trying with an empty file (no entities for the article)
        pmid = 191009
        ents = entities.find_entities(pmid, path)

        self.assertEqual([], ents)


if __name__ == '__main__':
    unittest.main()
