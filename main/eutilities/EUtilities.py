import requests

from main.model.Article import Article

BASE_ADDRESS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
PMC_ADDITIONAL_INFOS = "AuthorNameDisambiguation[tool]+AND+brian.pulfer@student.supsi.ch[email]"


class DATABASES:
    PubMed = "pubmed"
    Protein = "protein"
    Gene = "gene"


class Query:
    """Class that represents a query. A query might contain publication date and mesh terms information"""

    def __init__(self, pdat="", mesh=list(), any_terms=[]):
        self.pdat = pdat
        self.mesh = mesh
        self.any_terms = any_terms

    def set_pubblication_date(self, pdat):
        """Changes the query publication date to the given one"""
        self.pdat = pdat

    def set_mesh_terms(self, mesh_terms):
        """Changes the query mesh terms to the given ones"""
        self.mesh = mesh_terms

    def add_mesh_term(self, mesh_term):
        """Adds a mesh term in the query"""
        self.mesh.append(mesh_term)

    def set_any_terms(self, any_terms):
        """Changes the query any terms (type not specified) to the given ones"""
        self.any_terms = any_terms

    def add_any_terms(self, any_term):
        """Adds an any-term in the query. An any-term could be anything"""
        self.any_terms.append(any_term)

    def to_string(self):
        """Returns a string that represents the query. This string is used as end-point for the REST request"""
        at = ""
        mesh = ""
        pub_date = (self.pdat+"[pdat]")

        if pub_date == "[pdat]":
            pub_date = ""

        for elem in self.any_terms:
            at += (str(elem)+"+AND+")

        for elem in self.mesh:
            mesh += (elem+"[mesh]+AND+")

        return at+mesh+pub_date


def search(database_name, query):
    """Given a database name and a query object, returns a JSON containing infos on the related publications/articles"""
    url = \
        BASE_ADDRESS+"esearch.fcgi?db="+database_name+"&term="+query.to_string() + \
        "&"+PMC_ADDITIONAL_INFOS+"&usehistory=y"

    return requests.get(url)


def fetch(database_name, query, rettype="abstract", retmode="text"):
    """Given a database name and query object, returns the fetched data.

       Rettype field can be: 'abstract', 'fasta', 'xml', 'acc'.
       Retmode field can be: 'text', 'xml'

       RETTYPE ABSTRACT: returns the raw text of the article's abstract
       RETTYPE FASTA: returns just the essential information of the article, such as author's informations and PMID
       RETTYPE XML: returns the whole article as an XML file
       RETTYPE ACC: """

    # Sending a search request
    response = search(database_name, query)

    # Extracting QueryKey and WebEnv from the search's response
    query_key = response.content.decode('utf-8').split('<QueryKey>')[1].split('</QueryKey>')[0]
    web_env = response.content.decode('utf-8').split('<WebEnv>')[1].split('</WebEnv>')[0]

    # Sending the fetch request and returning the response
    url = BASE_ADDRESS+"efetch.fcgi?db="+database_name+"&query_key="+query_key+"&WebEnv="+web_env+\
                        "&rettype="+rettype+"&retmode="+retmode
    return requests.get(url)


def fetch_articles(database_name, query, rettype="abstract", retmode="text"):
    """Returns a list of articles with field 'raw_text' filled."""

    response = fetch(database_name, query, rettype, retmode)
    raw_texts = str(response.content).split('[Indexed for MEDLINE]')
    del raw_texts[-1]

    ret_val = list()

    for txt in raw_texts:
        ret_val.append(Article(raw_text=txt))

    return ret_val


def search_by_pmid(PMID):
    url = BASE_ADDRESS+"esearch.fcgi?db=pubmed&term="+str(PMID)+"&"+PMC_ADDITIONAL_INFOS
    return requests.get(url)


def extract_ids(response_content):
    """Given a result's content of a research, returns a list of all ids. This method is meant to work with PubMed"""
    ids = str(response_content).split("<Id>")
    ids_str = "".join(ids)
    ids = ids_str.split("</Id>")

    ids.remove(ids[0])
    ids.remove(ids[len(ids)-1])

    for i in range(len(ids)):
        ids[i] = int(ids[i][2:])

    return ids
