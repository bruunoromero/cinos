from parser import parse
from transformer import transform
from interpreter import interpret

tree = parse("(def a (. plus 1 2))")
mappedTree = transform(tree)
context, _ = interpret(mappedTree)
print(context.get("a"))
