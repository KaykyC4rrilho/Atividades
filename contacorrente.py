from conta import Conta


class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10

    def get_valor_imposto(self):
        valorImposto= self._saldo * 0.01
        return valorImposto