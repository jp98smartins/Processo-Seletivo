
class RegistroHistorico:
    def __init__(self, codigoDisciplina, cargaHoraria, nota, anoSemestre):
        self.codigoDisciplina = codigoDisciplina
        self.cargaHoraria = cargaHoraria
        self.nota = nota
        self.anoSemestre = anoSemestre
        self.registroHistorico = [self.codigoDisciplina, self.cargaHoraria, self.nota, self.anoSemestre]


    def pegarCodigoDisciplina( self ):
        return self.codigoDisciplina
    

    def pegarCargaHoraria( self ):
        return self.cargaHoraria
    

    def pegarNota( self ):
        return self.nota
    

    def pegarAnoSemestre( self ):
        return self.anoSemestre
    

    def pegarRegistroHistorico( self ):
        return self.registroHistorico

    