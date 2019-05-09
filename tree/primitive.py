from .node import CNSNode


class CNSPrimitive(CNSNode):
    def __init__(self, loc, value):
        super(CNSPrimitive, self).__init__(loc)
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.value)


class CNSInt(CNSPrimitive):
    pass


class CNSFloat(CNSPrimitive):
    pass


class CNSString(CNSPrimitive):
    pass


class CNSKeyword(CNSPrimitive):
    pass
