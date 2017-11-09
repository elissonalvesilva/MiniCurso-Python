from animal import Animal

class Cachorro(Animal):
    
    def __init__(self,_nome,
    _idade,_raca,_cor,_nomeDono):
        super().__init__(_nome,_idade)
        self.raca  = _raca
        self.cor = _cor
        self.nomeDono = _nomeDono

    def latir(self):
        print('AUUAUA')

    def somar(self, x, y):
        return x+y

    def criarArquivoEescreve(self,texto):
        arq = open('meuarquivo.txt','w')
        arq.write('ashdjaskasd')
        arq.close()


    


