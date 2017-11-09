from pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self,_nome,_cpf, _rg):
        super().__init__(_nome)
        self.cpf = _cpf
        self.rg = _rg