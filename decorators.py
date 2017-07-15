def property_required(func):
    def func_wrapper(self, value):
        return "hola"
    return func_wrapper
