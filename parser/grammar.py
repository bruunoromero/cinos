grammar = """
start: quoted_value*

SYMBOL: /[\-\+a-zA-Z\?\*$=%!\/<>\.][\-\+a-zA-Z0-9\?\*$=%!\/<>\.]*/

QUOTE: "'"

refer: SYMBOL(":"SYMBOL)?

list: "(" quoted_value* ")"

vec: "[" quoted_value* "]"

map: "{" quoted_value* "}"

KEYWORD: /:[\-\+a-zA-Z0-9\?\*$=%!\/<>\.]+/

primitive: KEYWORD
         | STRING
         | INT
         | FLOAT
         
value: refer
     | list
     | vec
     | map
     | primitive

quoted_value: QUOTE? value
     
%import common.WS
%import common.INT
%import common.FLOAT
%import common.ESCAPED_STRING -> STRING
%ignore WS
"""