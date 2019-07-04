class Affiliation:
    """Class that represents an Affiliation"""

    def __init__(self, infos):
        """Constructs the object"""
        self._infos = infos

    # Getters
    def get_infos(self):
        return self._infos

    def set_infos(self, infos):
        self._infos = infos
