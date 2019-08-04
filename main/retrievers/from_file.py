import os
import definitions

PATH_TO_ENTITIES = definitions.ROOT_DIR + '/dataset/articles_entities/'
PATH_TO_LOC_ORG = definitions.ROOT_DIR + '/dataset/articles_locs_orgs/'
PATH_TO_JDST = definitions.ROOT_DIR + '/dataset/articles_jdst/'


"""Scripts which offers method to retrieve information that has been written to files"""


def load_entities(pmid, dir_path=PATH_TO_ENTITIES):
    """Loads the .entities file for a given article pmid. Returns the entities as a list."""

    full_path = dir_path + str(pmid) + '.entities'
    file = open(full_path)

    entities = list()

    for line in file:
        if line is not '\n':
            line = line[:-1]
            entities.append(line)

    file.close()
    return entities


def load_jdst(pmid, dir_path=PATH_TO_JDST):
    """Loads the .jds and .sts files for the given article pmid. Returns a touple of 2 lists: (jds, sts)"""

    jds_path = dir_path + str(pmid) + '.jds'
    sts_path = dir_path + str(pmid) + '.sts'

    jds, sts = list(), list()

    if os.path.isfile(jds_path):
        file = open(jds_path, 'r')
        for line in file:
            if line is not '\n':
                line = line[:-1]
                jds.append(line)
        file.close()

    if os.path.isfile(sts_path):
        file = open(sts_path, 'r')
        for line in file:
            if line is not '\n':
                line = line[:-1]
                sts.append(line)
        file.close()

    if len(jds) == 0:
        jds = None
    if len(sts) == 0:
        sts = None

    return jds, sts


def load_locs_orgs(pmid, dir_path=PATH_TO_LOC_ORG):
    """Loads the .orgs and .locs files for the given article pmid. Returns a touple of 2 lists: (locs, orgs)"""

    loc_path = dir_path + str(pmid) + '.loc'
    org_path = dir_path + str(pmid) + '.org'

    loc_infos, org_infos = list(), list()

    if os.path.isfile(loc_path):
        file = open(loc_path, 'r')
        for line in file:
            if line is not '\n':
                line = line[:-1]
                loc_infos.append(line)

    if os.path.isfile(org_path):
        file = open(org_path)
        for line in file:
            if line is not '\n':
                line = line[:-1]
                org_infos.append(line)

    if len(loc_infos) == 0:
        loc_infos = None

    if len(org_infos) == 0:
        org_infos = None

    return loc_infos, org_infos
