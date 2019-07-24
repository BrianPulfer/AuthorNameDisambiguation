import numpy as np


def get_ambiguity_score(namespace_lastname: str, namespace_initial: str,  dataset,
                        ds_ln1_col, ds_fn1_col, ds_ln2_col, ds_fn2_col):
    """
    Calculates how ambiguous a name is in rapport to its dataset.
    :param namespace_lastname: The namespace full lastname
    :param namespace_initial:  The namespace firstname initial
    :param dataset:            The dataset where the namespace is included
    :param ds_ln1_col:          The dataset column where first articles lastnames are contained
    :param ds_fn1_col:          The dataset column where first articles firstnames are contained
    :param ds_ln2_col:          The dataset column where second articles lastnames are contained
    :param ds_fn2_col:          The dataset column where second articles firstnames are contained
    :return:                   A value between 0 and 1, where 0 is not ambiguous and 1 is most ambiguous
    """
    ds = np.array(dataset)

    total_authors = len(ds)*2
    matching_authors = 0

    for elem in dataset:
        # Retrieving the row's authors infos
        lastname1, firstname1, lastname2, firstname2 = \
            elem[ds_ln1_col], elem[ds_fn1_col], elem[ds_ln2_col], elem[ds_fn2_col]

        # If first author infos are legal and match, increase counter
        if are_strings(lastname1, firstname1):
            if lastname1 == namespace_lastname and firstname1[0] == namespace_initial:
                matching_authors = matching_authors + 1

        # If second author infos are legal and match, increase counter
        if are_strings(lastname2, firstname2):
            if lastname2 == namespace_lastname and firstname2[0] == namespace_initial:
                matching_authors = matching_authors + 1

    return matching_authors/total_authors


def are_strings(*args):
    return all(map(lambda _: type(_) is str, args))