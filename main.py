from MeuCsv import MeuCsv
from Registro import RegistroHistorico
from Historico import Historico
from Aluno import Aluno
from Curso import Curso
from Disciplina import Disciplina
from time import sleep

# Métodos para criação dos cursos da Faculdade
todosCursos = []
todasDisciplinas = []
todosAlunos = []

def verificarExistenciaCurso( codigo ):
    
    # Rodar a lista de cursos procurando um curso com o mesmo código
    for umCurso in todosCursos:

        if (umCurso.pegarCodigo() == codigo):

            return True
    
    return False


def verificarExistenciaDisciplina( codigo ):
    
    # Rodar a lista de cursos procurando um curso com o mesmo código
    for umaDisciplina in todasDisciplinas:

        if (umaDisciplina.pegarCodigo() == codigo):

            return True
    
    return False


def criarCursosDisciplinas( documento ):

    # Cabeçalho
    # 0 => MATRICULA | 1 => COD_DISCIPLINA | 2 => COD_CURSO
    # 3 => NOTA | 4 => CARGA_HORARIA | 5 => ANO_SEMESTRE

    for linha in documento:

        # Pegar Código do Curso
        cod_disciplina = linha[1]
        cod_curso = linha[2]

        # Verificar pré existência do curso
        cursoExiste = verificarExistenciaCurso( cod_curso )

        # Se o curso não existir adicioná-lo
        if cursoExiste:
            
            # Verificar pré existência da disciplina
            disciplinaExiste = verificarExistenciaDisciplina( cod_disciplina )

            if not disciplinaExiste:

                # Instânciar uma nova Disciplina
                disciplina = Disciplina( cod_disciplina )

                # Adicionar a nova disciplina na lista de disciplinas
                todasDisciplinas.append( disciplina )

                for umCurso in todosCursos:

                    if umCurso.pegarCodigo() == cod_curso:

                        # Adicionar a disiciplina no curso
                        umCurso.adicionarDisciplina( disciplina )

        else:

            # Instânciar um novo curso
            curso = Curso(cod_curso)

            # Instânciar uma nova Disciplina
            disciplina = Disciplina( cod_disciplina )

            # Adicionar a disiciplina no curso
            curso.adicionarDisciplina( disciplina )

            # Adicionar a nova disciplina na lista de disciplinas
            todasDisciplinas.append( disciplina )

            # Adicionar o novo curso na lista de cursos
            todosCursos.append(curso)


def pegarCurso( cod_curso ):

    for umCurso in todosCursos:

        if umCurso.pegarCodigo() == cod_curso:

            return umCurso


def pegarDisciplina( cod_disciplina ):

    for umaDisciplina in todasDisciplinas:

        if umaDisciplina.pegarCodigo() == cod_disciplina:

            return umaDisciplina            


def verificarExistenciaAlunoNaDisciplina( disciplina, aluno ):
    
    alunos = disciplina.pegarTodosAlunos()

    for umAluno in alunos:

        if umAluno.pegarMatricula() == aluno.pegarMatricula():

            return True
    
    return False


def adicionarAlunoNaDisciplina( aluno, cursosAluno, disciplinasAluno ):

    for codigoCurso in cursosAluno:

        curso = pegarCurso( codigoCurso )

        for umaDisciplina in curso.pegarTodasDisciplinas():

            for disciplinaAluno in disciplinasAluno:

                if umaDisciplina.pegarCodigo() == disciplinaAluno:

                    if not verificarExistenciaAlunoNaDisciplina( umaDisciplina, aluno ):
                
                        umaDisciplina.adicionarAluno( aluno )


def criarAlunoComHistorico( documento ):

    # Cabeçalho
    # 0 => MATRICULA | 1 => COD_DISCIPLINA | 2 => COD_CURSO
    # 3 => NOTA | 4 => CARGA_HORARIA | 5 => ANO_SEMESTRE

    # Como o documento está ordenado pelo número da matrícula do aluno
    matriculaAluno = 0
    historicoAluno = Historico()
    disciplinasAluno = []
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
            registroHistorico = RegistroHistorico( carga_horaria, nota, ano_semestre )

            # Adicionar ao Histórico
            historicoAluno.adicionarRegistroHistorico( registroHistorico )

            # Salvar Curso e Disciplinas que o Aluno estuda nas Listas
            cursosAluno.append( cod_curso )
            disciplinasAluno.append( cod_disciplina )

            contadorLinhas += 1
            
        elif matriculaAluno == matricula:

            # Instânciar novo Registro Histórico
            registroHistorico = RegistroHistorico( carga_horaria, nota, ano_semestre )

            # Adicionar o Registro ao Histórico
            historicoAluno.adicionarRegistroHistorico( registroHistorico )

            # Salvar Curso e Disciplinas que o Aluno estuda nas Listas
            cursosAluno.append( cod_curso )
            disciplinasAluno.append( cod_disciplina )

            contadorLinhas += 1
        
        else:
            
            # ====== Aluno Anterior ========
            # Gerar CR do Aluno
            historicoAluno.calculaCR()

            # Instânciar Novo Aluno
            aluno = Aluno( matriculaAluno, historicoAluno )

            todosAlunos.append( aluno )

            # Adicionar Aluno nos cursos em que participa
            adicionarAlunoNaDisciplina( aluno, cursosAluno, disciplinasAluno )

            # ====== Próximo Aluno ========
            # Adicionar o nº da matricula do próximo aluno
            # na variavel auxiliar e repetir o processo
            matriculaAluno = matricula

            # Instânciar novo Histórico
            historicoAluno = Historico()

            # Criar novo Registro
            registroHistorico = RegistroHistorico( carga_horaria, nota, ano_semestre )

            # Adicionar ao Histórico
            historicoAluno.adicionarRegistroHistorico( registroHistorico )

            # Salvar Curso e Disciplinas que o Aluno estuda nas Listas
            cursosAluno = [cod_curso]
            disciplinasAluno = [cod_disciplina]

            contadorLinhas += 1

        if contadorLinhas == len(documento):
            # Gerar CR do Último Aluno
            historicoAluno.calculaCR()

            # Instânciar Último Aluno
            aluno = Aluno( matriculaAluno, historicoAluno )  

            todosAlunos.append( aluno )

            # Adicionar Aluno nos cursos em que participa
            adicionarAlunoNaDisciplina( aluno, cursosAluno, disciplinasAluno )


print("=+=+=+=+=+=+=+=+            Desfio 3            =+=+=+=+=+=+=+=+")
print("=+=+=+=+=+=+=+=+        Inicializando CSV       =+=+=+=+=+=+=+=+")

# Instânciando um novo arquivo .csv
csv = MeuCsv("notas.csv")

print("=+=+=+=+=+=+=+=+        Lendo Arquivo CSV       =+=+=+=+=+=+=+=+")

# Lendo o arquivo .csv e retornando o cabeçalho e os dados do documento
cabecalho, documento = csv.converterCSV()

print("=+=+=+=+=+=+=+=+ Carregando os Dados no Programa =+=+=+=+=+=+=+=+")

# Criando os cursos
criarCursosDisciplinas( documento )

# Criando os Alunos e seus Respectivos Históricos
criarAlunoComHistorico( documento )

print("=+=+=+=+=+=+=+=+       O CR dos Alunos é:       =+=+=+=+=+=+=+=+")

for umAluno in todosAlunos:

    historico = umAluno.pegarHistorico()
    
    print(f"Aluno: {umAluno.pegarMatricula()}  -  CR: {historico.pegarCR():.2f}")

print("=+=+=+=+=+=+=+=+      CR Médio dos Cursos      =+=+=+=+=+=+=+=+")

for umCurso in todosCursos:
    
    umCurso.calculaCRMedio()

    print(f"Curso: {umCurso.pegarCodigo()}  -  CR Médio: {umCurso.pegarCRMedio():.2f}")

