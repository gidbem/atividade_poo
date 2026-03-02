class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 0
    
    def trabalhar(self):
        print('Trabalhei')
        self.dinheiro += 50 
    
    def gastar(self):
        print('Gastei!')
        self.dinheiro -= 20

pessoa = Pessoa('Giovanna')

pessoa.trabalhar()
pessoa.trabalhar()
pessoa.gastar()

print(pessoa.dinheiro)