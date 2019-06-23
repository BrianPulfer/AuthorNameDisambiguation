def find_keywords(article_content):
    """Finds the article keywords given its raw content (as string)"""

    meshes = article_content.split('MajorTopicYN')
    meshes = meshes[1:]

    retval = []

    for m in meshes:
        retval.append(m.split('<')[0].split('>')[1])

    return retval
