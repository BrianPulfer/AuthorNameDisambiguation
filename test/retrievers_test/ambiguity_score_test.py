import unittest
from main.retrievers import ambiguity_score


class TestAmbiguityScoreRetriever(unittest.TestCase):
    def test_get_ambiguity_score(self):
        lastname = 'test'
        firstname = 't'

        # Only first row matches
        dataset = [[lastname, firstname, 'other lastname', 'other firstname'],
                   ['Test', firstname, 'other lastname', 'other firstname'],
                   [lastname, 'T', 'other lastname', 'other firstname']]

        self.assertEqual(1 / 6, ambiguity_score.get_ambiguity_score(lastname, firstname[0], dataset, 0, 1, 2, 3))

        # All 3 rows matches
        dataset = [[lastname, firstname, 'NA', 'NA'],
                   [lastname, firstname, 'NA', 'NA'],
                   [lastname, firstname, 'NA', 'NA']]

        self.assertEqual(3 / 6, ambiguity_score.get_ambiguity_score(lastname, firstname[0], dataset, 0, 1, 2, 3))

    def test_are_strings(self):
        self.assertTrue(ambiguity_score.are_strings("String1", 'str2', '5'))
        self.assertFalse(ambiguity_score.are_strings('String1', 'str2', 5, '5'))


if __name__ == '__main__':
    unittest.main()
