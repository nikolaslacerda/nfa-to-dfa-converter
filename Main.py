# Nomes: Nikolas Lacerda e Victor Aso

import sys
from LeAutomato import fileToAFND

#path = sys.argv[1]
path = 'automato.txt'

afnd = fileToAFND(path)

print(afnd)

print('\n')

myAFD = afnd.convertToAFD()

print(myAFD)

print("\n")
print('Palavra aaab:', myAFD.aceita('aaab'))
print('Palavra ab:', myAFD.aceita('ab'))
print('Palavra baaa:', myAFD.aceita('baaa'))
print('Palavra aa:', myAFD.aceita('aa'))
print('Palavra aaa:', myAFD.aceita('aaa'))
print('Palavra baaa:', myAFD.aceita('baaa'))

print("\n")

print('Digite exit para sair')

test = ''
while test != 'exit':
    test = input("Digite a palavra:")
    if test == 'exit':
        sys.exit()
    print(myAFD.aceita(test))
