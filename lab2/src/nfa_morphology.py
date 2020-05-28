from enum import Enum
# state
class Symbol(Enum):
    EOS = 0
    # rgx's end

    ANY = 1
    # .

    AT_BOL = 2
    # ^

    AT_EOL = 3
    # $

    CCL_END = 4
    # ]

    CCL_START = 5
    # [

    CLOSE_CURLY = 6
    # }

    CLOSE_PAREN = 7
    # )

    CLOSURE = 8
    # +

    DASH = 9
    # -

    END_OF_INPUT = 10
    #

    L = 11
    # Character constants

    OPEN_CURLY = 12
    # {

    OPEN_PAREN = 13
    # (

    OPTIONAL = 14
    # ?

    OR = 15
    # |

    PLUS_CLOSE = 16
    # +

    COMMA = 17
    # ,

Symbols = {
    '.': Symbol.ANY,
    '^': Symbol.AT_BOL,
    '$': Symbol.AT_EOL,
    ')': Symbol.CLOSE_PAREN,
    '*': Symbol.CLOSURE,
    '(': Symbol.OPEN_PAREN,
    '|': Symbol.OR,
    '+': Symbol.PLUS_CLOSE,
}

# morphology analyzer
class Morphology(object):
    def __init__(self, pattern):
        self.pattern = pattern
        self.morcontent = ''
        self.position = 0
        self.isescape = False
        self.current_state = None

    def advance(self):
        position = self.position
        pattern = self.pattern
        if position > len(pattern) - 1:
            self.current_state = Symbol.EOS
            return Symbol.EOS

        # Handle escape characters
        character = self.morcontent = pattern[position]
        if character == '\\':
            self.isescape = not self.isescape
            self.position = self.position + 1
            self.current_state = self.handleesc()
        else:
            self.current_state = self.semantic(character)

        return self.current_state

    def handleesc(self):
        expr = self.pattern.lower()
        position = self.position
        ev = {
            '\0': '\\',
            'n': '\n',
            'f': '\f',
            'b': '\b',
            't': '\t',
            's': ' ',
            'e': '\033',
        }
        rval = ev.get(expr[position])
        if rval is None:
            if expr[position] == '^':
                rval = self.tip()
            else:
                rval = expr[position]
        self.position = self.position + 1
        self.morcontent = rval
        return Symbol.L

    def semantic(self, character):
        self.position = self.position + 1
        return Symbols.get(character, Symbol.L)

    def tip(self):
        self.position = self.position + 1
        return self.pattern[self.position] - '@'

    def match(self, state):
        return self.current_state == state