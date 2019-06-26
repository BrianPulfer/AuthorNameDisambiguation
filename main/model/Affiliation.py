class Affiliation:
    """Class that represents an Affiliation"""

    def __init__(self, infos, org_type: int=None, res_type: int=None):
        """Constructs the object"""
        self._infos = infos
        self._org_type = org_type
        self._res_type = res_type

    # Getters
    def get_infos(self):
        return self._infos

    def get_org_type(self):
        return self._org_type

    def get_res_type(self):
        return self._res_type
