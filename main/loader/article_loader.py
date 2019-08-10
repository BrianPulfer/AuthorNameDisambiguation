import definitions

from bs4 import BeautifulSoup

from main.model.article import Article


from main.retrievers import  authors, date, mail,\
    mesh, from_file, language

PATH_TO_ARTICLES = definitions.ROOT_DIR + '/dataset/articles/'
PATH_TO_ARTICLES_ENTITIES = definitions.ROOT_DIR + '/dataset/articles_entities/'


def load_article(pmid):
    """Given the PMID, creates and returns an article full of all its retrievable informations."""

    # Opening the file and reading the content
    file = open(PATH_TO_ARTICLES+str(pmid)+'.xml', 'r')
    article_content = file.read()
    file.close()

    # Converting raw string into an object
    soup = BeautifulSoup(article_content, 'xml')

    # Retrieving basic infos
    lan = language.find_language(soup)
    auts = authors.find_authors(soup)
    dat = date.find_date(soup)
    e_mail = mail.find_email(soup)
    meshes = mesh.find_mesh_terms(soup)

    # Retrieving infos written in files
    loc, org = from_file.load_locs_orgs(pmid)

    return Article(PMID=pmid, authors=auts, language=lan, e_mail=e_mail, date=dat, loc_list=loc, org_list=org,
                   mesh_terms=meshes)
