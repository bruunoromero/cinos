import parser
from transformer import transform
from interpreter import interpret

tree = parser.parse("1.1")
print(tree)
mappedTree = transform(tree)
interpret(mappedTree)
