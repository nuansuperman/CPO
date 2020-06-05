import src.nfa_construction as construction
from src.nfa_construction import get_visualize


class Regex(object):
    def __init__(self, input_string, pattern_string):
        self.input_string = input_string
        self.pattern_string = pattern_string
        self.graph = None


    def match(self):
        pattern_string = self.pattern_string
        input_string = self.input_string
        nfa_machine = construction.pattern(pattern_string)
        self.graph = get_visualize(nfa_machine)
        return construction.match(input_string, nfa_machine)

    def matchAll(self):
        ins = self.input_string
        for i in range(len(self.input_string)):
            result = self.match()
            if result:
                break
            self.input_string = self.input_string[1:]
        if len(result) == 0:
            return "You should enter the correct expression"
        return "".join(result)


st = 'bbbbbscccccasbdzx'
pattern = '(\*?|b+)(xy|sc*)(asb|ebd)(dzx)'

regex = Regex(st, pattern)
result = regex.matchAll()
print(result)
print(regex.graph)
