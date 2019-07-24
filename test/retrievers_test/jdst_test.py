import unittest
import definitions

from main.retrievers.jdst import JDSTRetriever


PATH_TO_ARTICLES = definitions.ROOT_DIR + '/dataset/articles/'


class TestJDSTRetriever(unittest.TestCase):

    @staticmethod
    def get_test_text():
        file = open(PATH_TO_ARTICLES+'4622441.xml', 'r')
        article_content = file.read()
        file.close()

        return article_content

    def test_get_jds(self):
        """Tests that the Journal Descriptors are correctly retrieved from the article"""
        retriever = JDSTRetriever()

        jds = retriever.get_jds(self.get_test_text())

        self.assertEqual('Behavioral Sciences', jds[0])
        self.assertEqual('Nutritional Sciences', jds[1])
        self.assertEqual('Biology', jds[2])

        self.assertEqual(3, len(jds))

    def test_get_sts(self):
        """Tests that the Semantic Types are correctly retrieved from the article"""
        retriever = JDSTRetriever()

        sts = retriever.get_sts(self.get_test_text())

        self.assertEqual('Conceptual Entity', sts[0])
        self.assertEqual('Pathologic Function', sts[1])
        self.assertEqual('Finding', sts[2])

        self.assertEqual(3, len(sts))


if __name__ == '__main__':
    unittest.main()
