from src.nfa_construction import *
from graphviz import Digraph

#epsilon edge
EPSILON = -1
# Edges correspond to character sets
CS = -2
#The corresponding node has two outgoing epsilon sides
EMPTY = -3
ASCII_COUNT = 127

# NFA
class Nfa(object):
    # the number of Node
    STATENUM = 0

    def __init__(self):
        self.edge = EPSILON
        self.next1 = None
        self.next2 = None
        self.input_set = set()
        self.set_state_num()
        self.flag = False

    def set_state_num(self):
        self.state_num = Nfa.STATENUM
        Nfa.STATENUM = Nfa.STATENUM + 1

    def set_input_set(self):
        self.input_set = set()
        for i in range(ASCII_COUNT):
            self.input_set.add(chr(i))


class NfaPair(object):
    def __init__(self):
        self.first_node = None
        self.last_node = None


# Visualization as a finite state machine
def get_visualize(first_node):
    dot = Digraph(comment='Visualization table')
    cur = []
    cur.append("digraph G :")
    def visualize(first_node, cur):
        next1 = first_node.next1 is not None
        next2 = first_node.next2 is not None

        if next1:
            cur.append(" {} -> {} [label=\"{}\"];".format(first_node.state_num, first_node.next1.state_num, first_node.edge))
        if next2:
            cur.append(" {} -> {} [label=\"{}\"];".format(first_node.state_num, first_node.next2.state_num, first_node.edge))
        first_node.flag = True
        if first_node.next1 is not None and not first_node.next1.flag:
            visualize(first_node.next1, cur)
        if first_node.next2 is not None and not first_node.next2.flag:
            visualize(first_node.next2, cur)
        return "\n".join(cur)

    return visualize(first_node, cur)+"\n}"


morphology = None


def pattern(pattern_string):
    global morphology
    morphology = Morphology(pattern_string)
    morphology.advance()
    nfa_pair = NfaPair()
    # group(nfa_pair)    # ???gai sub

    return nfa_pair.first_node


# use Bottom-up method
# # Matches. a (single character) []
def term(pair_out):
    if morphology.match(Symbol.L):
        nfa_single(pair_out)
    elif morphology.match(Symbol.ANY):
        nfa_dot(pair_out)


# Match a single character
def nfa_single(pair_out):
    if not morphology.match(Symbol.L):
        return False

    begin = pair_out.first_node = Nfa()
    pair_out.last_node = pair_out.first_node.next1 = Nfa()
    begin.edge = morphology.morcontent
    morphology.advance()
    return True


# . Matches any single character
def nfa_dot(pair_out):
    if not morphology.match(Symbol.ANY):
        return False

    begin = pair_out.first_node = Nfa()
    pair_out.last_node = pair_out.first_node.next1 = Nfa()
    begin.edge = CS
    begin.set_input_set()

    morphology.advance()
    return False


# factor connect
def factor_conn(pair_out):
    if is_conn(morphology.current_state):
        factor(pair_out)

    while is_conn(morphology.current_state):
        pair = NfaPair()
        factor(pair)
        pair_out.last_node.next1 = pair.first_node
        pair_out.last_node = pair.last_node

    return True


def is_conn(state):
    condition = [
        Symbol.OPEN_PAREN,
        Symbol.CLOSE_PAREN,
        Symbol.AT_EOL,
        Symbol.EOS,
        Symbol.CLOSURE,
        Symbol.PLUS_CLOSE,
        Symbol.CCL_END,
        Symbol.AT_BOL,
        Symbol.OR,
    ]
    return state not in condition



# factor * + ? closure
def factor(pair_out):
    term(pair_out)
    if morphology.match(Symbol.CLOSURE):
        nfa_star_closure(pair_out)
    elif morphology.match(Symbol.PLUS_CLOSE):
        nfa_plus_closure(pair_out)
    elif morphology.match(Symbol.OPTIONAL):
        nfa_option_closure(pair_out)


# * closure operations
def nfa_star_closure(pair_out):
    if not morphology.match(Symbol.CLOSURE):
        return False
    begin = Nfa()
    end = Nfa()
    begin.next1 = pair_out.first_node
    begin.next2 = end

    pair_out.last_node.next1 = pair_out.first_node
    pair_out.last_node.next2 = end

    pair_out.first_node = begin
    pair_out.last_node = end

    morphology.advance()
    return True


# + is closure
def nfa_plus_closure(pair_out):
    if not morphology.match(Symbol.PLUS_CLOSE):
        return False
    begin = Nfa()
    end = Nfa()
    begin.next1 = pair_out.first_node

    pair_out.last_node.next1 = pair_out.first_node
    pair_out.last_node.next2 = end

    pair_out.first_node = begin
    pair_out.last_node = end

    morphology.advance()
    return True

# ?
def nfa_option_closure(pair_out):
    if not morphology.match(Symbol.OPTIONAL):
        return False
    begin = Nfa()
    end = Nfa()

    begin.next1 = pair_out.first_node
    begin.next2 = end
    pair_out.last_node.next1 = end

    pair_out.first_node = begin
    pair_out.last_node = end

    morphology.advance()
    return True


def expr(pair_out):
    factor_conn(pair_out)
    pair = NfaPair()

    while morphology.match(Symbol.OR):
        morphology.advance()
        factor_conn(pair)
        begin = Nfa()
        begin.next1 = pair.first_node
        begin.next2 = pair_out.first_node
        pair_out.first_node = begin

        end = Nfa()
        pair.last_node.next1 = end
        pair_out.last_node.next2 = end
        pair_out.last_node = end

    return True

'''
def group(pair_out):
    global groupCount
    if morphology.match(Symbol.OPEN_PAREN):
        groupCount = groupCount+1
        morphology.advance()
        expr(pair_out)
        if morphology.match(Symbol.CLOSE_PAREN):
            morphology.advance()
    elif morphology.match(Symbol.EOS):
        return False
    else:
        expr(pair_out)

    while True:
        pair = NfaPair()
        if morphology.match(Symbol.OPEN_PAREN):
            groupCount = groupCount + 1
            morphology.advance()
            expr(pair)
            pair_out.last_node.next1 = pair.first_node
            pair_out.last_node = pair.last_node
            if morphology.match(Symbol.CLOSE_PAREN):
                morphology.advance()
        elif morphology.match(Symbol.EOS):
            return False
        else:
            expr(pair)
            pair_out.last_node.next1 = pair.first_node
            pair_out.last_node = pair.last_node
'''


def match(in_string, nfa_machine):
    lst = []
    first_node = nfa_machine

    current_nfa_set = [first_node]
    next_nfa_set = closure(current_nfa_set)

    for i, str in enumerate(in_string):
        current_nfa_set = move(next_nfa_set, str)
        next_nfa_set = closure(current_nfa_set)

        if next_nfa_set is None:
            return None
        else:
            lst.append(str)

        if accepted_state(next_nfa_set) and i == len(in_string) - 1:
            return lst

    return None
'''
def match2(in_string, nfa_machine,groupID):
    ls = []
    first_node = nfa_machine
    current_nfa_set = [first_node]
    next_nfa_set = closure(current_nfa_set)

    for i, ch in enumerate(in_string):
        current_nfa_set = move(next_nfa_set, ch)
        next_nfa_set = closure(current_nfa_set)

        if next_nfa_set is None:
            return None
        elif groupID==0:
            ls.append(ch)
        elif ( len(current_nfa_set)!=0 and current_nfa_set[0].groupID==groupID):
            ls.append(ch)

        if accepted_state(next_nfa_set) and i == len(in_string) - 1:
            return ls

    return None
'''


def closure(input_set):
    if len(input_set) <= 0:
        return None

    stack = []
    for i in input_set:
        stack.append(i)

    while len(stack) > 0:
        nfa = stack.pop()
        next1 = nfa.next1
        next2 = nfa.next2
        if next1 is not None and nfa.edge == EPSILON:
            if next1 not in input_set:
                input_set.append(next1)
                stack.append(next1)

        if next2 is not None and nfa.edge == EPSILON:
            if next2 not in input_set:
                input_set.append(next2)
                stack.append(next2)

    return input_set


def move(input_set, str):
    output_set = []
    for nfa in input_set:
        if nfa.edge == str or (nfa.edge == CS and str in nfa.input_set):
            output_set.append(nfa.next1)

    return output_set

# Match success
def accepted_state(nfa_set):
    for nfa in nfa_set:
        if nfa.next1 is None and nfa.next2 is None:
            return True

