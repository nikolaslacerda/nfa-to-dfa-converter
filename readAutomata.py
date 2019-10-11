from nfa import NFA


def fileToNFA(path):

    with open(path) as file:
        automata = file.readline()
        line = file.readline()
        line = file.readline()

        transitions = []

        while line:
            line = line.replace('\n', '')
            transitions.append(line)
            line = file.readline()

    split_automata_name = automata.split('=')

    nome_aux = split_automata_name[0]

    rest = split_automata_name[1]

    rest = rest.replace('(', '')
    rest = rest.replace(')', '')
    rest = rest.replace('\n', '')

    aux = rest.index('{')
    aux2 = rest.index('}')
    states_aux = rest[aux + 1:aux2]
    rest = rest[aux2 + 2:]

    aux = rest.index('{')
    aux2 = rest.index('}')
    symbols_aux = rest[aux + 1:aux2]
    rest = rest[aux2 + 2:]

    aux = rest.index(',')
    initial_state_aux = rest[:aux]
    rest = rest[aux + 1:]

    aux = rest.index('{')
    aux2 = rest.index('}')
    final_states_aux = rest[aux + 1:aux2]

    symbols_aux = symbols_aux.split(',')
    states_aux = states_aux.split(',')
    final_states_aux = final_states_aux.split(',')

    transitions_aux = {}

    for transition in transitions:
        tup = transition.split('=')
        key = tup[0].replace('(', '')
        key = key.replace(')', '')

        new_item = tuple(key.split(','))
        to = [tup[1]]

        if new_item in transitions_aux:
            old = transitions_aux[new_item]
            old.append(tup[1])
            to = old

        new_item_b = {new_item: to}
        transitions_aux.update(new_item_b)

    nfa = NFA()

    nfa.name = nome_aux
    nfa.states = states_aux
    nfa.symbols = symbols_aux
    nfa.initial_state = initial_state_aux
    nfa.final_states = final_states_aux
    nfa.transitions = transitions_aux

    return nfa
