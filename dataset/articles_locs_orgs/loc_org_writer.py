import os
import bs4
import pandas as pd

import definitions

from main.retrievers.jnius.ner import organization_location

def write_loc_orgs():
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

        article_file = open(definitions.PATH_TO_ARTICLES + pmid + '.xml', 'r')
        article_content = article_file.read()
        article_file.close()

        article = bs4.BeautifulSoup(article_content, 'xml')

        location_list = organization_location.find_location(article)
        organization_list = organization_location.find_organization(article)

        # Writing location infos
        if location_list is not None:
            filename = pmid + '.loc'

            if not os.path.isfile(filename):
                file = open(filename, 'w')
                for loc_info in location_list:
                    file.write(loc_info+'\n')
                file.close()

        # Writing organization infos
        if organization_list is not None:
            filename = pmid + '.org'

            if not os.path.isfile(filename):
                file = open(filename, 'w')
                for org_info in organization_list:
                    file.write(org_info+'\n')
                file.close()


if __name__ == '__main__':
    write_loc_orgs()
    print("All location and organization infos written to files.")
