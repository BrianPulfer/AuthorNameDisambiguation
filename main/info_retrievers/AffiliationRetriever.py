import enum
from main.model.Affiliation import Affiliation


class ORG_TYPES(enum.Enum):
    """Enum of the organization types"""
    Univers = 1
    Institu = 2
    College = 3
    Labor = 4
    Organ = 5
    Ministry = 6
    Cent = 7
    Department = 8
    Hospital = 9
    School = 10


def find_affiliation(article_content):
    """Constructs an Affiliation object by finding its raw infos, org_type and res_type."""
    return Affiliation(find_affiliation_infos(article_content), find_org_type(article_content),
                       find_res_type(article_content))


def find_affiliation_infos(article_content):
    """Given a string (containing xml content), returns the content of the <Affiliation> tag. None otherwise."""

    # Checking that the file contains the Affiliation tag
    if len(article_content.split('<Affiliation>')) < 2:
        return None

    return article_content.split('<Affiliation>')[1].split('</Affiliation>')[0]


def find_org_type(article_content):
    """Returns a tuple of 2 elements: The first element is the organisation type as integer, the second is the
    organisation type as string e.g. (1,'Univers') """
    affiliation = find_affiliation_infos(article_content)
    org_type = 0

    if affiliation is None:
        return None

    for type in ORG_TYPES:
        if type.name in affiliation:
            org_type = org_type + type.value

    return org_type


def find_res_type(article_content):
    """Returns a tuple of 2 elements: The first element is the organisation field as integer, the second is the
    organisation field as string e.g. (1,'Biolog') """
    affiliation = find_affiliation_infos(article_content)
    res_type = 0

    if affiliation is None:
        return None

    if 'Biolog' in affiliation:
        res_type = 1
    elif 'Chemist' in affiliation:
        res_type = 2
    elif 'Pediatric' in affiliation or 'Surgery' in affiliation or 'Medicine' in affiliation or 'Medical' in affiliation:
        res_type = 3
    elif 'Genetic' in affiliation:
        res_type = 4
    elif 'Infect' in affiliation:
        res_type = 5
    elif 'Agricult' in affiliation:
        res_type = 6
    elif 'Entomolog' in affiliation:
        res_type = 7
    elif 'Biotech' in affiliation:
        res_type = 8
    elif 'Neurolog' in affiliation:
        res_type = 9
    elif 'Psychol' in affiliation:
        res_type = 10
    elif 'Pharma' in affiliation:
        res_type = 11
    elif 'Toxic' in affiliation:
        res_type = res_type + 1.1
    elif 'Cancer' in affiliation:
        res_type = res_type + 2.1
    elif 'Cardiol' in affiliation:
        res_type = 12
    elif 'Dentist' in affiliation:
        res_type = res_type + 13.5
    elif 'Nutrition' in affiliation:
        res_type = 13
    elif 'Health' in affiliation:
        res_type = res_type + 0.6
    elif 'Disease' in affiliation:
        res_type = res_type + 0.11

    return res_type
