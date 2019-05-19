from .context import Context
from .evaluator import evaluate


def interpret(tree):
    initial_context = Context.new()
    exprs = list(map(lambda el: evaluate(el, initial_context), tree))
    return initial_context, exprs
