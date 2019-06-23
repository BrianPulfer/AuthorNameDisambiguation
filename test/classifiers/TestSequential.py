import unittest
import numpy as np
from main.classifiers.Sequential import Sequential


class TestSequential(unittest.TestCase):
    def test_sequential(self):
        """Tests the general behaviour of the classifier (creation, fit, predict)"""
        dataset = np.array([[0, 0],
                            [1, 0],
                            [0, 1],
                            [1, 1]])

        labels = np.array([0, 0, 1, 1])

        input_size = len(dataset[0])
        output_size = len(set(labels))

        classifier = Sequential(input_size, output_size)
        classifier.fit(dataset, labels)

        predictions = classifier.predict(np.array([[1, 1]]))

        self.assertEqual([1], predictions)


if __name__ == '__main__':
    unittest.main()
