# Nomes: Nikolas Lacerda e Victor Aso

from AFND import AFND


def fileToAFND(path):

    with open(path) as file:
        automato = file.readline()
        line = file.readline()
        line = file.readline()

        transacoes = []

        while line:
            line = line.replace('\n', '')
            transacoes.append(line)
            line = file.readline()

    # Consertando o automato

    separa_nome_automato = automato.split('=')

    nome_aux = separa_nome_automato[0]

    resto = separa_nome_automato[1]

    resto = resto.replace('(', '')
    resto = resto.replace(')', '')
    resto = resto.replace('\n', '')

    aux = resto.index('{')
    aux2 = resto.index('}')
    estados_aux = resto[aux + 1:aux2]
    resto = resto[aux2 + 2:]

    aux = resto.index('{')
    aux2 = resto.index('}')
    simbolos_aux = resto[aux + 1:aux2]
    resto = resto[aux2 + 2:]

    aux = resto.index(',')
    estado_inicial_aux = resto[:aux]
    resto = resto[aux + 1:]

    aux = resto.index('{')
    aux2 = resto.index('}')
    estados_finais_aux = resto[aux + 1:aux2]

    simbolos_aux = simbolos_aux.split(',')
    estados_aux = estados_aux.split(',')
    estados_finais_aux = estados_finais_aux.split(',')

    # Arruma transações

    transacoes_aux = {}

    for transacao in transacoes:
        tupla = transacao.split('=')
        key = tupla[0].replace('(', '')
        key = key.replace(')', '')

        new_item = tuple(key.split(','))
        to = [tupla[1]]

        if new_item in transacoes_aux:
            antigo = transacoes_aux[new_item]
            antigo.append(tupla[1])
            to = antigo

        new_itemc = {new_item: to}

        transacoes_aux.update(new_itemc)

    # Cria automato

    afnd = AFND()

    afnd.nome = nome_aux
    afnd.estados = estados_aux
    afnd.simbolos = simbolos_aux
    afnd.estado_inicial = estado_inicial_aux
    afnd.estados_finais = estados_finais_aux
    afnd.transacoes = transacoes_aux

    return afnd
