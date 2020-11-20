from Aluno import Aluno
class Curso:
    def __init__( self, codigo ):
        self.codigo = codigo
        self.disciplinas = list()
        self.crMedio = 0
    

    def pegarCodigo( self ):
        return self.codigo
    

    def adicionarDisciplina( self, disciplina ):
        self.disciplinas.append( disciplina )
    

    def pegarTodasDisciplinas( self ):
        return self.disciplinas


    def pegarCRMedio( self ):
        return self.crMedio
    

    def calculaCRMedio( self ):

        crMedio = 0
        quantidadeAlunos = 0

        for umaDisciplina in self.disciplinas:

            alunos = umaDisciplina.pegarTodosAlunos()

            for umAluno in alunos:

                historico = umAluno.pegarHistorico()
            
                # Pegando o CR de cada um dos Alunos
                crMedio += historico.pegarCR()

                quantidadeAlunos += 1
        
        # Dividindo a soma dos CR's dos Alunos pela Quantidade de Alunos
        crMedio = crMedio / quantidadeAlunos

        self.crMedio = crMedio

