from linkedlist_mutable import LinkedList

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

  def __repr__(self):
        return '<Hashmap %r>' % self.buckets
