import abc
from Historico import Historico

class Conta(abc.ABC):

    total_contas = 0

    def __init__(self, numero, titular, saldo=0.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self.historico = Historico()
        Conta.total_contas += 1
#-----------------------getANDsetters-------------------------------------------
    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def depositar(self,valor):
        self._saldo += valor
        self.historico.transacoes.append('Depósito de {}'.format(valor))

    def sacar(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append('Saque de {}'.format(valor))
            return True

    def extrato(self):
        print('Informações do Titular')
        self._titular.imprimir()
        print('número:\t\t{}\nsaldo:\t\t{}'.format(self._numero, self._saldo))
        self.historico.transacoes.append('Tirou extrato - saldo de {}'.format(self._saldo))

    def transferir_para(self, destino, valor):
        retirou = self.sacar(valor)
        if not retirou:
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append('Transferência de {} para a conta {}'.
                                             format(valor, destino._numero))
            return True

    @abc.abstractmethod
    def atualiza():
        pass
#-----------------------getANDsetters-------------------------------------------