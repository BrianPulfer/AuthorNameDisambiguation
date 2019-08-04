import unittest

from main.model.affiliation import Affiliation


class TestAffiliation(unittest.TestCase):
    """Test class for the 'Affiliation' class"""

    def test_class(self):
        """Tests all the class methods"""
        infos = "TEST: Dana-Farber Cancer Institute"

        self.assertEqual(Affiliation.TYPE.INSTITU, Affiliation.find_type(infos))
        self.assertEqual(Affiliation.DESCRIPTOR.CANCER, Affiliation.find_descriptor(infos))


if __name__ == '__main__':
    unittest.main()
