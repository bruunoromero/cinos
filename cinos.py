import parser
from tree import CNSTransformer

tree = parser.parse("{:a 10"
                    " :b 30}")
print(CNSTransformer().transform(tree))
