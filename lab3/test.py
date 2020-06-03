import unittest
from positonal import *
from position_inheritances import multimethod_inheritance
from name import multimethod_name
from optional import multimethod_optional
class PositionalArgsTestCase(unittest.TestCase):

    def test_add(self):
        """test multimethod"""
        class test(object):
            @multimethod_position(int, int)
            def add(a, b):
                return 'int: a+b = {}'.format(a+b)

            @multimethod_position(float, float)
            def add(a, b):
                return 'float: a+b = {}'.format(a+b)

            @multimethod_position(str, str)
            def add(a, b):
                return 'string: a+b = {}'.format(a+b)
        X = test()
        self.assertEqual(X.add(4, 5), 'int: a+b = 9')
        self.assertEqual(X.add(1.2, 3.4), 'float: a+b = 4.6')
        self.assertEqual(X.add('dayday', 'up'), 'string: a+b = daydayup')

    def test_multiply(self):
        """test multimethod"""
        class test(object):
            @multimethod_position(int, int)
            def multiply(a, b):
                return 'int: a*b = {}'.format(int(a*b))

            @multimethod_position(float, float)
            def multiply(a, b):
                return 'float: a*b = {}'.format(a*b)
        X = test()
        self.assertEqual(X.multiply(1, 2), 'int: a*b = 2')
        self.assertEqual(X.multiply(1.0, 2.0), 'float: a*b = 2.0')

    def test_divide(self):
        """test multimethod"""
        class test(object):
            @multimethod_position(int, int)
            def divide(a, b):
                return 'int: a/b = {}'.format(int(a/b))

            @multimethod_position(float, float)
            def divide(a, b):
                return 'float: a/b = {}'.format(a/b)
        X = test()
        self.assertEqual(X.divide(1, 2), 'int: a/b = 0')
        self.assertEqual(X.divide(1.0, 2.0), 'float: a/b = 0.5')



class MultimethodTestCase(unittest.TestCase):
    def test_multimethod(self):
        class test(object):
            @multimethod_inheritance(int,int,int)
            def foo(a, b, c):
                return a*b*c
            @multimethod_inheritance(float, float)
            def foo( a, b):
                return a+b

            @multimethod_inheritance(str, str)
            def foo(a, b):
                return a+b

            @multimethod_inheritance(dict, dict)
            def foo( a, b):
                return "dict, dict"
        X=test()
        self.assertEqual(X.foo(1,2,3),6)
        self.assertEqual(X.foo(1.2,3.4),4.6)
        self.assertEqual(X.foo("dayday","up"),"daydayup")
        self.assertEqual(X.foo(dict(first_name='yong'), dict(last_name='ding')), "dict, dict")

class NamedArgsTest(unittest.TestCase):
    def test_multimethod_name(self):
        @multimethod_name(2)
        def foo(a, b):
            return a+b
        self.assertEqual(foo(a=11, b=22), 33)

        @multimethod_name(3)
        def foo(a, b, d):
            return a+b+d
        self.assertEqual(foo(a=11, b=22, d=33), 66)

        @multimethod_name(4)
        def foo(a, b, c, d):
            return a+b+c+d
        self.assertEqual(foo(11, 22, c=33, d=44), 110)

class OptionalArgsTest(unittest.TestCase):
    def test_multimethod_optional(self):
        @multimethod_optional(2)
        def foo(a, b):
            return a+b

        @multimethod_optional(3)
        def foo(a, b, c):
            return a+b+c

        @multimethod_optional(4)
        def foo(a, b, c, d):
            return a + b + c + d

        self.assertEqual(foo(123, 456), 579)
        self.assertEqual(foo(123, 456,789), 1368)
        self.assertEqual(foo(1, 2, 3, 4), 10)

if __name__ == '__main__':
    unittest.main()
