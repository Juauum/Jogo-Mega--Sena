print('='*90)
print('\033[1;32mMEGA-SENA\033[m'.center(100))
print('='*90)
from random import shuffle
nums = []
aposta = 0
for c in range(1,61):
    nums.append(c)
    
shuffle(nums)
aposta = int(input('Quantas apostas deseja fazer: '))
print('-'*90)
for j in range(0,aposta):
    shuffle(nums)
    print(sorted(nums[0:6]))
    print()
if aposta == 1:
    print(f'Valor da aposta de 1 jogo: 4,50 R$')
if aposta > 1:
    print(f'Valor da aposta de {aposta} jogos: {aposta * 4.50:.2f} R$')
print('-'*90)
print('\033[1;32mBOA SORTE\033[m'.center(100))  