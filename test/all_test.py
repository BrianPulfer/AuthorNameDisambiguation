import unittest

# Classifier imports
from test.classifiers_test.cart_test import TestCART
from test.classifiers_test.knn_test import TestKNN
from test.classifiers_test.random_forest_test import TestRandomForest
from test.classifiers_test.sequential_test import TestSequential
from test.classifiers_test.svm_test import TestSVM

# EUtilities import
from test.eutilities_test.e_utilities_test import TestQueries

# Loader import
from test.loader_test.article_loader_test import TestArticleLoader

# Model imports
from test.model_test.affiliation_test import TestAffiliation
from test.model_test.article_pair_test import TestArticlePair
from test.model_test.article_test import TestArticle
from test.model_test.author_test import TestAuthor

# OGER import
from test.oger_test.oger_test import TestOrgerUtility

# Retrievers imports
from test.retrievers_test.doc2vec.doc2vec_test import TestDoc2Vec
from test.retrievers_test.ambiguity_score_test import TestAmbiguityScoreRetriever
from test.retrievers_test.authors_test import TestAuthorsRetriever
from test.retrievers_test.date_test import TestDateRetriever
from test.retrievers_test.entities_test import TestEntitiesRetriever
from test.retrievers_test.language_test import TestLanguageRetriever
from test.retrievers_test.mail_test import TestEmailRetriever
from test.retrievers_test.mesh_test import TestMeshTermsRetriever

# MainApp import
from test.main_app_test import MainTest

LOADER = unittest.TestLoader()
RUNNER = unittest.TextTestRunner(verbosity=2)


def test_all():
    """Tests everything in the 'test' package except for the 'test.retrievers_test.jnius' package"""
    # Classifiers tests
    suites = [LOADER.loadTestsFromTestCase(TestCART),
              LOADER.loadTestsFromTestCase(TestKNN),
              LOADER.loadTestsFromTestCase(TestRandomForest),
              LOADER.loadTestsFromTestCase(TestSequential),
              LOADER.loadTestsFromTestCase(TestSVM)
              ]
    for suite in suites:
        RUNNER.run(suite)

    # EUtilities tests
    suites = [LOADER.loadTestsFromTestCase(TestQueries)
              ]
    for suite in suites:
        RUNNER.run(suite)

    # Loader tests
    suites = [LOADER.loadTestsFromTestCase(TestArticleLoader)
              ]
    for suite in suites:
        RUNNER.run(suite)

    # Model tests
    suites = [LOADER.loadTestsFromTestCase(TestAffiliation),
              LOADER.loadTestsFromTestCase(TestArticlePair),
              LOADER.loadTestsFromTestCase(TestArticle),
              LOADER.loadTestsFromTestCase(TestAuthor)
              ]
    for suite in suites:
        RUNNER.run(suite)

    # OGER tests
    suites = [LOADER.loadTestsFromTestCase(TestOrgerUtility)]
    for suite in suites:
        RUNNER.run(suite)

    # Retrievers tests
    suites = [LOADER.loadTestsFromTestCase(TestDoc2Vec),
              LOADER.loadTestsFromTestCase(TestAmbiguityScoreRetriever),
              LOADER.loadTestsFromTestCase(TestAuthorsRetriever),
              LOADER.loadTestsFromTestCase(TestDateRetriever),
              LOADER.loadTestsFromTestCase(TestEntitiesRetriever),
              LOADER.loadTestsFromTestCase(TestLanguageRetriever),
              LOADER.loadTestsFromTestCase(TestEmailRetriever),
              LOADER.loadTestsFromTestCase(TestMeshTermsRetriever)
              ]
    for suite in suites:
        RUNNER.run(suite)

    # Main test
    main_suite = LOADER.loadTestsFromTestCase(MainTest)
    RUNNER.run(main_suite)


if __name__ == '__main__':
    """Runs every test exept for the jnius package (test.retrievers_test.jnius). 
    EUtilities failing tests MUST be checked by running them separately."""
    test_all()
    print("All tests executed")
