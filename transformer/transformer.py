from lark import Transformer
from .node import CNSQuote
from .location import CNSLocation
from .reference import CNSSymbol, CNSReference
from .derivated import CNSList, CNSMap, CNSVector
from .primitive import CNSInt, CNSFloat, CNSString, CNSKeyword


def transform(tree):
    return _CNSTransformer().transform(tree)

class _CNSTransformer(Transformer):

    @staticmethod
    def start(args):
        return args

    @staticmethod
    def primitive(args):
        token = args[0]
        loc = CNSLocation(token)
        if token.type == "INT":
            return CNSInt(loc, int(token))
        elif token.type == "KEYWORD":
            return CNSKeyword(loc, token[1:])
        elif token.type == "STRING":
            return CNSString(loc, token[1:-1])
        elif token.type == "FLOAT":
            return CNSFloat(loc, float(token))
        else:
            raise Exception("Unknown primitive %s" % token.type)

    @staticmethod
    def value(args):
        return args[0]

    @staticmethod
    def refer(args):
        symbols = map(lambda arg: CNSSymbol(CNSLocation(arg), arg), args)
        return CNSReference(symbols)

    @staticmethod
    def list(args):
        return CNSList(args)

    @staticmethod
    def map(args):
        return CNSMap(args)

    @staticmethod
    def vec(args):
        return CNSVector(args)

    @staticmethod
    def quoted_value(args):
        if len(args) == 2:
            return CNSQuote(args[1])

        return args
