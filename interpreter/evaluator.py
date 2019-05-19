import transformer
from .vector import evaluate_vector
from .map_literal import evaluate_map
from .primitive import evaluate_primitive
from .reference import evaluate_reference
from .s_expression import evaluate_s_expression


def evaluate(ls, context):
    el = ls[0]
    if isinstance(el, transformer.CNSPrimitive):
        return evaluate_primitive(el)
    elif isinstance(el, transformer.CNSVector):
        return evaluate_vector(el, evaluate)
    elif isinstance(el, transformer.CNSList):
        return evaluate_s_expression(el, evaluate, context)
    elif isinstance(el, transformer.CNSMap):
        return evaluate_map(el, evaluate)
    elif isinstance(el, transformer.CNSReference):
        return evaluate_reference(el, context)
    else:
        print("dont know")
