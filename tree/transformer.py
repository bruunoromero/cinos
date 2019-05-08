from lark import Transformer
from .node import CNSQuote
from .location import CNSLocation
from .primitive import CNSInt, CNSKeyword


class CNSTransformer(Transformer):

    @staticmethod
    def primitive(args):
        token = args[0]
        loc = CNSLocation(token)
        if token.type == "INT":
            return CNSInt(loc, int(token))
        elif token.type == "KEYWORD":
            return CNSKeyword(loc, token[1:])

    @staticmethod
    def quoted_value(args):
        if len(args) == 2:
            return CNSQuote(args[1])

        return args
