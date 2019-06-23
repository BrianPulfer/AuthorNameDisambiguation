import unittest
from main.model.Author import Author


class TestAuthor(unittest.TestCase):
    def test_class(self):
        author = Author('lastname', 'forename', 'initials')

        self.assertEqual('lastname', author.lastname)
        self.assertEqual('forename', author.forename)
        self.assertEqual('initials', author.initials)


if __name__ == '__main__':
    unittest.main()