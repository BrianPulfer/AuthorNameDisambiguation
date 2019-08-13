import os
import unittest

import definitions
from main.retrievers.doc2vec import doc2vec


class TestDoc2Vec(unittest.TestCase):
    def test_vector(self):
        """Tests that a vector is retrieved correctly for every article"""

        # Only tests one file every 'rate'.
        rate = 100
        rate_count = 0
        tested = 0

        for filename in os.listdir(definitions.PATH_TO_ARTICLES):
            rate_count = rate_count + 1

            if rate_count == rate:
                rate_count = 0
                if filename.endswith('.xml'):
                    pmid = filename[:-4]

                    vector = doc2vec.get_vector(pmid)
                    self.assertEqual(doc2vec.DOC2VEC_VECTOR_DIMENSION, len(vector))
                    tested = tested + 1

        # Checks that at least 10 files were tested
        self.assertTrue(tested > 10)


if __name__ == '__main__':
    unittest.main()