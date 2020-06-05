from enum import Enum
# state
class Symbol(Enum):
    ANY = 0
    # .

    EOS = 1
    # rgx's end

    AT_EOL = 2
    # $

    AT_BOL = 3
    # ^

    CS_begin = 4
    # [

    CS_END = 5
    # ]

    OPEN_CURLY = 6
    # {

    CLOSE_CURLY = 7
    # }

    OPEN_PAREN = 8
    # (

    CLOSE_PAREN = 9
    # )

    CLOSURE = 10
    # +
    DASH =11
    END_OF_INPUT = 12
    L = 13
    # Character constants

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


# Lexical analyzer
class Morphology(object):
    def __init__(self, pattern):
        self.position = 0
        self.pattern = pattern
        self.morcontent = ''
        self.current_state = None
        self.sawEsc = False

    def advance(self):
        position = self.position
        pattern = self.pattern
        if position > len(pattern) - 1:
            self.current_state = Symbol.EOS
            return Symbol.EOS

        # Handle escape characters
        character = self.morcontent = pattern[position]

        if character == '\\':
            self.sawEsc = not self.sawEsc
            self.position = self.position + 1
            self.current_state = self.handleesc()
        else:
            self.current_state = self.semantic(character)

        return self.current_state

    def tip(self):
        self.position = self.position + 1
        return self.pattern[self.position] - '@'

    def semantic(self, character):
        self.position = self.position + 1
        return Symbols.get(character, Symbol.L)

    def match(self, state):
        return self.current_state == state

    # When the transfer character '\ 'exists,
    # it must be interpreted with the character or string that follows it
    def handleesc(self):
        exprToUpper = self.pattern.lower()
        position = self.position
        eTU = {
            '\0': '\\',
            'b': '\b',  #backspace
            'f': '\f',  #formfeed
            'n': '\n',  #newline
            's': ' ',   # space
            't': '\t',  #tab
            'e': '\033',#ASCII ESC ('\033')
        }
        rval = eTU.get(exprToUpper[position])
        if rval is None:
            if exprToUpper[position] == '^':
                rval = self.tip()
            else:
                rval = exprToUpper[position]
        self.position = self.position + 1
        self.morcontent = rval
        return Symbol.L
