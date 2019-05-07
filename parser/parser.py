from lark import Lark
from .grammar import grammar


def parse(content):
    parser = Lark(grammar, propagate_positions=True)
    return parser.parse(content)
