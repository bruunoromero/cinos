from .core import evaluate_core_fn


def evaluate_s_expression(el, evaluator, context):
    try:
        return evaluate_core_fn(el, evaluator, context)
    except Exception:
        return None
