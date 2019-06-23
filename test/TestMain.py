import unittest

from main import Main
from decimal import Decimal
import pandas as pd
import numpy as np


class MainTest(unittest.TestCase):

    def test_compute_accuracy(self):
        """Tests the 'compute_accuracy' method in Main with different values."""

        # Testing full accuracy on 5 labels
        y_star = [1, 0, 0, 1, 0]
        y = [1, 0, 0, 1, 0]
        self.assertEqual(Main.compute_accuracy(y_star, y), 1,
                         "Accuracy should be 1 for [1,0,0,1,0] [1,0,0,1,0]")

        # Testing full failure on 1 label
        y_star = [1]
        y = [0]
        self.assertEqual(Main.compute_accuracy(y_star, y), 0,
                         "Accuracy should be 0 for [1] [0]")

        # Testing decimal accuracy on 5 labels
        y_star = [0, 0, 0, 0, 0]
        y = [0, 0, 0, 1, 1]
        self.assertEqual(Main.compute_accuracy(y_star, y), Decimal('0.6'),
                         "Accuracy should be 0.6 for [0,0,0,0,0] [0,0,0,1,1]")

        # Testing decimal accuracy on 5 labels with different values
        y_star = [5.2, -10, -15.3, "str", 0]
        y = [5.2, -10, -15.3, "str", 1000]
        self.assertEqual(Main.compute_accuracy(y_star, y), Decimal('0.8'),
                         "Accuracy should be 0.8 for [5.2, -10, -15.3, 'str', 0] [5.2, -10, -15.3, 'str', 1000]")

    def test_get_set(self):
        """Tests that data from CSV file is loaded without null values"""

        # Retrieving sets
        training_set = Main.get_set('../dataset/1500_pairs_train.csv')
        testing_set = Main.get_set('../dataset/400_pairs_test.csv')

        sets = [training_set, testing_set]

        # Checking that there is no null value in any cell of the matrix of any csv file
        for current in range(len(sets)):
            for row in range(len(sets[current])):
                for col in range(len(sets[current][row])):
                    self.assertFalse(pd.isnull(sets[current][row, col]))

    def test_normalize_set(self):
        """Tests that a given dataset is correctly normalized"""
        dataset = np.random.rand(1000, 4)

        col0_mean, col0_std = np.mean(dataset[:, 0]), np.std(dataset[:, 0])
        col1_mean, col1_std = np.mean(dataset[:, 1]), np.std(dataset[:, 1])
        col2_mean, col2_std = np.mean(dataset[:, 2]), np.std(dataset[:, 2])
        col3_mean, col3_std = np.mean(dataset[:, 3]), np.std(dataset[:, 3])

        new_col0 = (dataset[:, 0] - col0_mean) / col0_std
        new_col1 = (dataset[:, 1] - col1_mean) / col1_std
        new_col2 = (dataset[:, 2] - col2_mean) / col2_std
        new_col3 = (dataset[:, 3] - col3_mean) / col3_std

        new_set = [new_col0, new_col1, new_col2, new_col3]
        normalized_set = Main.normalize_set(dataset)

        for col in range(len(normalized_set[0])):
            for row in range(len(normalized_set)):
                self.assertEqual(new_set[col][row], normalized_set[row, col])


if __name__ == '__main__':
    unittest.main()
