class DFA:

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

    def getNextState(self, transition):
        return self.transitions[transition]

    def accept(self, word):
        actual_state = self.initial_state
        characters_of_word = list(word)

        for character in characters_of_word:

            try:
                new_state = self.getNextState((actual_state, character))
            except:
                new_state = None

            if new_state is None:
                return 'Reject'

            actual_state = new_state

        if actual_state in self.final_states:
            return 'Accept'
        else:
            return 'Reject'
