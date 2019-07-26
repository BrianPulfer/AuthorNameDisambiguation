from sklearn import svm


class SVM:
    """Wrapper class for a Support Vector Machine classifier with custom parameters"""

    def __init__(self):
        """Initializes the classifier according to custom parameters"""

        self._clf = svm.SVC(gamma='scale')

    def fit(self, x_train, y_train):
        """Trains the classifier"""

        self._clf.fit(x_train, y_train)

    def predict(self, x_test):
        """Returns the classifier's predictions"""

        return self._clf.predict(x_test)
