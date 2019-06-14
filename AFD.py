class AFD:

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
                \n\nTransações: {self.transacoes}'

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
        # transação = (q0, a)
        # retorna = q1
        return self.transacoes[transacao]

    def aceita(self, w):
        pass