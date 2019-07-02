import copy
import numpy as np


def get_ambiguity_score(namespace_lastname: str, namespace_initial: str,  dataset, ds_ln_col, ds_fn_col):
    """
    Calculates how ambiguous a name is in rapport to its dataset.
    :param namespace_lastname: The namespace full lastname
    :param namespace_initial:  The namespace firstname initial
    :param dataset:            The dataset where the namespace is included
    :param ds_ln_col:          The dataset column where lastnames are contained
    :param ds_fn_col:          The dataset column where firstnames are contained
    :return:                   A value between 0 and 1, where 0 is not ambiguous and 1 is most ambiguous
    """
    ds = np.array(dataset)

    total_rows = len(ds)
    matching_rows = 0

    for elem in dataset:
        if elem[ds_ln_col] == namespace_lastname and elem[ds_fn_col][0] == namespace_initial:
            matching_rows = matching_rows + 1

    return matching_rows/total_rows
