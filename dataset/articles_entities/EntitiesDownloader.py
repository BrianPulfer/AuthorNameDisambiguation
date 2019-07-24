import os
import sys
import pandas as pd

import definitions
from main.oger.oger_utility import OgerUtility


PATH_TO_TRAINING_SET = './../1500_pairs_train.csv'
PATH_TO_TESTING_SET = './../400_pairs_test.csv'
UTILITY = OgerUtility('./../../main/oger_test/test/testfiles/test_terms.tsv')


def download_entities(pmids=None):
    """Downloads the entities in a .entities file for the specified pmids.
    Downloads all entities of the dataset if no pmids are given."""

    if pmids is None:
        # If no pmids are given as argument, downloads entities for every PMID in the dataset.
        training_set = pd.read_csv(PATH_TO_TRAINING_SET, sep=";", encoding='latin').\
            dropna(subset=['PMID1', 'PMID2', 'Authorship']).values
        testing_set = pd.read_csv(PATH_TO_TESTING_SET, sep=";", encoding='latin').\
            dropna(subset=['PMID1', 'PMID2', 'Authorship']).values

        training_pmids = list(training_set[:, 0])
        testing_pmids = list(testing_set[:, 0])

        training_pmids.extend(list(training_set[:, 4]))
        testing_pmids.extend(list(testing_set[:, 4]))

        all_pmids = training_pmids
        all_pmids.extend(testing_pmids)

        # Downloading the entities just once for article
        pmids = list(set(all_pmids))

        # Converting the pmids into strings with no decimal values.
        for i in range(len(pmids)):
            pmids[i] = str(pmids[i])
            if '.' in pmids[i]:
                pmids[i] = pmids[i][:-2]

    print("Downloading entities for", len(pmids), "articles.")
    download(pmids)
    print("Entities successfully written to files.")


def download(pmids):
    """Writes the entities to files for the specified pmids."""

    # Writing once per each file because bugs happens otherwise (inefficient, might be changed)
    for pmid in pmids:
        filename = str(pmid)+".entities"

        if not os.path.isfile(filename):
            file = open(filename, 'w')
            entities = UTILITY.get_entities_by_pmids([pmid])

            for i in range(len(entities)):
                for j in range(len(entities[i])):
                    file.write(entities[i][j].text+"\n")
                file.write("\n")

            file.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        download_entities(sys.argv[1:])
    else:
        download_entities()

    print("Program finished")
