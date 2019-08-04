import os
import definitions
import pandas as pd

from main.loader import article_loader


def write_jdst():
    """Writes every Journal Descriptor and Semantic Type for every article into files"""

    training_set = pd.read_csv(definitions.PATH_TO_TRAINING_SET, sep=";", encoding='latin'). \
        dropna(subset=['PMID1', 'PMID2', 'Authorship'], how='any').values

    testing_set = pd.read_csv(definitions.PATH_TO_TESTING_SET, sep=";", encoding='latin'). \
        dropna(subset=['PMID1', 'PMID2', 'Authorship'], how='any').values

    training_pmids = list(training_set[:, 0])
    testing_pmids = list(testing_set[:, 0])

    training_pmids.extend(list(training_set[:, 4]))
    testing_pmids.extend(list(testing_set[:, 4]))

    all_pmids = training_pmids
    all_pmids.extend(testing_pmids)

    # Downloading the entities just once for article
    pmids = list(set(all_pmids))

    for pmid in pmids:
        # Converting the pmid from number to string
        pmid = str(int(pmid))

        # Loading the article's data
        article = article_loader.load_article(pmid)

        # Writing the article's journal descriptors
        filename = pmid + '.jds'

        if not os.path.isfile(filename):
            file = open(filename, 'w')

            for jd in article.get_jds():
                file.write(jd+'\n')
            file.close()

        # Writing the article's semantic types
        filename = pmid + '.sts'

        if not os.path.isfile(filename):
            file = open(filename, 'w')

            for st in article.get_sts():
                file.write(st+'\n')
            file.close()


if __name__ == '__main__':
    write_jdst()
