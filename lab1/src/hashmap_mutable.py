from linkedlist_mutable import LinkedList
from linkedlist_mutable import Node
class Hashmap(object):

  # buckets = list of Linked List Objects
  # length = length of the bucket list
  def __init__(self, length=100):
    listBuckets = []
    for i in range(length):
      listBuckets.append(LinkedList())
    self.buckets = listBuckets
    self.length = length

  def hash(self, data):
    key = data % self.length+1
    return key

  def insert(self, node):
    key = self.hash(node.data)
    node.key = key
    insertOutput = self.buckets[key].insert(node)
    return insertOutput

  def remove(self, data):
    key = self.hash(data)
    removedOutput = self.buckets[key].remove(data)
    return removedOutput

  def to_list(self,key):
    to_listOutput = self.buckets[key].to_list()
    return to_listOutput

  def from_list(self,key,lst):
    from_listOutput = self.buckets[key].to_list()
    return from_listOutput

  def find_uneven(self,key):
    find_unevenoutput=self.buckets[key].find_uneven()
    return find_unevenoutput
  def filter_uneven(self,key):
    filter_unevenoutput = self.buckets[key].filter_uneven()
    return filter_unevenoutput

  def map(self,key,f):
    mapOutput = self.buckets[key].map(f)
    return mapOutput

  def reduce(self, key,f, initial_state):
    reduceOutput = self.buckets[key].reduce(f,initial_state)
    return reduceOutput

  def __repr__(self):
        return '<Hashmap %r>' % self.buckets



