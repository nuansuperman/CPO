import unittest
from example import *
from  inheritance import *

class TestMultimethod(unittest.TestCase):

    # 1.support for different types
    def test_type(self):
        self.assertEqual(foo(1, 2), 3)
        self.assertEqual(foo(1.0, 1.0), 0.0)
        self.assertEqual(foo('1', 10), '110')
        self.assertEqual(foo('dayday', 'up'), 'daydayup')
        self.assertEqual(foo(dict(first_name='Yong'), dict(last_name='Ding')), {'first_name': 'Yong', 'last_name': 'Ding'})


    # 2.Optional and named parameters
    def test_optional(self):
        self.assertEqual(foo('1'), '110')
        self.assertEqual(foo('11', 9), '119')

        self.assertEqual(foo(10.0, 40, '10'), 20)
        self.assertEqual(foo(10.0), 20.0)
        self.assertEqual(foo(10.0, 2), 14)

    # 3.support for named argumants
    def test_named_object(self):
        self.assertEqual(foo(a=1, b=2), 3)
        self.assertEqual(foo(a='1', b=10), '110')

    #4.inherit
    def test_inherit(self):
        self.assertEqual(bar_A(1,3),bar_B(1,3))




if __name__ == '__main__':
    unittest.main()
