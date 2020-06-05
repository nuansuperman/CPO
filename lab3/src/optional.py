dict_check={}


class Mulitimethod(object):
    def __init__(self,name):
        self.name=name
        self.type={}
    def __call__(self, *args, **kwargs):
        num=len(args)
        function=self.type.get(num)
        if function is None:
            raise TypeError("Type is empty")
        return function(*args)
    def register(self,types,function):
        if types in self.type:
            raise TypeError("The type already exists")
        self.type[types] = function


def multimethod_optional(num): #optional parameter
    def register(function):
        name = function.__name__
        names = dict_check.get(name)
        if names is None:
            names = dict_check[name] = Mulitimethod(name)
        names.register(num, function)
        return names
    return register

















