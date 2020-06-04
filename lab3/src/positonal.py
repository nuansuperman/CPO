dict_check={}

class Mulitimethod(object):
    def __init__(self,name):
        self.name=name
        self.type={}
    def __call__(self, *args, **kwargs):
        types=tuple(arg.__class__ for arg in args)
        function=self.type.get(types)
        if function is None:
            raise TypeError("Type is empty")
        return function(*args)
    def register(self,types,function):
        if types in self.type:
            raise TypeError("The type already exists")
        self.type[types] = function


def multimethod_position(*types): #position parameter
    def register(function):
        name = function.__name__
        names = dict_check.get(name)
        if names is None:
            names = dict_check[name] = Mulitimethod(name)
        names.register(types, function)
        return names
    return register
def multimethod_defaults(*types):  #Defaults parameter
    def register(function):
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        names = dict_check.get(name)
        if names is None:
            names.dict_check[name]=Mulitimethod(name)
        names.register(types, function)
        names.__lastreg__ = function
        return names
    return register


















