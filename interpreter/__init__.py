import transformer


def evaluate(ls):
    el = ls[0]
    if isinstance(el, transformer.CNSFloat.__class__):
        print("float")


def interpret(tree):
    return list(map(evaluate, tree))
