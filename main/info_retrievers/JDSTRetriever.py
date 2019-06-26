from py4j.java_gateway import JavaGateway

# Connecting to the Java Gateway
gateway = JavaGateway()

# Saving a reference to the Java instance of 'TextCategorization'
text_categorization = gateway.entry_point


def get_jds(pmid):
    """Given an article's PMID, returns the article Journal Descriptors"""
    # TODO
    pass


def get_sts(pmid):
    """Given an article's PMID, returns the article Semantic Types"""
    # TODO
    pass
