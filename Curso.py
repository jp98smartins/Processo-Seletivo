from Aluno import Aluno
class Curso:
    def __init__( self, codigo ):
        self.codigo = codigo
        self.alunos = list()
        self.crMedio = 0
    

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
    

    def pegarCRMedio( self ):
        return self.cr
    

    def calculaCRMedio( self ):

        crMedio = 0
        quantidadeAlunos = 0

        for umAluno in self.alunos:

            historico = umAluno.pegarHistorico()
            
            # Pegando o CR de cada um dos Alunos
            crMedio += historico.pegarCR()

            quantidadeAlunos += 1
        
        # Dividindo a soma dos CR's dos Alunos pela Quantidade de Alunos
        crMedio = crMedio / quantidadeAlunos

        self.crMedio = crMedio

