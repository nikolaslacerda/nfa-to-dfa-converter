# Nomes: Nikolas Lacerda e Victor Aso

from AFD import AFD


class AFND:

    def __init__(self):
        self.nome = ''
        self.estados = []
        self.estado_inicial = ''
        self.estados_finais = []
        self.simbolos = []
        self.transacoes = {}

    def __str__(self):
        return f'Nome do Autômato: {self.nome} \
                \nEstados: {self.estados} \
                \nSimbolos: {self.simbolos} \
                \nEstado Inicial: {self.estado_inicial} \
                \nEstados Finais: {self.estados_finais} \
                \nTransações: {self.transacoes}'

    def getEstadoInicial(self):
        return self.estado_inicial

    def getEstadosFinais(self):
        return self.estados_finais

    def getEstados(self):
        return self.estados

    def getTransacoes(self):
        return self.transacoes

    def getSimbolos(self):
        return self.simbolos

    def getProximoEstado(self, estado, simbolo):
        return self.transacoes[(estado, simbolo)]

    def convertToAFD(self):

        afd = {}
        faltantes = [(self.estado_inicial,)]
        check = []

        while len(faltantes) != 0:
            atual = faltantes[0]
            check.append(atual)
            #print('Faltantes no inicio', faltantes)
            #print('Atual', atual)
            if len(atual) > 1:
                listAtual = []
                for simbolo in self.simbolos:
                    for estado in atual:
                        try:
                            a = self.transacoes[(estado, simbolo)]
                        except:
                            a = None
                        #print(f"Estado {estado} recebendo {simbolo} é {a}")

                        if a != None:
                            for b in a:
                                if b not in listAtual:
                                    listAtual.append(b)
                    t = tuple(listAtual)
                    #print("t", t)
                    if t in check:
                        pass
                    else:
                        if t not in faltantes:
                            faltantes.append(t)

                    #print("Faltantes Final", faltantes)

                    #print("Inserindo", {(atual, simbolo): t})
                    afd.update({(atual, simbolo): t})
                    #print("AFD agr", afd)
                    listAtual = []
                faltantes.pop(0)

            else:
                for simbolo in self.simbolos:
                    for estado in atual:
                        try:
                            a = self.transacoes[(estado, simbolo)]
                        except:
                            a = None

                    # print(f"Estado {estado} recebendo {simbolo} é {a}")

                    if a != None:
                        aTuple = tuple(a)
                        #print("inserindo", {(atual, simbolo): tuple(a)})
                        afd.update({(estado, simbolo): tuple(a)})

                        if aTuple in check:
                            pass
                        else:
                            if aTuple not in faltantes:
                                faltantes.append(aTuple)
                faltantes.pop(0)
            #print("Faltantes Final", faltantes)
            #print("AFD agr", afd)


        #print("Faltantes:", faltantes)
        afd_conv = {}
        new_finals = []

        for k in afd:
            b = False

            if len(k[0]) > 1:

                for item in k[0]:
                    if item in self.estados_finais:
                        b = True
            else:
                if k[0] in self.estados_finais:
                    b = True

            if b:
                if k[0] not in new_finals:
                    if type(k[0]) == tuple:
                        new_finals.append(k[0])

        for k, v in afd.items():
            if len(k[0]) > 1:
                afd_conv.update({(convertTuple(k[0]), k[1]): convertTuple(v)})
            else:
                afd_conv.update({(k[0], k[1]): convertTuple(v)})

        # ERROS DAQUI PRA CIMA
        # print(afd)

        myAFD = AFD()
        myAFD.nome = self.nome + "(AFD)"
        myAFD.estado_inicial = self.estado_inicial
        myAFD.simbolos = self.simbolos

        for estadofinal in new_finals:
            if type(estadofinal) == tuple:
                myAFD.estados_finais.append(convertTuple(estadofinal))
            else:
                myAFD.estados_finais.append(estadofinal)

        myAFD.transacoes = afd_conv

        for estado in afd_conv:
            if estado[0] not in myAFD.estados:
                myAFD.estados.append(estado[0])

        # print(myAFD)
        # return afd_conv
        return myAFD


def convertTuple(tup):
    str = ''.join(tup)
    return str
