import numpy as np
import pandas as pd
from decimal import Decimal

from main.info_retrievers import AmbiguityScoreRetriever

from main.loader import ArticleLoader
from main.model.ArticlePair import ArticlePair

from main.classifiers.KNN import KNN
from main.classifiers.RandomForest import RandomForest
from main.classifiers.Sequential import Sequential


def get_set(path):
    """Returns a matrix of data given the path to the CSV file. The heading row and NaN values are excluded."""
    df = pd.read_csv(path, sep=';', encoding='latin')
    return df.dropna(subset=['PMID1', 'PMID2', 'Authorship'], how='any').values


def compute_accuracy(classifier_results, labels):
    """Returns the accuracy (0-1) of a classifier given it's results and the actual labels."""
    correct = 0
    for i in range(len(labels)):
        if labels[i] == classifier_results[i]:
            correct += 1

    return Decimal(correct)/Decimal(len(labels))


def normalize_set(ds, binaries: list):
    """Applies standardization (AKA Z-Score normalization) on the 2 dimensional set"""
    normalized_set = np.array(ds)
    numpy_set = np.array(ds)
    for i in range(len(numpy_set[0])):
        if not binaries[i]:
            avg = np.mean(numpy_set[:, i])
            std = np.std(numpy_set[:, i])

            normalized_set[:, i] = (numpy_set[:, i] - avg) / std

    return normalized_set


def fill_empty_with_average(set):
    """Given a set, replaces all the -1 values with the respective column average"""
    matrix = np.array(set)
    averages = list()

    # Getting each row's average without considering -1 values.
    for col in range(len(matrix[0])):
        sum, count = 0, 0

        for row in range(len(matrix)):
            if matrix[row][col] == -1:
                pass
            else:
                sum = sum + matrix[row][col]
                count = count + 1

        averages.append(sum/count)

    # Applying the averages to the -1 values
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                matrix[i][j] = averages[j]

    return matrix


def main(training_set_path="./dataset/1500_pairs_train.csv", testing_set_path="./dataset/400_pairs_test.csv"):
    # Positive instances in the training set: 970. Negative instances in the training set: 503
    # Positive instances in the testing set: 217. Negative instances in the testing set: 182
    # Nominative training set length is 1500 Instances. After filtering out null values there are 1473 instances
    # Nominative testing set length is 400 Instances. After filtering out null values there are 397 instances

    # Retrieving sets
    training_set = get_set(training_set_path)
    testing_set = get_set(testing_set_path)

    x_train = list()
    y_train = np.array(training_set[:, 8])

    x_test = list()
    y_test = np.array(testing_set[:, 8])

    # Changing labels from 'YES'/'NO' to 1/0
    for i in range(len(y_train)):
        if 'NO' in y_train[i]:
            y_train[i] = 0
        else:
            y_train[i] = 1

    for i in range(len(y_test)):
        if 'NO' in y_test[i]:
            y_test[i] = 0
        else:
            y_test[i] = 1

    y_train = y_train.astype('int')
    y_test = y_test.astype('int')

    # Filling training set data
    for i in range(len(training_set)):
        pmid_left = int(training_set[i][0])
        pmid_right = int(training_set[i][4])

        article1 = ArticleLoader.load_article(pmid_left)
        article1.set_main_author_initials(training_set[i][2])
        article1.set_ambiguity(
            AmbiguityScoreRetriever.get_ambiguity_score(training_set[i][1],
                                                        training_set[i][2],
                                                        training_set,
                                                        1, 2, 5, 6))

        article2 = ArticleLoader.load_article(pmid_right)
        article2.set_main_author_initials(training_set[i][6])
        article2.set_ambiguity(
            AmbiguityScoreRetriever.get_ambiguity_score(training_set[i][5],
                                                        training_set[i][6],
                                                        training_set,
                                                        1, 2, 5, 6))

        article_pair = ArticlePair(article1, article2)

        x_train.append(article_pair.scores())

    # Filling testing set data
    for i in range(len(testing_set)):
        pmid_left = int(testing_set[i][0])
        pmid_right = int(testing_set[i][4])

        article1 = ArticleLoader.load_article(pmid_left)
        article1.set_main_author_initials(testing_set[i][2])
        article1.set_ambiguity(
            AmbiguityScoreRetriever.get_ambiguity_score(testing_set[i][1],
                                                        testing_set[i][2],
                                                        testing_set,
                                                        1, 2, 5, 6))

        article2 = ArticleLoader.load_article(pmid_right)
        article2.set_main_author_initials(testing_set[i][6])
        article2.set_ambiguity(
            AmbiguityScoreRetriever.get_ambiguity_score(testing_set[i][5],
                                                        testing_set[i][6],
                                                        testing_set,
                                                        1, 2, 5, 6))

        article_pair = ArticlePair(article1, article2)

        x_test.append(article_pair.scores())

    # Filling empty datas with average values
    x_train_filled = fill_empty_with_average(x_train)
    x_test_filled = fill_empty_with_average(x_test)

    # Normalizing data
    binaries_features = ArticlePair.binary_scores()

    x_train_norm = normalize_set(x_train_filled, binaries_features).astype('float64')
    x_test_norm = normalize_set(x_test_filled, binaries_features).astype('float64')

    # KNN - CLASSIFIER
    classifier = KNN(5)
    classifier.fit(x_train_norm, y_train)
    knn_accuracy = compute_accuracy(classifier.predict(x_test_norm), y_test)
    print("5NN - Classifier accuracy: " + str(int(knn_accuracy*100))+"%")

    # RANDOM FOREST - CLASSIFIER
    classifier = RandomForest(50)
    classifier.fit(x_train_norm, y_train)
    rf_accuracy = compute_accuracy(classifier.predict(x_test_norm), y_test)
    print("Random Forest - Classifier accuracy: "+str(int(rf_accuracy*100))+"%")


if __name__ == '__main__':
    main("./../dataset/1500_pairs_train.csv", "./../dataset/400_pairs_test.csv")
