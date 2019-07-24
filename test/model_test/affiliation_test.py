import unittest

from main.model.affiliation import Affiliation


class TestAffiliation(unittest.TestCase):
    """Test class for the 'Affiliation' class"""

    def test_class(self):
        """Tests all the class methods"""
        infos = "Test Affiliation infos"
        affiliation = Affiliation(infos)

        self.assertEqual(infos, affiliation.get_infos())

        infos = "Testing"
        affiliation.set_infos(infos)

        self.assertEqual(infos, affiliation.get_infos())


if __name__ == '__main__':
    unittest.main()
