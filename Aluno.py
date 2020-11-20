class Aluno:
    def __init__(self, matricula, historico):
        self.matricula = matricula
        self.historico = historico
    
    
    def pegarMatricula(self):
        return self.matricula


    def pegarHistorico(self):
        return self.historico
    
    