from main.oger.ctrl.router import Router, PipelineServer


class OgerUtility:
    """Wrapper class for the OGER API"""

    def __init__(self, termlist_path):
        """The termlist_path must be a string path to a tsv file containing the term list.
        The default term list file is located in 'main/oger_test/test/testfiles/test_terms.tsv'"""

        self.conf = Router(termlist_path=termlist_path)
        self.pl = PipelineServer(self.conf)

    def get_entities_by_pmids(self, pmids):
        """Returns all the entities for the given articles pmids"""
        all_entities = []

        coll = self.pl.load_one(pmids, fmt='pubmed')
        self.pl.process(coll)

        for article in coll:
            entities_iter = article.iter_entities()
            entities = []

            for entity in entities_iter:
                entities.append(entity)

            all_entities.append(entities)

        return all_entities
