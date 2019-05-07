from .node import UTANode


class UTAFunctionCall(UTANode):
    def __init__(self, callee, args):
        self.__callee = callee
        self.__args = args

    @property
    def callee(self):
        return self.__callee

    @property
    def args(self):
        return self.__args
