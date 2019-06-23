from sklearn import neighbors


class KNN:
    def __init__(self, k):
        self.k = k
        self.classifier = neighbors.KNeighborsClassifier(k)

    def fit(self, x_train, y_train):
        """Trains the classifier. Note that the features should be normalized/standarized."""
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        """Returns the classifier predictions for the given instances.
        Note that the features should be normalized/standarized."""
        return self.classifier.predict(x_test)
