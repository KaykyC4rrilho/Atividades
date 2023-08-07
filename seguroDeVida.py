

class SeguroDeVida:
    def __init__(self,titular, numero_apolice, valor):
        self._titular= titular
        self._numero_apolice= numero_apolice
        self._valor= valor

#-----------------------getANDsetters-------------------------------------------
    def getTitular(self):
        return self._titular
    
    def setTitular(self, titular):
        self._titular= titular
#            " "

    def getNumeroA(self):
        return self._numero_apolice

    def setNumeroA(self, numero):
        self._numero_apolice= numero
#           " "

    def getValor(self):
        return self._valor

    def setValor(self, valor):
        self._valorr= valor
#           " "

    def get_valor_imposto(self):
        valorImposto= (self._valor * 0.05 ) +50
        return valorImposto
#----------------------getANDsetters-------------------------------------