import unittest
from main.classifiers.svm import SVM


class TestSVM(unittest.TestCase):
    def test_classifier(self):
        """Tests the general behaviour of the classifier (train and predict)"""
        x_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
        y_train = [0, 1, 1, 1]

        classifier = SVM()
        classifier.fit(x_train, y_train)

        prediction_1 = classifier.predict([[0, 0]])
        prediction_2 = classifier.predict([[1, 1]])

        self.assertEqual(0, prediction_1)
        self.assertEqual(1, prediction_2)


if __name__ == '__main__':
    unittest.main()
