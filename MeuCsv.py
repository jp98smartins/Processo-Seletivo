import csv
class MeuCsv:
    def __init__(self, caminho):
        self.caminho = caminho
    

    def converterCSV( self ):
        caminhoCSV = self.caminho
        cabecalho = list()
        documento = list()

        with open( caminhoCSV, mode = 'r' ) as arquivoCSV:
            # Abrindo o Arquivo CSV
            dados = csv.reader(arquivoCSV)
            
            # Contador p/ separar o Cabeçalho
            separarCabecalho = 0

            # Lendo o Arquivo
            for umaLinha in dados:
                if separarCabecalho == 0:
                    # Lendo o cabecalho
                    cabecalho = umaLinha

                    # Aumentando contador para ler o documento
                    separarCabecalho += 1

                else: 
                    # Adicionando linha no documento
                    documento.append(umaLinha)

        # Retornando dados formatados (Cabeçalho e Dados do Documento)
        return cabecalho, documento

