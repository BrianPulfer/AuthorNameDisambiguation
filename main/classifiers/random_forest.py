import sklearn.ensemble


class RandomForest:
    """Wrapper class for the sklearn RandomForest implementation"""

    def __init__(self, estimators):
        """Initializes the classifier giving the number of decision trees for the forest"""
        self._classifier = sklearn.ensemble.RandomForestClassifier(estimators)

    def fit(self, x_train, y_train):
        """Trains the classifier"""
        self._classifier.fit(X=x_train, y=y_train)

    def predict(self, x_test):
        """Returns predictions for the testing data"""
        return self._classifier.predict(x_test)

    def feature_importances_(self):
        """Returns the features importances"""
        return self._classifier.feature_importances_
