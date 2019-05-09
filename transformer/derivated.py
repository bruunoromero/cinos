class CNSList:
    def __init__(self, els):
        self.__els = els

    @property
    def els(self):
        return self.__els

    def __repr__(self):
        reprs = map(lambda symbol: symbol.__repr__(), self.els)
        return "%s(%s)" % (self.__class__.__name__, ", ".join(reprs))


class CNSVector(CNSList):
    pass


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


class CNSMap:
    def __init__(self, els):
        if len(els) % 2 != 0:
            raise Exception("Map with odd number of elements")

        self.__entries = chunks(els, 2)

    @property
    def entries(self):
        return self.__entries

    def __repr__(self):
        reprs = map(lambda symbol: symbol.__repr__(), self.entries)
        return "%s(%s)" % (self.__class__.__name__, ", ".join(reprs))