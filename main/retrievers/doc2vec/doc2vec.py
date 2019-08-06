import os
import bs4
import definitions

from gensim.models.doc2vec import Doc2Vec, TaggedDocument


DOC2VEC_MODEL_FILE_PATH = definitions.ROOT_DIR+'/main/retrievers/doc2vec/doc2vec_model'
DOC2VEC_VECTOR_DIMENSION = 300


def _get_all_articles():
    """Returns a list containing all articles. Each article is a list of strings."""
    articles = list()

    for filename in os.listdir(definitions.PATH_TO_ARTICLES):
        if filename.endswith('.xml'):
            pmid = filename[:-4]

            file = open(definitions.PATH_TO_ARTICLES + filename, 'r')
            content = file.read()
            file.close()

            soup = bs4.BeautifulSoup(content, 'xml')
            article = list()

            if soup.ArticleTitle is not None:
                title_words = str(soup.ArticleTitle.string).split(' ')
                for word in title_words:
                    article.append(word)

            if soup.AbstractText is not None:
                text_words = str(soup.AbstractText.string).split(' ')
                for word in text_words:
                    article.append(word)

            articles.append(TaggedDocument(article, [pmid]))
    return articles


def train_model():
    """Trains a doc2vec model and persist it to a file"""
    documents = _get_all_articles()

    model = Doc2Vec(documents, vector_size=DOC2VEC_VECTOR_DIMENSION, window=2, min_count=1, workers=4)
    model.delete_temporary_training_data(True, True)
    model.save(DOC2VEC_MODEL_FILE_PATH)


def get_vector(pmid):
    """Loads the doc2vec previously trained and uses it to assign a vector to the given document"""

    model = Doc2Vec.load(DOC2VEC_MODEL_FILE_PATH)
    return model.docvecs[str(pmid)]


if __name__ == '__main__':
    train_model()
    print("Model successfully trained. Vector dimension per document: ", DOC2VEC_VECTOR_DIMENSION)
