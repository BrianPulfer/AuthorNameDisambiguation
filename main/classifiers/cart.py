from sklearn.tree import DecisionTreeClassifier


class CART:
    """Wrapper class for a CART classifier"""

    def __init__(self):
        """Initializes classifier"""

        self._clf = DecisionTreeClassifier()

    def fit(self, x_train, y_train):
        """Trains the classifier"""

        self._clf.fit(x_train, y_train)

    def predict(self, x_test):
        """Returns the classifier predictions"""

        return self._clf.predict(x_test)


