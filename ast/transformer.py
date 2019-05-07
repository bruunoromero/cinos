from lark import Transformer
from .primitive import UTAInt


class UntypedTransformer(Transformer):

    @staticmethod
    def primitive(args):
        token = args[0]
        if token.type == 'INT':
            return UTAInt(int(token))



