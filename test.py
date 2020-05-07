from linkedlist import Node
from linkedlist import LinkedList
from hashmap import Hashmap
import unittest

class Test_LinkedList(unittest.TestCase):
  def setUp(self):
    self.linkedlist = LinkedList()
  def tearDown(self):
    del self.linkedlist

class Test_LinkedList(Test_LinkedList):

  def test_init(self):
    self.assertEqual(self.linkedlist.head, None)

  def test_len(self):
    self.assertEqual(len(self.linkedlist), 0)

    for i in range(30):
      node = Node(i)
      self.linkedlist.insert(node)
    self.assertEqual(len(self.linkedlist), 30)

  def test_insert(self):
    node = Node(5)
    output = self.linkedlist.insert(node)
    self.assertEqual(repr(output), "<Node index: None data: 5>")
    for i in range(7):
      node = Node(i)
      output = self.linkedlist.insert(node)
    self.assertEqual(repr(output), "<Node index: None data: 5>")

  def test_remove(self):
    node = Node(10)
    outputEmpty = self.linkedlist.remove(node.data)
    self.assertEqual(outputEmpty, "Linked List is empty, value of: 10 is not here")
    # Does not Remove anything if does not exist in Linked List
    for i in range(10):
      node = Node(i)
      self.linkedlist.insert(node)
    outputNotHere = self.linkedlist.remove(11)
    self.assertEqual(outputNotHere,'Node is not here')

    # Removes correct element
    outputRemove = self.linkedlist.remove(5)
    self.assertEqual(outputRemove, 'Node with the value: 5 was removed from the LinkedList')

  def test_str(self):
    output = str(self.linkedlist)
    self.assertEqual(output, '<LinkedList: 0 nodes>')

  def test_repr(self):
    output = repr(self.linkedlist)
    self.assertEqual(output, 'LinkedList: Nodes: []')

class TestCaseHashMap(unittest.TestCase):
  def setUp(self):
    self.hashmap = Hashmap()
  def tearDown(self):
    del self.hashmap

class Test_Hashmap(TestCaseHashMap):
  def test_init(self):
    self.assertEqual(self.hashmap.length, 100)
    del self.hashmap
    self.hashmap = Hashmap(5)
    self.assertEqual(self.hashmap.length, 5)
    # Check that buckets are LinkedList Objects
    self.assertEqual(self.hashmap.buckets[3].head, None)

  def test_hash(self):
    # hashes to correct index
    index = self.hashmap.hash(1079)
    self.assertEqual(index, 80)

  def test_insert(self):
    # places into correct location in Hashmap
    node = Node(123)
    insertOutput = self.hashmap.insert(node)
    self.assertEqual(repr(insertOutput), '<Node index: 24 data: 123>')

  def test_remove(self):
    # does not remove from an empty List at specified index
    removeEmpty = self.hashmap.remove(5)
    self.assertEqual(removeEmpty, "Linked List is empty, value of: 5 is not here")

    # does not remove if it is not in List at specified index
    for i in range(10):
      node = Node(i)
      self.hashmap.insert(node)
    outputNotHere = self.hashmap.remove(505)
    self.assertEqual(outputNotHere,'Node is not here')

    outputRemove = self.hashmap.remove(5)
    self.assertEqual(outputRemove, 'Node with the value: 5 was removed from the LinkedList')

    node = Node(67)
    self.hashmap.insert(node)
    node = Node(76)
    self.hashmap.insert(node)
    outputRemove = self.hashmap.remove(76)
    self.assertEqual(outputRemove, 'Node with the value: 76 was removed from the LinkedList')

if __name__ == '__main__':
    unittest.main()
