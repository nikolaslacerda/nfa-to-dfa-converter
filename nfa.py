from dfa import DFA


class NFA:

    def __init__(self):
        self.name = ''
        self.states = []
        self.initial_state = ''
        self.final_states = []
        self.symbols = []
        self.transitions = {}

    def __str__(self):
        return f'Name: {self.name} \
                \nStates: {self.states} \
                \nSymbols: {self.symbols} \
                \nInitial State: {self.initial_state} \
                \nFinal States: {self.final_states} \
                \nTransitions: {self.transitions}'

    def convertToAFD(self):
        dfa = {}
        missing = [(self.initial_state,)]
        check = []

        while len(missing) != 0:
            actual_state = missing[0]
            check.append(actual_state)
            if len(actual_state) > 1:
                actual_list = []
                for symbol in self.symbols:
                    for state in actual_state:
                        try:
                            a = self.transitions[(state, symbol)]
                        except:
                            a = None

                        if a is not None:
                            for b in a:
                                if b not in actual_list:
                                    actual_list.append(b)
                    t = tuple(actual_list)
                    if t in check:
                        pass
                    else:
                        if t not in missing:
                            missing.append(t)

                    dfa.update({(actual_state, symbol): t})
                    actual_list = []
                missing.pop(0)

            else:
                for symbol in self.symbols:
                    for state in actual_state:
                        try:
                            actual_transition = self.transitions[(state, symbol)]
                        except:
                            actual_transition = None

                    if actual_transition is not None:
                        actual_transition_state = tuple(actual_transition)
                        dfa.update({(state, symbol): tuple(actual_transition)})

                        if actual_transition_state in check:
                            pass
                        else:
                            if actual_transition_state not in missing:
                                missing.append(actual_transition_state)
                missing.pop(0)

        dfa_convert = {}
        new_finals = []

        for k_state in dfa:
            control = False

            if len(k_state[0]) > 1:

                for item in k_state[0]:
                    if item in self.final_states:
                        control = True
            else:
                if k_state[0] in self.final_states:
                    control = True

            if control:
                if k_state[0] not in new_finals:
                    if type(k_state[0]) == tuple:
                        new_finals.append(k_state[0])

        for k, v in dfa.items():
            if len(k[0]) > 1:
                dfa_convert.update({(convertTuple(k[0]), k[1]): convertTuple(v)})
            else:
                dfa_convert.update({(k[0], k[1]): convertTuple(v)})

        my_dfa = DFA()
        my_dfa.name = self.name + "(AFD)"
        my_dfa.initial_state = self.initial_state
        my_dfa.symbols = self.symbols

        for final_state in new_finals:
            if type(final_state) == tuple:
                my_dfa.final_states.append(convertTuple(final_state))
            else:
                my_dfa.final_states.append(final_state)

        my_dfa.transitions = dfa_convert

        for state in dfa_convert:
            if state[0] not in my_dfa.states:
                my_dfa.states.append(state[0])

        return my_dfa


def convertTuple(tup):
    string_tuple = ''.join(tup)
    return string_tuple
