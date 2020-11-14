
class Curso:
    def __init__(self, codigo, alunos):
        self.codigo = codigo
        self.alunos = alunos
    
    def pegarCodigo(self):
        return self.codigo
    
    def pegarTodosAlunos(self):
        return self.alunos