from ex1 import Celular
from ex2 import Pessoa

celular1 = Celular('Apple', '14 pro')
celular2 = Celular('Samsung', 'A23')

print('c1:', celular1.marca)
print('c2:', celular2.bateria)


print('[antes do uso] Bateria c1: ', celular1.bateria )
celular1.usar()
celular1.usar()
print('[depois do uso] Bateria c1: ', celular1.bateria)

pessoa = Pessoa('Giovanna')

print(f'Dinheiro{pessoa.nome}: ', pessoa.dinheiro)
pessoa.trabalhar()
pessoa.trabalhar()
pessoa.gastar()
print(f'Dinheiro {pessoa.nome}: ', pessoa.dinheiro)