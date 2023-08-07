from contacorrente import ContaCorrente
from seguroDeVida import SeguroDeVida
from manipulador_tributaveis import ManipuladorDeTributaveis
from Historico import Historico
from contapoupanca import ContaPoupanca
from Tributavel import Tributavel

Tributavel.register(ContaCorrente)
Tributavel.register(SeguroDeVida)

contaC = ContaCorrente( 1234, "Kayky", 5000)
seguro= SeguroDeVida("Marcos", 12, 34000)
contaP= ContaPoupanca(2342,"Athos", 50000)

contalistas= [
    contaC,
    seguro,
    contaP]

print(contaC.get_valor_imposto(), "\n", seguro.get_valor_imposto())


manipuladorImp= ManipuladorDeTributaveis()
print(manipuladorImp.calcula_imposto(contalistas))


