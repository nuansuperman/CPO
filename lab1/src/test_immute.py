import unittest
from hypothesis import given,settings
import hypothesis.strategies as st
from hash_immute import *


class TestNode(unittest.TestCase):
    def test_hash(self):
        node1 = Node(data=10)
        node2 = Node(data=15)
        self.assertEqual(hash(node1, 5), hash(node2, 5))

    def test_insert(self):
        buckets = [Node(0), Node(1), Node(2)]

        node1 = Node(data=3)
        node2 = Node(data=6)
        self.assertEqual(insert(node1, buckets), insert(node2, buckets))

    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(form(Node(1), Node(1,'a'))), 2)

    def test_remove(self):
        head = Node(1)
        head.next = Node(1,'a')
        head.next.next = Node(2, 'b')
        self.assertEqual(remove(form(Node(1), Node(1, 'a')), 'a'), Node(1, 'a'))

    def test_to_list(self):
        head = Node(1)
        node_1 = Node(1, 'a')
        node_2 = Node(1, 'b')
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
                node = Node(i[0], i[1])
                head = form(head, node)
                list.append([i[0], i[1]])
            list.reverse()
            self.assertEqual(to_list(head), list)

    def test_form(self):
        self.assertEqual(form(Node(1), Node(1, 'a')), Node(1, next= Node(1, 'a')))

    def test_head(self):
        self.assertEqual(head(Node(1,'a')), 'a')

    def test_tail(self):
        head = Node(1)
        node_1 = Node(1, 'a')
        node_2 = Node(1,'b')
        head.next = node_1
        node_1.next = node_2
        self.assertEqual(tail(node_2), None)
        self.assertEqual(tail(head), node_1)


    def test_mconcat(self):
        head1 = Node(1)
        node_1 = Node(1, 'a', None)
        head2 = Node(2)
        node_2 = Node(2, 'b', None)
        head1.next = node_1
        head2.next = node_2
        self.assertEqual(mconcat(head1,head2), Node(1,None,Node(1,'a',Node(2,'b',None))))

    def test_remove_hashmap(self):
        buckets = [
            Node(data=0),
            Node(data=1),
            Node(data=2),
        ]
        node1 = Node(data=2)
        node2 = Node(data=4)
        node3 = Node(data=6)
        node4 = Node(data=8)
        insert(node1, buckets)
        insert(node2, buckets)
        insert(node3, buckets)
        insert(node4, buckets)
        hash(node1, len(buckets))
        hash(node2, len(buckets))
        hash(node3, len(buckets))
        hash(node4, len(buckets))
        self.assertEqual(remove_hashmap(node1, buckets), 1)


    @given(st.lists(st.lists(st.integers(1,150),min_size=2,max_size=2),min_size=3))
    def test_from_list_to_list_equality(self,v):
        head = from_list(v)
        ans = to_list(head)
        self.assertEqual(ans, v)
        print('1>', ans)


    @given(st.lists(st.lists(st.integers(1,150),min_size=2,max_size=2),min_size=3))
    def test_monoid_identity(self, lst):
        a=from_list(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)


    @given(a=st.lists(st.lists(st.integers(1,15),min_size=2,max_size=2),min_size=3), b=st.lists(st.lists(st.integers(1,15),min_size=2,max_size=2),min_size=3), c=st.lists(st.lists(st.integers(1,15),min_size=2,max_size=2),min_size=3))
    def test_monoid_associativity(self, a, b, c):
        l1_1=from_list(a)
        l1_2=from_list(a)
        l2_1=from_list(b)
        l2_2=from_list(b)
        l3_1=from_list(c)
        l3_2=from_list(c)
        self.assertEqual(to_list(mconcat(mconcat(l1_1, l2_1), l3_1)),to_list(mconcat(l1_2, mconcat(l2_2, l3_2))))



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
