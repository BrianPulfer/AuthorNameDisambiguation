import unittest

from main.model.affiliation import Affiliation


class TestAffiliation(unittest.TestCase):
    """Test class for the 'Affiliation' class"""

    def test_class(self):
        """Tests all the class methods"""
        infos = "TEST: Dana-Farber Cancer Institute"
        affiliation = Affiliation(infos)

        self.assertEqual(infos, affiliation.get_infos())
        self.assertEqual(affiliation.TYPE.INSTITU, affiliation.get_type())
        self.assertEqual(affiliation.DESCRIPTOR.CANCER, affiliation.get_descriptor())


if __name__ == '__main__':
    unittest.main()
