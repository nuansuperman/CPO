import unittest
from hypothesis import given,settings
import hypothesis.strategies as st
from src.hash_immute import *


class TestNode(unittest.TestCase):
    def test_hash(self):
        node1 = Node(None,10, None)
        node2 = Node(None,15, None)
        self.assertEqual(hash(node1, 5), hash(node2, 5))

    def test_insert(self):
        buckets = [Node(0,None,None), Node(1,None,None), Node(2,None,None)]

        node1 = Node(None,3, None)
        node2 = Node(None,6, None)
        self.assertEqual(insert(node1, buckets), insert(node2, buckets))

    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(form(Node(1, None, None), Node(1, 'a', None))), 2)

    def test_remove(self):
        head = Node(1, None, None)
        head.next = Node(1, 'a', None)
        head.next.next = Node(2, 'b', None)
        self.assertEqual(remove(form(Node(1, None, None), Node(1, 'a', None)), 'a'), Node(1, 'a', None))

    def test_to_list(self):
        head = Node(1, None, None)
        node_1 = Node(1, 'a', None)
        node_2 = Node(1, 'b', None)
        head.next = node_1
        node_1.next = node_2
        self.assertEqual(to_list(head), [[1, 'a'], [1, 'b']])

    def test_from_list(self):
        test_data = [
            [],
            [[None, 'a']],
            [[None, 'a'], [None, 'b']]
        ]

        for e in test_data:
            list = []
            head = Node()
            for i in e:
                node = Node(i[0], i[1], None)
                head = form(head, node)
                list.append([i[0], i[1]])
            list.reverse()
            self.assertEqual(to_list(head), list)

    def test_form(self):
        self.assertEqual(form(Node(1, None, None), Node(1, 'a', None)), Node(1, None, Node(1, 'a', None)))

    def test_head(self):
        self.assertEqual(head(Node(1,'a',None)), 'a')

    def test_tail(self):
        head = Node(1, None, None)
        node_1 = Node(1, 'a', None)
        node_2 = Node(1, 'b', None)
        head.next = node_1
        node_1.next = node_2
        self.assertEqual(tail(node_2), None)
        self.assertEqual(tail(head), node_1)


    def test_mconcat(self):
        head1 = Node(1, None, None)
        node_1 = Node(1, 'a', None)
        head2 = Node(2, None, None)
        node_2 = Node(2, 'b', None)
        head1.next = node_1
        head2.next = node_2
        self.assertEqual(mconcat(head1,head2), Node(1,None,Node(1,'a',Node(2,'b',None))))

    def test_remove_hashmap(self):
        buckets = [
            Node(None, 0, None),
            Node(None, 1, None),
            Node(None, 2, None),
        ]
        node1 = Node(None,2, None)
        node2 = Node(None,4, None)
        node3 = Node(None,6, None)
        node4 = Node(None,8, None)
        insert(node1, buckets)
        insert(node2, buckets)
        insert(node3, buckets)
        insert(node4, buckets)
        hash(node1, len(buckets))
        hash(node2, len(buckets))
        hash(node3, len(buckets))
        hash(node4, len(buckets))
        self.assertEqual(remove_hashmap(node1, buckets), 1)

    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers())
    def test_from_list_to_list_equality(self, a, b):
        v= [[a,b]]
        head = from_list(v)

        ans = to_list(head)
        self.assertEqual(ans, v)

    @given(a=st.integers(), b=st.integers())
    def test_monoid_identity(self, a, b):
        node = Node(a, b, None)
        head1 = Node()
        head2 = Node()
        head2.next = node
        self.assertEqual(mconcat(head1, head2), head2)
        self.assertEqual(mconcat(head2, head1), head2)

    def test_iter(self):
        x = [[1,1], [2,2], [3,3]]
        head = from_list(x)
        tmp = []
        try:
            get_next = iterator(head)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(head), tmp)


if __name__ == '__main__':
    unittest.main()
