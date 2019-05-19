def evaluate_entry(entry, evaluator):
    return list(map(evaluator, entry))


def evaluate_map(el, evaluator):
    mapped = {}
    evaluated_entries = list(map(lambda entry: evaluate_entry(entry, evaluator), el.entries))

    for [key, value] in evaluated_entries:
        mapped[key] = value

    return mapped
