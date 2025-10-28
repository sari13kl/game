#ano de nascimento e idade
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess} pessoa nasceu?'))
    idade = atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também  tivemos {menores} pessoas menores de idade')