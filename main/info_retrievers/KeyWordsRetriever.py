def find_keywords(article_content):
    """Finds the article keywords given its raw content (as string)"""

    meshes = []
    meshes.extend(article_content.findAll("DescriptorName", {'MajorTopicYN': 'Y'}))
    meshes.extend(article_content.findAll("DescriptorName", {'MajorTopicYN': 'N'}))
    meshes.extend(article_content.findAll("QualifierName", {'MajorTopicYN': 'Y'}))
    meshes.extend(article_content.findAll("QualifierName", {'MajorTopicYN': 'N'}))

    retval = []

    for m in meshes:
        retval.append(m.string)

    return retval
