class NFA:
    def __init__(self):
        """Creates a blank NFA"""
        self.alphabet = set()
        self.states = {0}
        self.transition_function = {}
        self.accept_states = set()
        self.in_states = {0}

    def add_state(self, state, accepts=False):
        self.states.add(state)

        if accepts:
            self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_states):
        self.transition_function[(from_state, symbol)] = to_states

        if symbol != "":
            self.alphabet.add(symbol)

    def feed_symbol(self, symbol):
        """
        Feeds a symbol into the NFA, calculating which states the
        NFA is now in, based on which states it used to be in
        """
        if self.is_dead():
            return
        new_states = set()

        for state in self.in_states:
            pair = (state, symbol)
            # check for a legal transition from the old state to a
            # new state, based on what symbol was fed in
            if pair in self.transition_function:
                new_states |= self.transition_function[pair]
        self.in_states = new_states
        self.feed_empty()

    def feed_symbols(self, symbols, return_if_dies=False):
        for symbol in symbols:
            self.feed_symbol(symbol)

            if return_if_dies and self.is_dead():
                return

    def feed_empty(self):
        """
        Continuously feeds empty strings into the NFA until they fail
        to cause any further state transitions
        """
        if self.is_dead():
            return
        old_states_len = None
        # set of states that will be fed the empty string on the next pass
        unproc_states = self.in_states
        first_run = True

        # keep feeding the empty string until no more new states are transitioned into
        while first_run or len(self.in_states) > old_states_len:
            old_states_len = len(self.in_states)
            # set of new states transitioned into after the empty string was fed
            new_states = set()

            # process each state in turn
            for state in unproc_states:
                pair = (state, "")

                # check if this state has a transition using the empty string
                # to another state
                if pair in self.transition_function:
                    # add the new state to a set to be added to self.in_states later
                    new_states |= self.transition_function[pair]

            # merge new states back into "in" states
            self.in_states |= new_states
            # all new states discovered will be fed the empty string on the next pass
            unproc_states = new_states
            first_run = False

    def is_accepting(self):
        #ds
        # accepts if we are in ANY accept states
        # ie. if in_states and accept_states share any states in common
        return len(self.in_states & self.accept_states) > 0

    def is_dead(self):
        return len(self.in_states) == 0

    def reset(self):
        self.in_states = {0}
        self.feed_empty()

    # def __str__(self):
    #     """
    #     String representation of this NFA.
    #     Useful for debugging.
    #     """
    #     return "NFA:\n" \
    #            "Alphabet: {}\n" \
    #            "States: {}\n" \
    #            "Transition Function: {}\n" \
    #            "Accept States: {}\n" \
    #            "In states: {}\n" \
    #            "Accepting: {}\n"\
    #         .format(self.alphabet,
    #                 self.states,
    #                 self.transition_function,
    #                 self.accept_states,
    #                 self.in_states,
    #                 "Yes" if self.is_accepting() else "No")

    def __eq__(self, other):
        """
        Checks if two NFAs are equal. Used for testing.
        """
        return self.states == other.states \
           and self.transition_function == other.transition_function \
           and self.accept_states == other.accept_states


