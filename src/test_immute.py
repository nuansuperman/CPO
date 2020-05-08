from hash_immute import *
import unittest

class TestImmutable(unittest.TestCase):
    def test_insert(self):
        newhash = hashmap()
        insert(newhash, 1)
        self.assertEqual(to_list(newhash), [1])

    def test_size(self):
        newhash = hashmap()
        insert(newhash, 1)
        self.assertEqual(size(newhash), 1)
        insert(newhash, 2)
        self.assertEqual(size(newhash),2)
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


    def test_concat(self):
        newhash1 = hashmap()
        insert(newhash1, 2)
        insert(newhash1, 4)
        newhash2 = hashmap()
        insert(newhash2, 6)
        newhash3 = hashmap()
        insert(newhash3, 2)
        insert(newhash3, 4)
        insert(newhash3, 6)
        self.assertEqual(to_list(concat(newhash1,newhash2)), to_list(newhash3))

if __name__ == '__main__':
    unittest.main()