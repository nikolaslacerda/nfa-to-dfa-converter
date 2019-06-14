class AFND:

    def __init__(self):
        self.name = ''
        self.estados = []
        self.estado_inicial = ''
        self.estados_finais = []
        self.simbolos = []
        self.transacoes = {}

    def __str__(self):
        return f'Nome do Autômato: {self.name} \
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

    # def getProximoEstado(self, transacao):
    # transação = (q0, a)
    # retorna = q1
    # return self.transacoes[transacao]

    def getProximoEstado(self, estado, simbolo):
        return self.transacoes[(estado, simbolo)]

    def convertToAFD(self):

        afd = {}
        faltantes = [self.estado_inicials7]

        for simbolo in self.simbolos:
            for element in faltantes:
                try:
                    a = self.transacoes[(faltantes[0], simbolo)]
                except:
                    a = 'none'

                afd.update({(faltantes[0], simbolo): a})
                next = a
                faltantes.append(next)

        faltantes.pop(0)

        print(faltantes)
        return afd


def aceita(self, w):
    pass
