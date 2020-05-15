from hashmap_mutable import Hashmap


class hashmap(object):
    def __init__(self,datas=None):
        self.hashtable = [[None for i in range(1)] for j in range(15)]
        self.length = 15
        if datas is not None:
            for data in datas:
                insert(self, data)


def insert(n, value):
    key = value % n.length
    if n.hashtable[key][0] is None:
        n.hashtable[key][0] =value
    else:
        flag = 1
        while n.hashtable[key][flag] != None &n.hashtable[key][flag] != value:
            flag = flag+1
        n.hashtable[key][flag] = value


def size(n):
    s = 0
    if n is None:
        return 0
    else:
        for i in range(n.length):
            for j in range(len(n.hashtable[i])):
                if n.hashtable[i][j] != None:
                    s += 1
        return s



# conversion to python lists
def to_list(n):
    newlist = []
    for i in range(n.length):
        for j in range(len(n.hashtable[i])):
            if n.hashtable[i][j] != None:
                newlist.append(n.hashtable[i][j])
    return newlist


#  conversion from python lists
def from_list(n, list):
    newtable = list
    for i in range(len(newtable)):
        insert(n, newtable[i])


def map(n,f):
    for i in range(n.length):
        for j in range(len(n.hashtable[i])):
            if n.hashtable[i][j] != None:
                n.hashtable[i][j] = f(n.hashtable[i][j])


# process structure elements to build a return value by specific functions
def reduce(n,m):
    sum =0
    a = 0
    for i in range(n.length):
        for j in range(len(n.hashtable[i])):
            if n.hashtable[i][j] != None:
                sum += n.hashtable[i][j]
                a +=1
    if (m == 'sum'):
        return sum
    elif (m == 'table'):
        return sum/a


def mconcat(n,m):
    res = to_list(m)
    for data in res:
        insert(n, data)
    return n


# remove an element
def remove(n,value):
    key =value %n.length
    if n.hashtable[key][0] is None:
        return false
    else:
        for i in range(len(n.hashtable[key])):
            if n.hashtable[key][i] == value:
                n.hashtable[key][i] == n.hashtable[key][len(n.hashtable[key])-1]
                n.hashtable[key].pop()
                break
            while i == len(n.hashtable[key]) -1:
                return false


def mempty():
    return None


#  find element by specific predicate
def find_iseven(n):
    newlist1 = []
    newlist2 = []
    for i in range(n.length):
        for j in range(len(n.hashtable[i])):
            if n.hashtable[i][j] != None:
                newlist1.append(n.hashtable[i][j])
    for m in range(len(newlist1)):
        if newlist1[m] % 2 == 1:
            newlist2.append(newlist1[m])
    return newlist2


#  filter data structure by specific predicate
def filter_iseven(n):
    newlist1 = []
    newlist2 = []
    for i in range(n.length):
        for j in range(len(n.hashtable[i])):
            if n.hashtable[i][j] != None:
                newlist1.append(n.hashtable[i][j])
    for m in range(len(newlist1)):
        if newlist1[m] % 2 == 1:
            newlist2.append(newlist1[m])
    return newlist2


def iterator(n):
    if n is not None:
        cur = []
        for i in range(n.length):
            for j in range(len(n.hashtable[i])):
                if n.hashtable[i][j] != None:
                    cur.append(n.hashtable[i][j])
        b = iter(cur)
    else:
        b = None

    def get_next():
        if b is None:
            return False
        else:
            return next(b)
    return get_next





