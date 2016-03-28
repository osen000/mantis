from sys import maxsize

class Project:
    def __init__(self, name=None, status=None, inherit_global=None, view_state=None, description=None, id=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.name, self.id)
    #
    # def __eq__(self, other):
    #     return (self.name == other.name and self.id == other.id)
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name
    # def key(self):
    #     return self.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize