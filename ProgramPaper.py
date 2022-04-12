from random import randint
from time import sleep
print('-------- jogo do pedra, papel, tesoura -------')

print('Pedra é [0]')
print('Tesoura  é [2]')
print('Papel é [1]')
p = int(input('Digite qual você quer: '))
lista = ['pedra','papel','tesoura']
c = randint(0, 2)
print('JO')
sleep(1)
print('KEN')

print('O computador escolheu {}'.format(lista[c]))
print('Jogador escolheu {}'.format(lista[p]))

if c == 0:
    if p == 0:
       print('EMPATE')
    elif p == 1:
       print('Jogador venceu')
    elif p == 2:
       print('Jogador perdeu')
    else:
        print('JOGADA INVALIDA')
elif c == 1:
    if p == 0:
       print('Computador venceu')
    elif p == 1:
       print('empate')
    elif p == 2:
        print('Jogador venceu')
    else:
        print('JOGADA INVALIDA')
elif c == 2:
    if p == 0:
         print('Jogador venceu')
    elif p == 1:
         print('Computdor vence')
    elif p == 2:
       print('empate')
    else:
        print('JOGADA INVALIDA')