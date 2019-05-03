from lark import Lark
from .grammar import grammar


def parse(content):
    parser = Lark(grammar)
    return parser.parse(content)
