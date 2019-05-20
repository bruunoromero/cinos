
def build_primitive(value):
    if isinstance(value, int):
        return Integer(value)
    elif isinstance(value, float):
        return Float(value)
    elif isinstance(value, str):
        return String(value)


class Primitive:
    def plus(self, right):
        return build_primitive(self + right)

    def sub(self, right):
        return build_primitive(self - right)

    def mul(self, right):
        return build_primitive(self * right)

    def div(self, right):
        return build_primitive(self / right)

    def greet(self):
        return "ola mundo"


class Integer(Primitive, int):
    def __new__(cls, value):
        return int.__new__(cls, value)


class Float(Primitive, float):
    def __new__(cls, value):
        return float.__new__(cls, value)


class String(Primitive, str):
    def __new__(cls, value):
        return str.__new__(cls, value)
