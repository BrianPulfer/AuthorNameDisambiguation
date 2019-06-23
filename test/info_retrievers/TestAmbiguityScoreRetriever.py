import unittest
from main.info_retrievers import AmbiguityScoreRetriever


class TestAmbiguityScoreRetriever(unittest.TestCase):
    def test_get_ambiguity_score(self):
        lastname = 'test'
        initial = 't'

        dataset = [[lastname, initial],
                   ['Test', initial],
                   [lastname, 'T']]

        self.assertEqual(1/3, AmbiguityScoreRetriever.get_ambiguity_score(lastname, initial, dataset, 0, 1))

        dataset = [[lastname, initial],
                   [lastname, initial],
                   [lastname, 'P']]

        self.assertEqual(2/3, AmbiguityScoreRetriever.get_ambiguity_score(lastname, initial, dataset, 0, 1))


if __name__ == '__main__':
    unittest.main()
