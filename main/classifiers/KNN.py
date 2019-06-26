from sklearn import neighbors


class KNN:
    """A wrapper class for the K Nearest Neighbour sklearn implementation"""

    def __init__(self, k):
        """Creates the classifier giving the number of neighbours to be considered"""
        self.k = k
        self.classifier = neighbors.KNeighborsClassifier(k)

    def fit(self, x_train, y_train):
        """Trains the classifier. Note that the features should be normalized/standarized."""
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        """Returns the classifier predictions for the given instances.
        Note that the features should be normalized/standarized."""
        return self.classifier.predict(x_test)
