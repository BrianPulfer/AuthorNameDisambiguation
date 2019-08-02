from enum import Enum


class Affiliation:
    """Class that represents an Affiliation"""

    class TYPE(Enum):
        """Possible Affiliation Types"""
        UNIVERS = 1
        INSTITU = 2
        COLLEGE = 3
        LABOR = 4
        ORGANI = 5
        MINISTRY = 6
        CENTER = 7
        DEPARTMENT = 8
        HOSPITAL = 9
        SCHOOL = 10

    class DESCRIPTOR(Enum):
        """Possible Affiliation Descriptors"""
        BIOLOG = 1
        CHEMIST = 2
        PEDIATRIC = 3
        SURGERY = 4
        MEDIC = 5
        GENETIC = 6
        INFECT = 7
        AGRICULT = 8
        ENTOMOLOG = 9
        BIOTECH = 10
        NEUROLOG = 11
        PSYCHOL = 12
        PHARMA = 13
        TOXIC = 14
        CANCER = 15
        CARDIOL = 16
        DENTIST = 17
        NUTRITION = 18
        HEALTH = 19
        DISEASE = 20

    def __init__(self, infos):
        """Constructs the object"""
        self._infos = infos
        self._type = self._find_type(infos)
        self._descriptor = self._find_descriptor(infos)

    # Type & Descriptor finder methods
    def _find_type(self, text: str):
        """Returns the Affiliation Type by searching in the given string"""
        if text is None:
            return None

        temp = text.upper()

        for t in self.TYPE:
            if t.name in temp:
                return t
        return None

    def _find_descriptor(self, text):
        """Returns the Affiliation Descriptor by searching in the given string"""
        if text is None:
            return None

        temp = text.upper()

        for d in self.DESCRIPTOR:
            if d.name in temp:
                return d
        return None

    # Getters & Setters
    def get_infos(self):
        return self._infos

    def set_infos(self, infos):
        self._infos = infos

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_descriptor(self):
        return self._descriptor

    def set_descriptor(self, descriptor):
        self._descriptor = descriptor
