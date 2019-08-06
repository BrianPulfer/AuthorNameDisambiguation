import os
import unittest

import definitions
from main.retrievers.doc2vec import doc2vec


class TestDoc2Vec(unittest.TestCase):
    def test_vector(self):
        """Tests that a vector is retrieved correctly for every article"""

        for filename in os.listdir(definitions.PATH_TO_ARTICLES):
            if filename.endswith('.xml'):
                pmid = filename[:-4]

                vector = doc2vec.get_vector(pmid)
                self.assertEqual(doc2vec.DOC2VEC_VECTOR_DIMENSION, len(vector))


if __name__ == '__main__':
    unittest.main()