from src.nfa_morphology import *
from graphviz import Digraph
# Edges correspond to epsilon
EPSILON = -1
# Edges correspond to character sets
CS = -2
# This node has no outgoing edges
EMPTY = -3
# Edges correspond to a number of {}
BOUND = -4
ASCII_COUNT = 127
groupCount = 0
# NFA
class Nfa(object):
    # Node number
    STATE_NUM = 0

    def __init__(self):
        self.edge = EPSILON     # Record the input corresponding to the conversion edge
        self.next1 = None       # The next state of the jump can be empty
        self.next2 = None       # The second state of a jump.
        self.flag = False       # Whether the node has been accessed for node printing
        self.input_set = set()
        self.set_state_num()
        # self.value = None

    def set_state_num(self):
        self.state_num = Nfa.STATE_NUM
        Nfa.STATE_NUM = Nfa.STATE_NUM + 1

    def set_input_set(self):
        self.input_set = set()
        for i in range(ASCII_COUNT):
            self.input_set.add(chr(i))


class NfaPair(object):
    def __init__(self):
        self.first_node = None
        self.last_node = None


morphology = None


def move(input_set, ch):
    out_set = []
    for nfa in input_set:
        if nfa.edge == ch or (nfa.edge == CS and ch in nfa.input_set):
            out_set.append(nfa.next1)

    return out_set


# Match success
def has_accepted_state(nfa_set):
    for nfa in nfa_set:
        if nfa.next1 is None and nfa.next2 is None:
            return True


def closure(input_set):
    if len(input_set) <= 0:
        return None

    nfa_stack = []
    for i in input_set:
        nfa_stack.append(i)

    while len(nfa_stack) > 0:
        nfa = nfa_stack.pop()
        next_first = nfa.next1
        next_second = nfa.next2
        if next_first is not None and nfa.edge == EPSILON:
            if next_first not in input_set:
                input_set.append(next_first)
                nfa_stack.append(next_first)

        if next_second is not None and nfa.edge == EPSILON:
            if next_second not in input_set:
                input_set.append(next_second)
                nfa_stack.append(next_second)

    return input_set


def pattern(pattern_string):
    global morphology
    morphology = Morphology(pattern_string)
    morphology.advance()
    nfa_pair = NfaPair()
    group(nfa_pair)

    return nfa_pair.first_node


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
def factor_connect(pair_out):
    if is_connect(morphology.current_state):
        factor(pair_out)

    while is_connect(morphology.current_state):
        pair = NfaPair()
        factor(pair)
        pair_out.last_node.next1 = pair.first_node
        pair_out.last_node = pair.last_node

    return True


def is_connect(state):
    nc = [
        Symbol.OPEN_PAREN,
        Symbol.CLOSE_PAREN,
        Symbol.AT_EOL,
        Symbol.EOS,
        Symbol.CLOSURE,
        Symbol.PLUS_CLOSE,
        Symbol.CS_END,
        Symbol.AT_BOL,
        Symbol.OR,
    ]
    return state not in nc


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


# factor * + ? closure
def factor(pair_out):
    term(pair_out)
    if morphology.match(Symbol.CLOSURE):
        nfa_star_closure(pair_out)
    elif morphology.match(Symbol.PLUS_CLOSE):
        nfa_plus_closure(pair_out)
    elif morphology.match(Symbol.OPTIONAL):
        nfa_option_closure(pair_out)


# factor connect
def factor_connect(pair_out):
    if is_connect(morphology.current_state):
        factor(pair_out)

    while is_connect(morphology.current_state):
        pair = NfaPair()
        factor(pair)
        pair_out.last_node.next1 = pair.first_node
        pair_out.last_node = pair.last_node

    return True


def exprToUpper(pair_out):
    factor_connect(pair_out)
    pair = NfaPair()

    while morphology.match(Symbol.OR):
        morphology.advance()
        factor_connect(pair)
        begin = Nfa()
        begin.next1 = pair.first_node
        begin.next2 = pair_out.first_node
        pair_out.first_node = begin

        end = Nfa()
        pair.last_node.next1 = end
        pair_out.last_node.next2 = end
        pair_out.last_node = end

    return True


def get_visualize( first_node):
    dot = Digraph(comment='The Test Table')
    res = []
    res.append("digraph G {")
    res.append(" rankdir=LR;")

    def visualize(first_node,res):
        next1 = first_node.next1 is not None
        next2 = first_node.next2 is not None

        if next1:
            res.append(" {} -> {} [label=\"{}\"];".format(first_node.state_num,first_node.next1.state_num,first_node.edge))
        if next2:
            res.append(" {} -> {} [label=\"{}\"];".format(first_node.state_num,first_node.next2.state_num, first_node.edge))
        first_node.flag = True
        if first_node.next1 is not None and not first_node.next1.flag:
            visualize(first_node.next1, res)
        if first_node.next2 is not None and not first_node.next2.flag:
            visualize(first_node.next2, res)
        return "\n".join(res)

    return visualize(first_node, res)+"\n}"


def match(input_string, nfa_machine):
    ls = []
    first_node = nfa_machine

    current_nfa_set = [first_node]
    next_nfa_set = closure(current_nfa_set)

    for i, str in enumerate(input_string):
        current_nfa_set = move(next_nfa_set, str)
        next_nfa_set = closure(current_nfa_set)
        if next_nfa_set is None:
            return ls
        else:
            ls.append(str)

        if has_accepted_state(next_nfa_set) and i == len(input_string) - 1:
            return ls

    return None


def group(pair_out):
    global groupCount
    if morphology.match(Symbol.OPEN_PAREN):
        groupCount = groupCount+1
        morphology.advance()
        exprToUpper(pair_out)
        if morphology.match(Symbol.CLOSE_PAREN):
            morphology.advance()
    elif morphology.match(Symbol.EOS):
        return False
    else:
        exprToUpper(pair_out)

    while True:
        pair = NfaPair()

        if morphology.match(Symbol.OPEN_PAREN):
            groupCount = groupCount + 1
            morphology.advance()
            exprToUpper(pair)
            pair_out.last_node.next1 = pair.first_node
            pair_out.last_node = pair.last_node
            if morphology.match(Symbol.CLOSE_PAREN):
                morphology.advance()
        elif morphology.match(Symbol.EOS):
            return False
        elif morphology.match(Symbol.AT_BOL):
            morphology.advance()
            group(pair_out)
        elif morphology.match(Symbol.AT_EOL):
            return False
        else:
            exprToUpper(pair)
            pair_out.last_node.next1 = pair.first_node
            pair_out.last_node = pair.last_node
