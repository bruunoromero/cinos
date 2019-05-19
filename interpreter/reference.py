from utils import reference_to_str


def evaluate_reference(ls, context):
    ref_str = reference_to_str(ls)
    return context.get(ref_str)
