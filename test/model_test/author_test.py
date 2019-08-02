import unittest
from main.model.author import Author


class TestAuthor(unittest.TestCase):
    def test_class(self):
        author = Author('lastname', 'forename', 'initials')

        self.assertEqual('lastname', author.get_lastname())
        self.assertEqual('forename', author.get_forename())
        self.assertEqual('initials', author.get_initials())


if __name__ == '__main__':
    unittest.main()