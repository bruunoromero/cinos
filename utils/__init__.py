def reference_to_str(ref):
    symbols_str = list(map(lambda symbol: symbol.name, ref.symbols))
    return "$".join(symbols_str)
