from MeuCsv import MeuCsv
from Registro import RegistroHistorico
from Historico import Historico
from Aluno import Aluno
from Curso import Curso
from time import sleep

# Métodos para criação dos cursos da Faculdade
todosCursos = []
todosAlunos = []

def verificarExistenciaCurso( codigo ):
    
    # Rodar a lista de cursos procurando um curso com o mesmo código
    for umCurso in todosCursos:

        if (umCurso.pegarCodigo() == codigo):

            return True
    
    return False


def criarCursos( documento ):

    # Cabeçalho
    # 0 => MATRICULA | 1 => COD_DISCIPLINA | 2 => COD_CURSO
    # 3 => NOTA | 4 => CARGA_HORARIA | 5 => ANO_SEMESTRE

    for linha in documento:

        # Pegar Código do Curso
        cod_curso = linha[2]

        # Verificar pré existência do curso
        cursoExiste = verificarExistenciaCurso( cod_curso )

        # Se o curso não existir adicioná-lo
        if not cursoExiste:
            # Instânciar um novo curso
            curso = Curso(cod_curso)

            # Adicionar o novo curso na lista de cursos
            todosCursos.append(curso)


def verificarExistenciaAlunoNoCurso( cod_curso, matricula ):
    
    # Rodar a lista de cursos procurando um curso com o mesmo código
    for umCurso in todosCursos:

        if umCurso.pegarCodigo() == cod_curso:

            if umCurso.possuiAluno( matricula ):

                return True
    
    return False


def adicionarAlunoNoCurso( aluno, cursosAluno ):

    for codigoCurso in cursosAluno:

        if not verificarExistenciaAlunoNoCurso( codigoCurso, aluno.pegarMatricula() ):
            
            for umCurso in todosCursos:

                if umCurso.pegarCodigo() == codigoCurso:

                    umCurso.adicionarAluno( aluno )


def criarAlunoComHistorico( documento ):

    # Cabeçalho
    # 0 => MATRICULA | 1 => COD_DISCIPLINA | 2 => COD_CURSO
    # 3 => NOTA | 4 => CARGA_HORARIA | 5 => ANO_SEMESTRE

    # Como o documento está ordenado pelo número da matrícula do aluno
    matriculaAluno = 0
    historicoAluno = Historico()
    cursosAluno = []
    contadorLinhas = 0
    
    for linha in documento:

        # Pegar Matrícula do aluno
        matricula = linha[0]
        cod_disciplina = linha[1]
        cod_curso = linha[2]
        nota = linha[3]
        carga_horaria = linha[4]
        ano_semestre = linha[5]

        if matriculaAluno == 0:

            # Adicionar o nº da matricula na variavel auxiliar
            matriculaAluno = matricula

            # Criar novo Registro
            registroHistorico = RegistroHistorico( cod_disciplina, carga_horaria, nota, ano_semestre )

            # Adicionar ao Histórico
            historicoAluno.adicionarRegistroHistorico( registroHistorico )

            # Salvar Curso que o Aluno estuda na Lista
            cursosAluno.append( cod_curso )

            contadorLinhas += 1
            
        elif matriculaAluno == matricula:

            # Instânciar novo Registro Histórico
            registroHistorico = RegistroHistorico( cod_disciplina, carga_horaria, nota, ano_semestre )

            # Adicionar o Registro ao Histórico
            historicoAluno.adicionarRegistroHistorico( registroHistorico )

            # Salvar Curso que o Aluno estuda na Lista
            cursosAluno.append( cod_curso )

            contadorLinhas += 1
        
        else:
            
            # ====== Aluno Anterior ========
            # Gerar CR do Aluno
            historicoAluno.calculaCR()

            # Instânciar Novo Aluno
            aluno = Aluno(matriculaAluno, historicoAluno)

            todosAlunos.append( aluno )

            # Adicionar Aluno nos cursos em que participa
            adicionarAlunoNoCurso( aluno, cursosAluno )

            # ====== Próximo Aluno ========
            # Adicionar o nº da matricula do próximo aluno
            # na variavel auxiliar e repetir o processo
            matriculaAluno = matricula

            # Instânciar novo Histórico
            historicoAluno = Historico()

            # Criar novo Registro
            registroHistorico = RegistroHistorico( cod_disciplina, carga_horaria, nota, ano_semestre )

            # Adicionar ao Histórico
            historicoAluno.adicionarRegistroHistorico( registroHistorico )

            # Resetar Lista de Cursos que o Aluno participa
            cursosAluno = [cod_curso]

            contadorLinhas += 1

        if contadorLinhas == len(documento):
            # Gerar CR do Último Aluno
            historicoAluno.calculaCR()

            # Instânciar Último Aluno
            aluno = Aluno(matriculaAluno, historicoAluno)  

            todosAlunos.append( aluno )

            # Adicionar Aluno nos cursos em que participa
            adicionarAlunoNoCurso( aluno, cursosAluno )


print("=+=+=+=+=+=+=+=+            Desfio 3            =+=+=+=+=+=+=+=+")
print("=+=+=+=+=+=+=+=+        Inicializando CSV       =+=+=+=+=+=+=+=+")

# Instânciando um novo arquivo .csv
csv = MeuCsv("C:/Processo Seletivo STI/Processo Seletivo/teste.csv")

print("=+=+=+=+=+=+=+=+        Lendo Arquivo CSV       =+=+=+=+=+=+=+=+")

# Lendo o arquivo .csv e retornando o cabeçalho e os dados do documento
cabecalho, documento = csv.converterCSV()

print("=+=+=+=+=+=+=+=+ Carregando os Dados no Programa =+=+=+=+=+=+=+=+")

# Criando os cursos
criarCursos( documento )

# Criando os Alunos e seus Respectivos Históricos
criarAlunoComHistorico( documento )

print("=+=+=+=+=+=+=+=+       O CR dos Alunos é:       =+=+=+=+=+=+=+=+")

for umAluno in todosAlunos:

    historico = umAluno.pegarHistorico()
    
    print(f"${umAluno.pegarMatricula()}  -  ${historico.pegarCR()}")

print("=+=+=+=+=+=+=+=+      CR Médio dos Cursos      =+=+=+=+=+=+=+=+")
