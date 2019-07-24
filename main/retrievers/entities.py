PATH_TO_DATASET = './../../dataset/article_entities/'


def find_entities(pmid, dir_path=PATH_TO_DATASET):
    """Finds the .entities file for a given article pmid. Returns the entities as a list."""

    full_path = dir_path + str(pmid) + ".entities"
    file = open(full_path)

    entities = list()

    for line in file:
        if line is not '\n':
            line = line[:-1]
            entities.append(line)

    file.close()
    return entities
