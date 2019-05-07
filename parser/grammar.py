grammar = """
start: value*

symbol: /[\-\+a-zA-Z\?\*$=%!\/<>\.][\-\+a-zA-Z0-9\?\*$=%!\/<>\.]*/

refer: symbol(":"symbol)?

list: "(" value* ")"

vec: "[" value* "]"

map: "{" value* "}"

keyword: ":" symbol

value: refer
     | list
     | vec
     | keyword
     | map
     | STRING
     | INT
     | FLOAT
     
%import common.WS
%import common.INT
%import common.FLOAT
%import common.ESCAPED_STRING -> STRING
%ignore WS
"""