def hash(Node, length):
    key = Node.data % length
    Node.key = key
    return key


def insert(node, buckets):
    key = hash(node, len(buckets))
    node.key = key
    insert_node = form(buckets[key],node)
    if insert_node:
        return 1
    else:
        return 0


def size(node):
    if node is None:
        return 0
    else:
        return 1 + size(node.next)


# remove hashNode
def remove_hashmap(node, buckets):
    key = hash(node, len(buckets))
    remove_node = remove(buckets[key], node.data)
    if remove_node:
        return 1
    else:
        return 0


def to_list(head):
    list = []
    # list_keys = []
    res = head.next
    while res is not None:
        list.append([res.key, res.data])
        res = res.next
    return list


def from_list(nodes):
    head = Node(None, None, None)
    root = None
    if len(nodes) == 0:
        return head
    for d in reversed(nodes):
        root = Node(d[0], d[1], root)
    head.next = root
    return head


# add a new Node to head of the list
def form(head, node):
    node.next = head.next
    head.next = node
    return head


#  delete the data of data of the list, return the Node that we cancel
def remove(head, data):
    res = head.next
    p = head

    while res is not None:
        if res.data == data:
            cancel = res
            p.next = res.next
            res = res.next
        else:
            res =res.next
    return cancel


def head(node):
    assert type(node) is Node
    return node.data


def tail(node):
    assert type(node) is Node
    return node.next


def mempty():
    return None


def mconcat(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.next is None:
        return head2
    if head2.next is None:
        return head1

    else:
        res = head1
        while res.next is not None:
            res = res.next
        res.next = head2.next
    return head1


def iterator(head):
    if head is not None:
        res = head.next

        def foo():
            nonlocal res
            if res is None:
                raise StopIteration
            tmp = [res.key, res.data]
            res = res.next
            return tmp

        return foo
    else:
        raise StopIteration


class Node(object):
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next

    def __repr__(self):
        if self.key != None:
            return "<Node key: %d data: %d>" % (self.key, self.data)
        else:
            return "<Node key: %s data: %d>" % (self.key, self.data)

    def __str__(self):
        if type(self.next) is Node:
            return "key: data : next".format(self.key, self.data, self.next)
        return "key : data".format(self.key,self.data)

    def __eq__(self, other):
        if other is None:
            return False
        if self.data != other.data:
            return False
        if self.key != other.key:
            return False
        return self.next == other.next
