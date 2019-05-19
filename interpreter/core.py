from .function import Function
from utils import reference_to_str


def fn(args, evaluator, context):
    body = args[1]
    params_list = list(map(lambda ref: reference_to_str(ref[0]), args[0][0].els))

    return Function(params_list, lambda fn_ctx: evaluator(body, fn_ctx), context)


def define(args, evaluator, context):
    name = reference_to_str(args[0][0])
    value = evaluator(args[1], context)
    return context.set(name, value)


core_evaluators = {
    "fn*": fn,
    "def": define,
}


def evaluate_core_fn(expr, evaluator, context):
    args = expr.els[1:]
    name = expr.els[0][0].symbols[0].name
    core_evaluator = core_evaluators[name]

    if core_evaluator:
        return core_evaluator(args, evaluator, context)
    else:
        raise Exception("error")
