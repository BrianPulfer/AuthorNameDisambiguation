from country_list import countries_for_language


def find_country(article_content):
    """Finds an article's country given it's  XML object (soup).
    None is returned if no country is found."""
    all_countries = dict(countries_for_language('en'))

    if article_content.Affiliation is not None:
        if article_content.Affiliation.string is not None:
            for v in all_countries.values():
                if v.lower() in article_content.Affiliation.string.lower():
                    return v

    if article_content.Country is not None:
        if article_content.Country.string is not None:
            for v in all_countries.values():
                if v.lower() in article_content.Country.string.lower():
                    return v
            return article_content.Country.string

    return None


def find_city(article_content):
    """Finds an article's city given it's XML object (soup).
    None is returned if the xml does not contain the 'Affiliation' tag."""
    country = find_country(article_content)

    if country is not None and get_affiliation_infos(article_content) is not None:
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
    if article_content.Affiliation is None:
        return None
    return article_content.Affiliation.string
