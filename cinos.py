import parser
from ast import UntypedTransformer

tree = parser.parse(":a")
print(UntypedTransformer().transform(tree))
