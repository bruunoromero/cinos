import parser
from transformer import transform
from interpreter import interpret

tree = parser.parse("(def a (fn* [a] a))")
mappedTree = transform(tree)
context, _ = interpret(mappedTree)
print(context.get("a").invoke([1]))
