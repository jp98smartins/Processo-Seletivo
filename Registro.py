
class RegistroHistorico:
    def __init__(self, cargaHoraria, nota, anoSemestre):
        self.cargaHoraria = cargaHoraria
        self.nota = nota
        self.anoSemestre = anoSemestre
        self.registroHistorico = [self.cargaHoraria, self.nota, self.anoSemestre]


    def pegarCargaHoraria( self ):
        return self.cargaHoraria
    

    def pegarNota( self ):
        return self.nota
    

    def pegarAnoSemestre( self ):
        return self.anoSemestre
    

    def pegarRegistroHistorico( self ):
        return self.registroHistorico

    