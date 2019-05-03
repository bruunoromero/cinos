grammar = """
start: expr 

expr: unary_expr

BANG: "!"
PLUS: "+"
MINUS: "-"

unary_op: PLUS
        | MINUS

unary_expr: unary_op primitive

?primitive: STRING
          | INT
          | FLOAT

%import common.INT
%import common.FLOAT
%import common.ESCAPED_STRING -> STRING
"""