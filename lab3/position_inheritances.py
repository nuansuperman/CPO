from positonal import Mulitimethod
dict_check={}
class Mulitimethod_inheritance(Mulitimethod):
    def nn(self):
        print("It's a class which inherent from Mulitimethod")

def multimethod_inheritance(*types): #position parameter
    def register(function):
        name = function.__name__
        names = dict_check.get(name)
        if names is None:
            names = dict_check[name] = Mulitimethod_inheritance(name)
        names.register(types, function)
        return names
    return register

