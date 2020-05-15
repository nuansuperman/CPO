from src.hash_immute import *
import unittest
from hypothesis import given
import hypothesis.strategies as st


class TestImmutable(unittest.TestCase):
    def test_insert(self):
        newhash = hashmap()
        insert(newhash, 1)
        self.assertEqual(to_list(newhash), [1])
        insert(newhash, 2)
        self.assertEqual(to_list(newhash), [1, 2])
        insert(newhash, 3)
        self.assertEqual(to_list(newhash), [1, 2, 3])

    def test_size(self):
        newhash = hashmap()
        insert(newhash, 1)
        self.assertEqual(size(newhash), 1)
        insert(newhash, 2)
        self.assertEqual(size(newhash), 2)
        insert(newhash, 3)
        self.assertEqual(size(newhash), 3)

    def test_to_list(self):
        newhash = hashmap()
        insert(newhash, 1)
        insert(newhash, 2)
        self.assertEqual(to_list(newhash), [1, 2])

    def test_from_list(self):
        test = [[], [2]]
        for l in test:
            newhash=hashmap()
            from_list(newhash, l)
            self.assertEqual(size(newhash), len(l))

    def test_reduce(self):
        newhash = hashmap()
        insert(newhash, 5)
        insert(newhash, 10)
        self.assertEqual(reduce(newhash, 'sum'), 15)

    def test_mconcat(self):
        newhash1 = hashmap()
        insert(newhash1, 2)
        insert(newhash1, 4)
        newhash2 = hashmap()
        insert(newhash2, 6)
        newhash3 = hashmap()
        insert(newhash3, 2)
        insert(newhash3, 4)
        insert(newhash3, 6)
        self.assertEqual(to_list(mconcat(newhash1,newhash2)), to_list(newhash3))

    def test_find_iseven(self):
        newhash = hashmap()
        insert(newhash, 3)
        insert(newhash, 4)
        self.assertEqual(find_iseven(newhash), [3])
        insert(newhash, 5)
        insert(newhash, 6)
        self.assertEqual(find_iseven(newhash), [3, 5])

    def test_filter_iseven(self):
        newhash = hashmap()
        insert(newhash, 3)
        insert(newhash, 4)
        self.assertEqual(filter_iseven(newhash), [3])
        insert(newhash, 5)
        insert(newhash, 6)
        self.assertEqual(filter_iseven(newhash), [3, 5])

    def test_iter(self):
        newlist = [1, 2, 3]
        newhash = hashmap()
        from_list(newhash, newlist)
        tmp = []
        try:
            get_next = iterator(newhash)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(newlist, tmp)
        self.assertEqual(to_list(newhash), tmp)

        get_next = iterator(None)
        self.assertEqual(get_next(), False)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, newhash):
        newlist = hashmap()
        newlist = from_list(newlist, newhash)
        a = to_list(newlist)
        self.assertEqual(newhash, a)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, newlist):
        newhash = hashmap()
        newhash = from_list(newhash, newlist)
        self.assertEqual(len(newhash), newlist)


if __name__ == '__main__':
    unittest.main()