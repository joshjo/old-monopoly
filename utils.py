def property_required(func):
    def func_wrapper(self):
        return "hola"
    return func_wrapper
