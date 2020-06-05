import unittest
from nfa_rgx import *


class SymbolExpression(unittest.TestCase):
    # test |
    def test_or(self):
        st = "abbbb"
        pat = "\\*?|ab+"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)


    def test_begin(self):
        st = "bbbb"
        pat = "^bb*"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, st)

    def test_end(self):
        st = "aaaaa"
        pat = "^aa*$"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, st)

    #test .
    def test_point(self):
        st = "abaaad"
        pat= "ab.aad"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)

    #test *
    def test_multiplication(self):
        st = "bbbbbb"
        pat = "bb*"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)

    # test +
    def test_plus(self):
        st = "bbb"
        pat = "b+"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)


    # test ()
    def test_match(self):
        st = "bbbbbscccccasbdzx"
        pat= "(\\*?|b+)(xy|sc*)(asb|ebd)(dzx)"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)

    def test_part_string(self):
        st = 'hwhwhwhwhbbbbbscccccasbdzx'
        pat= r"(\*?|b+)(xy|sc*)(asb|ebd)(dzx)"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "bbbbbscccccasbdzx")

    def test_filename(self):
        st = "/hello/rjjjj/dyyyyy"
        pat = "/hello/rj+/dy+"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, st)


    def test_email(self):
        st = "aaaabbb1094466256@qq.comcdcd"
        pat="^1094466256@qq.com"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "1094466256@qq.com")
        st = "aaabbb1102667245@qq.comdcdcd"
        pat = "^1102667245@qq.com"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "1102667245@qq.com")


    def test_phoneNumber(self):
        st="aaa13355667778"
        pat = "^13+5*6*7*8$"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "13355667778")

    def test_multiple_matches(self):
        st = 'gfdgfregreg2224443333hwhsfsdfdg'
        pat = '2*4*3*'
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "2224443333")
        st = 'arkejkwjeihbbbbbscccccasbdzxwhwfsdfdg'
        pat= r"(\*?|b+)(xy|sc*)(asb|ebd)(dzx)"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "bbbbbscccccasbdzx")

    def test_negative_tests(self):
        st = "fadfsadfasf"
        pat = "zad*"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "You should enter the correct expression")


if __name__=="__main__":
    unittest.main()