import os
import definitions
import bs4

os.environ['CLASSPATH'] = definitions.ROOT_DIR + "/main/retrievers/jnius/ner/AuthoringNER.jar"

from jnius import autoclass


# Importing Java classes
CRFClassifier = autoclass('edu.stanford.nlp.ie.crf.CRFClassifier')
CoreAnnotations = autoclass('edu.stanford.nlp.ling.CoreAnnotations')
AnswerAnnotation = autoclass('edu.stanford.nlp.ling.CoreAnnotations$AnswerAnnotation')

# Defining the path for the file to be loaded (classifier)
LOAD_PATH = definitions.ROOT_DIR + '/main/retrievers/jnius/ner/english.muc.7class.distsim.crf.ser.gz'


def identify_ner(text):
    """Given a string text, returns a dictonary containing information under keys such as:
    PERSON, LOCATION, ORGANIZATION"""

    classifier = CRFClassifier.getClassifierNoExceptions(LOAD_PATH)
    entities = classifier.classify(text)

    retval = dict()

    for i in range(entities.size()):
        for j in range(entities.get(i).size()):
            label = entities.get(i).get(j)

            word = label.word()
            category = label.get(AnswerAnnotation)

            if not category == 'O':
                if category not in retval.keys():
                    retval[category] = [word]
                else:
                    retval[category].append(word)

    return retval


def find_location(article_content: bs4.BeautifulSoup):
    """Given the xml article, returns a list of elements that concern the location"""

    if article_content.Affiliation is not None:
        if article_content.Affiliation.string is not None:
            entities = identify_ner(article_content.Affiliation.string)

            if 'LOCATION' in entities.keys():
                return entities['LOCATION']
    return None


def find_organisation(article_content: bs4.BeautifulSoup):
    """Given the xml article, returns a list of elements that concern the organization"""

    if article_content.Affiliation is not None:
        if article_content.Affiliation.string is not None:
            entities = identify_ner(article_content.Affiliation.string)

            if 'ORGANIZATION' in entities.keys():
                return entities['ORGANIZATION']
    return None


print(identify_ner("University of California is located in California, United States"))
print(identify_ner("Alice went to the Museum of Natural History."))
