class Affiliation:
    def __init__(self, infos, org_type: int=None, res_type: int=None):
        self.infos = infos
        self.org_type = org_type
        self.res_type = res_type

    def get_infos(self):
        return self.infos

    def get_org_type(self):
        return self.org_type

    def get_res_type(self):
        return self.res_type
