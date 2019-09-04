import unittest

from main.main_app import compute_accuracy, get_set, normalize_set, fill_empty_with_average, fill_empty_with_random
from decimal import Decimal
import pandas as pd
import numpy as np


class MainTest(unittest.TestCase):

    def test_compute_accuracy(self):
        """Tests the 'compute_accuracy' method in Main with different values."""

        # Testing full accuracy on 5 labels
        y_star = [1, 0, 0, 1, 0]
        y = [1, 0, 0, 1, 0]
        self.assertEqual(compute_accuracy(y_star, y), 1,
                         "Accuracy should be 1 for [1,0,0,1,0] [1,0,0,1,0]")

        # Testing full failure on 1 label
        y_star = [1]
        y = [0]
        self.assertEqual(compute_accuracy(y_star, y), 0,
                         "Accuracy should be 0 for [1] [0]")

        # Testing decimal accuracy on 5 labels
        y_star = [0, 0, 0, 0, 0]
        y = [0, 0, 0, 1, 1]
        self.assertEqual(compute_accuracy(y_star, y), Decimal('0.6'),
                         "Accuracy should be 0.6 for [0,0,0,0,0] [0,0,0,1,1]")

        # Testing decimal accuracy on 5 labels with different values
        y_star = [5.2, -10, -15.3, "str", 0]
        y = [5.2, -10, -15.3, "str", 1000]
        self.assertEqual(compute_accuracy(y_star, y), Decimal('0.8'),
                         "Accuracy should be 0.8 for [5.2, -10, -15.3, 'str', 0] [5.2, -10, -15.3, 'str', 1000]")

    def test_get_set(self):
        """Tests that data from CSV file is loaded without null values"""

        # Retrieving sets
        training_set = get_set('../dataset/1500_pairs_train.csv')
        testing_set = get_set('../dataset/400_pairs_test.csv')

        sets = [training_set, testing_set]

        # Checking that there is no null value in any cell of the matrix of any csv file
        for current in range(len(sets)):
            for row in range(len(sets[current])):
                self.assertFalse(pd.isnull(sets[current][row, 0]))   # No PMID1 can be null
                self.assertFalse(pd.isnull(sets[current][row, 4]))   # No PMID2 can be null
                self.assertFalse(pd.isnull(sets[current][row, 8]))   # No Authorship can be null

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
        normalized_set = normalize_set(dataset, [False, False, False, False])

        for col in range(len(normalized_set[0])):
            for row in range(len(normalized_set)):
                self.assertEqual(new_set[col][row], normalized_set[row, col])

    def test_fill_empty_with_average(self):
        """Tests that a bi-dimensional matrix containing '-1' values is replaced with the same matrix with mean column
         value instead of the '-1's."""
        test_matrix = np.array([[1, 2, 3],
                                [1, -1, 5],
                                [-1, -1, -1]])

        expected = np.array([[1, 2, 3],
                             [1, 2, 5],
                             [1, 2, 4]])

        new_matrix = fill_empty_with_average(test_matrix)

        for row in range(len(expected)):
            for col in range(len(expected[row])):
                self.assertEqual(expected[row, col], new_matrix[row, col])

    def test_fill_empty_with_random(self):
        """Tests that -1 values in a matrix are converted in a random value between the column's min and max value"""
        matrix = np.array([[0, 100, 15],
                           [-100, 100, 45],
                           [-1, -1, -1]])

        result = fill_empty_with_random(matrix)

        # Checking first column
        self.assertTrue(result[2][0] < 0)
        self.assertTrue(result[2][0] >= -100)

        # Checking second column
        self.assertEqual(100, result[2][1])

        # Checking third column
        self.assertTrue(result[2][2] < 45)
        self.assertTrue(result[2][2] >= 15)


if __name__ == '__main__':
    unittest.main()
