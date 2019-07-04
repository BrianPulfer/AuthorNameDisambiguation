from lxml import objectify
from country_list import countries_for_language


def find_country(article_content):
    """Finds an article's country given it's raw text (string) from the XML format.
    None is returned if no country is found."""
    affiliation_infos = get_affiliation_infos(article_content)
    all_countries = dict(countries_for_language('en'))

    if affiliation_infos is None:
        return None

    for v in all_countries.values():
        if v in affiliation_infos.string:
            return v

    return None


def find_city(article_content):
    """Finds an article's city given it's raw text (string) from the XML format.
    None is returned if the xml does not contain the 'Affiliation' tag."""
    country = find_country(article_content)

    if country is not None:
        affiliation_infos = get_affiliation_infos(article_content)
        city = affiliation_infos.string.split(country)[0]

        if ',' in city:
            city = city.split(',')[-2]
        if " " in city:
            city = city.split(" ")[-1]
        return city

    return None


def get_affiliation_infos(article_content):
    """Returns the affiliation infos given the xml as a string.
    An empty string is returned if the xml does not contain the 'Affiliation' tag."""
    return article_content.Affiliation.string
