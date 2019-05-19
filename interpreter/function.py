from utils import reference_to_str

class Function:
    def __init__(self, params, fn, context):
        self.__fn = fn
        self.__meta = None
        self.__params = params
        self.__arity = len(params)
        self.__parent_context = context

    @property
    def fn(self):
        return self.__fn

    @property
    def arity(self):
        return self.__arity

    def with_meta(self, meta):
        self.__meta = meta

    def invoke(self, args=[]):
        if self.match_arity(args):
            fn_context = self.__parent_context.extend()
            self.bind_args_to_context(args, fn_context)
            return self.fn(fn_context)
        else:
            raise Exception("Function do not match arity")

    def bind_args_to_context(self, args, context):
        for index in range(len(self.__params)):
            arg = args[index]
            param = self.__params[index]
            context.set(param, arg)

    def match_arity(self, args):
        return len(args) == len(self.__params)
