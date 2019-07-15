import numpy as np


def get_ambiguity_score(namespace_lastname: str, namespace_initial: str,  dataset,
                        ds_ln1_col, ds_fn1_col, ds_ln2_col,ds_fn2_col):
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

    total_rows = len(ds)
    matching_rows = 0

    for elem in dataset:
        # If every cell selected is a string ...
        if type(elem[ds_ln1_col]) is str and type(elem[ds_fn1_col]) is str \
                and type(elem[ds_ln2_col]) is str and type(elem[ds_fn2_col]) is str:

            # ...and if they match, increase the counter.
            if elem[ds_ln1_col] == namespace_lastname and elem[ds_fn1_col][0] == namespace_initial\
                    or elem[ds_ln2_col == namespace_lastname and elem[ds_fn2_col == namespace_initial]]:
                matching_rows = matching_rows + 1

    return matching_rows/total_rows
