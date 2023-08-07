from Tributavel import Tributavel
class ManipuladorDeTributaveis:



    
    
    def calcula_imposto(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel):
                total += t.get_valor_imposto()

            else:
                print("{} Erro e apenas os tributáveis serão somados ao total.".format(t.__class__.__name__))
        return total
