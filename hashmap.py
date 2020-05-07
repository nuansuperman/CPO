from linkedlist import LinkedList

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
    index = data % self.length+1
    return index

  def insert(self, node):
    index = self.hash(node.data)
    node.index = index
    insertOutput = self.buckets[index].insert(node)
    return insertOutput

  def remove(self, data):
    index = self.hash(data)
    removedOutput = self.buckets[index].remove(data)
    return removedOutput

  def __repr__(self):
        return '<Hashmap %r>' % self.buckets
