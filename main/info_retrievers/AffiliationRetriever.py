from main.model.Affiliation import Affiliation


def find_affiliation(article_content):
    """Constructs an Affiliation object by finding its raw infos, org_type and res_type."""
    return Affiliation(find_affiliation_infos(article_content))


def find_affiliation_infos(article_content):
    """Given a string (containing xml content), returns the content of the <Affiliation> tag. None otherwise."""

    # Checking that the file contains the Affiliation tag
    if article_content.Affiliation is None:
        return None

    return article_content.Affiliation.string
