from lang.primitive import build_primitive


def evaluate_primitive(el):
    return build_primitive(el.value)
