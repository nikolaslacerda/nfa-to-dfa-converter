# Nomes: Nikolas Lacerda e Victor Aso


class AFD:

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

    def getProximoEstado(self, transacao):
        return self.transacoes[transacao]

    def aceita(self, palavra):
        estadoatual = self.estado_inicial
        caracteres_da_palavra = list(palavra)

        for caracter in caracteres_da_palavra:

            try:
                novoestado = self.getProximoEstado((estadoatual, caracter))
            except:
                novoestado = None

            if (novoestado == None):
                return 'Rejeita'

            estadoatual = novoestado

        if estadoatual in self.estados_finais:
            return 'Aceita'
        else:
            return 'Rejeita'
