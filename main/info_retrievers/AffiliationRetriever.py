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
    return Affiliation(find_affiliation_infos(article_content))


def find_affiliation_infos(article_content):
    """Given a string (containing xml content), returns the content of the <Affiliation> tag. None otherwise."""

    # Checking that the file contains the Affiliation tag
    if len(article_content.split('<Affiliation>')) < 2:
        return None

    return article_content.split('<Affiliation>')[1].split('</Affiliation>')[0]
