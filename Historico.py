from Registro import RegistroHistorico
class Historico:
    def __init__(self):
        self.historico = list()
        self.cr = 0.0
    

    def adicionarRegistroHistorico( self, registroHistorico ):
        self.historico.append(registroHistorico)


    def pegarHistorico( self ):
        return self.historico
    

    def pegarCR( self ):
        return self.cr
    

    def calculaCR( self ):

        cr = 0
        cargaHorariaTotal = 0

        for registro in self.historico:

            cargaHoraria = float(registro.pegarCargaHoraria())
            nota = float(registro.pegarNota())

            # Multiplicando as notas pelas cargas horárias
            cr += (nota * cargaHoraria)
            cargaHorariaTotal += cargaHoraria
            
        # Dividindo a multiplicacao das notas por carga horária pela carga horária total
        cr = cr / cargaHorariaTotal

        self.cr = cr

            