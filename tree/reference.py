from .node import CNSNode


class CNSSymbol(CNSNode):
    def __init__(self, loc, name):
        super(CNSSymbol, self).__init__(loc)
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)


class CNSReference:
    def __init__(self, symbols):
        self.__symbols = symbols

    @property
    def symbols(self):
        return self.__symbols

    def __repr__(self):
        reprs = map(lambda symbol: symbol.__repr__(), self.symbols)
        return "%s(%s)" % (self.__class__.__name__, ", ".join(reprs))
