import unittest
from main.classifiers.random_forest import RandomForest


class TestRandomForest(unittest.TestCase):
    def test_class(self):
        """Tests that the classifier is constructed and works as expected"""
        classifier = RandomForest(100)

        x_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
        y_train = [0, 0, 1, 1]

        classifier.fit(x_train, y_train)

        predictions = classifier.predict(x_train)

        self.assertEqual(0, predictions[0])
        self.assertEqual(0, predictions[1])
        self.assertEqual(1, predictions[2])
        self.assertEqual(1, predictions[3])


if __name__ == '__main__':
    unittest.main()
