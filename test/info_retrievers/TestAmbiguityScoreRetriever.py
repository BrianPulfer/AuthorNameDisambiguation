import unittest
from main.info_retrievers import AmbiguityScoreRetriever


class TestAmbiguityScoreRetriever(unittest.TestCase):
    def test_get_ambiguity_score(self):
        lastname = 'test'
        firstname = 't'

        # Only first row matches
        dataset = [[lastname, firstname, 'other lastname', 'other firstname'],
                   ['Test', firstname, 'other lastname', 'other firstname'],
                   [lastname, 'T', 'other lastname', 'other firstname']]

        self.assertEqual(1/6, AmbiguityScoreRetriever.get_ambiguity_score(lastname, firstname[0], dataset, 0, 1, 2, 3))

        # All 3 rows matches
        dataset = [[lastname, firstname, 'NA', 'NA'],
                   [lastname, firstname, 'NA', 'NA'],
                   [lastname, firstname, 'NA', 'NA']]

        self.assertEqual(3/6, AmbiguityScoreRetriever.get_ambiguity_score(lastname, firstname[0], dataset, 0, 1, 2, 3))

    def test_are_strings(self):
        self.assertTrue(AmbiguityScoreRetriever.are_strings("String1", 'str2', '5'))
        self.assertFalse(AmbiguityScoreRetriever.are_strings('String1', 'str2', 5, '5'))


if __name__ == '__main__':
    unittest.main()
