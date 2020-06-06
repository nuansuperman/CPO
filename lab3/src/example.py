# Different methods are used depending on the type of input parameter
from multimethod import multimethod
import functools

def Merge(dict1, dict2):
    return(dict2.update(dict1))
#Enter different data types and merge data
@multimethod(int, int)
def foo(a, b):
    return a+b
@multimethod(float, float)
def foo(a, b):
    return a - b

@multimethod(str, str)
def foo(a, b):
    return a + b

@multimethod(dict, dict)
def foo(a, b):
    res = {**a, **b}
    return res


@multimethod(str)
@multimethod(str, int)
def foo(a, b=10):
    c = str(b)
    return a + c

#Enter different data types and calculate the average
@multimethod(float)
@multimethod(float, int)
@multimethod(float, int, str)
def foo(a, b=20, c='30'):
    d=int(c)
    return (a + b + d)/3




