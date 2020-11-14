from MeuCsv import MeuCsv
from time import sleep

print("=+=+=+=+=+=+=+=+ Inicializando Desfio 3 =+=+=+=+=+=+=+=+")

sleep(0.5)

print("=+=+=+=+=+=+=+=+ Inicializando CSV =+=+=+=+=+=+=+=+")
csv = MeuCsv("C:/Processo Seletivo STI/Processo Seletivo/teste.csv")

print("=+=+=+=+=+=+=+=+ Lendo Arquivo CSV =+=+=+=+=+=+=+=+")
c, d = csv.converterCSV()

print(c)
print(d)

print("=+=+=+=+=+=+=+=+ Carregando os Dados no Programa =+=+=+=+=+=+=+=+")


print("=+=+=+=+=+=+=+=+ Calculando CR dos Alunos =+=+=+=+=+=+=+=+")


print("=+=+=+=+=+=+=+=+ CR de cada Aluno =+=+=+=+=+=+=+=+")


print("=+=+=+=+=+=+=+=+ CR Médio dos Cursos =+=+=+=+=+=+=+=+")





def calculaCR( notas, cargasHorarias ):
        cr = 0
        cargaHorariaTotal = 0

        # Multiplicando as notas pelas cargas horárias
        for indice in range(0, len(notas)):
            cr += (notas[indice] * cargasHorarias[indice])
            cargaHorariaTotal += cargasHorarias[indice]
        
        # Dividindo a multiplicacao das notas por carga horária pela carga horária total
        cr = cr / cargaHorariaTotal

        return cr

# c, d = converterCSV("C:/Processo Seletivo STI/Processo Seletivo/teste.csv")

# notas = [82, 90, 8, 65, 96]
# chs = [60, 30, 30, 60, 60]

# cr = calculaCR(notas, chs)
