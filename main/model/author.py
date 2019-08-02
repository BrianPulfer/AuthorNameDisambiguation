class Author:
    """Class which represents an Author. Contains all the needed author's infos"""

    def __init__(self, lastname: str, forename: str, initials: str):
        self.lastname = lastname
        self.forename = forename
        self.initials = initials

    # Getters and Setters
    def get_initials(self):
        return self.initials

    def set_initial(self, initials):
        self.initials = initials

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_forename(self):
        return self.forename

    def set_forename(self, forename):
        self.forename = forename
