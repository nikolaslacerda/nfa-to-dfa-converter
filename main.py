import sys
from readAutomata import fileToNFA

path = sys.argv[1]  # or path = 'automato.txt'

nfa = fileToNFA(path)

print(nfa)

print('\n')

my_dfa = nfa.convertToAFD()

print(my_dfa)

print('Type \'exit\' to exit')

test = ''
while test != 'exit':
    test = input("Type a word:")
    if test == 'exit':
        sys.exit()
    print(my_dfa.accept(test))
