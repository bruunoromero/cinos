class CNSNode:
    def __init__(self, loc):
        self.__location = loc


class CNSQuote(CNSNode):
    def __init__(self, quoted):
        self.__value = quoted

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.__value)