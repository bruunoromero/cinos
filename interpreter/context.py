class Context:
    def __init__(self, parent):
        self.__defs = {}
        self.__parent = parent

    @staticmethod
    def new():
        return Context(None)

    def extend(self):
        return Context(self)

    def has(self, name):
        try:
            _ = self.__defs[name]
            return True
        except:
            return False

    def get(self, name):
        if self.has(name):
            return self.__defs[name]
        elif self.__parent is not None:
            return self.__parent.get(name)
        else:
            raise Exception("%s not found" % name)

    def set(self, name, value):
        self.__defs[name] = value
        return value
