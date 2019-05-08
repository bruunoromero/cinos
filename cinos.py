import parser
from tree import CNSTransformer

tree = parser.parse("'(a 10 20)")
print(CNSTransformer().transform(tree))
