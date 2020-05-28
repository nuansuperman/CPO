class Node(object):
  # key = index in the Hashmap
  # data = data of Node (integer)
  def __init__(self, data,next=None):
    self.key = None
    self.data = data
    self.next = next

  def __repr__(self):
    if self.key != None:
      return "<Node key: %d data: %d>" % (self.key, self.data)
    else:
      return "<Node key: %s data: %d>" % (self.key, self.data)

# A Linked List of Node Objects
class LinkedList(object):
  # head:pointer to the first Node
  # current:pointer to current Node in list, used when Traversing Linked List
  def __init__(self):
    self.head = None
    self.current = None

  def get_length(self):
    length = 0
    if self.head is None:
      return length
    else:
      length = 1
      self.current = self.head
      while self.current.next != None:
        self.current = self.current.next
        length = length + 1
      return length

  def insert(self, node):
    self.current = self.head
    # Add to front of List if it is Empty
    if self.head is None:

      self.head = node
      return self.head
    else:
      while self.current.next != None:
        self.current = self.current.next
      self.current.next = node
    return self.current

  def __len__(self):
    return self.get_length()

  def __str__(self):
    return '<LinkedList: %d nodes>' % self.get_length()

  def __repr__(self):
    nodes = []
    node = self.head
    while not node is None:
      nodes.append(repr(node))
      node = node.next
    return 'LinkedList: Nodes: %r' % nodes

  def to_list(self):
    res = []
    node = self.head
    while not node is None:
      res.append(node.data)
      node = node.next
    return res

  def from_list(self,lst):
    if len(lst) == 0:
      self.head = None
      return
    head = None
    for e in reversed(lst):
      head = Node(e,head)
      self.head = head

  def find_uneven(self):
    res = []
    node = self.head
    while not node is None:
      if node.data%2==1:
        res.append(node.data)
        node = node.next
      else:
        node=node.next
    return res

  def filter_uneven(self):
    previous = None
    self.current = self.head
    if self.current is None:
      return 'Linked List is empty'
    else:
      while self.current != None:
        if self.current.data %2==1:
          # Remove the value from the Linked List
          if len(self) is 1:
            previous = None
            self.current = None
            self.head = None
          else:
            previous.next = self.current.next
            self.current = None
          return 'Uneven was removed from the LinkedList'
        else:
          previous = self.current
          self.current = self.current.next
      return 'No uneven is  in LinkedList'




  def map(self, f):
      cur = self.head
      while cur is not None:
        cur.data = f(cur.data)
        cur = cur.next


  def reduce(self, f, initial_state):
      state = initial_state
      cur = self.head
      while cur is not None:
        state = f(state, cur.data)
        cur = cur.next
      return state

  def remove(self, value):
    previous = None
    self.current = self.head
    # Attempted to Remove from Empty Linked List
    if self.current is None:
      return 'Linked List is empty, value of: %d is not here' % value
    else:
      while self.current != None:
        if self.current.data == value:
          # Remove the value from the Linked List
          if len(self) is 1:
            previous = None
            self.current = None
            self.head = None
          else:
            previous.next = self.current.next
            self.current = None
          return 'Node with the value: %d was removed from the LinkedList' % value
        else:
          previous = self.current
          self.current = self.current.next
      return 'Node is not in LinkedList'

def mempty():
 return None

def mconcat(a,b):
  if a==None:
    return b
  if b==None:
    return a
  b_lst=b.to_list()
  a_lst=a.to_list()
  for i in b_lst:
    a_lst.append(i)
  a.from_list(a_lst)
  return a


# a=LinkedList()
# a.from_list([1,5,9])
# b=LinkedList()
# b.from_list([2,4,6])
# a.insert(Node(13))
# print(type(mconcat(a,b)))



