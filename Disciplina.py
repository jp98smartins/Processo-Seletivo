from Aluno import Aluno
class Disciplina:
    def __init__( self, codigo ):
        self.codigo = codigo
        self.alunos = list()
    

    def pegarCodigo( self ):
        return self.codigo


    def adicionarAluno( self, aluno ):
        self.alunos.append( aluno )
    

    def pegarTodosAlunos( self ):
        return self.alunos
    

    def possuiAluno( self, matricula_aluno ):
        
        # Rodar a lista de Alunos procurando um aluno com a mesma matricula
        for umAluno in self.alunos:
            
            if umAluno.pegarMatricula() == matricula_aluno:
                
                return True
        
        return False

