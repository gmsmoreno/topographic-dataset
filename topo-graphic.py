# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:25:17 2021

@author: Gabriel
"""

import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt


def criararq(txt):
    open(txt + '.txt', 'w')

def arqexist(txt):
    try:
        open(txt + '.txt', 'r')
        print('O arquivo já existe')
    except FileNotFoundError:
        print('O arquivo não foi criado')
        try:
            criararq(input('Digite o nome do arquivo: '))
            print('Arquivo criado com sucesso!')
        except:
            print('Arquivo não criado')
    
    
    
    
nome = input('Procure o nome do arquivo: ')
arqexist(nome)

arq = open(nome + '.txt', 'w')

num_marcos = int(input('Defina o número de marcos a serem utilizados no cálculo: '))



y = []
x = []
horizontal_i = int(input('O espaçamento inicial entre os marcos será: '))
metros = 0
marco = 0

for i in range(0, num_marcos):
    while True:
        try:
            cota = int(input(f'Qual o valor da {i + 1}ª cota para inserção na tabela? '))
        except(TypeError, ValueError):
            print('Este valor não corresponde a valores numéricos')
        else:
            marco += 1
            break
    y.append(cota)
    x.append(metros)
    metros += horizontal_i
    arq.writelines(f'{marco};{cota}\n')
 

horizontal = int(input('Qual será o novo valor de espaçamento entre os marcos interpolados? '))


new_length = (horizontal_i / horizontal) * (num_marcos - 1)
new_x = np.linspace(min(x), max(x), int(new_length))
new_y = interpolate.interp1d(x, y, kind='quadratic')(new_x)

fig = plt.figure(1)

plt.subplot(2, 1, 1)
plt.plot(x, y, '-ko')
plt.title('Cotas Originais')

plt.subplot(2,1,2)
plt.plot(new_x, new_y, '-ko')
plt.title('Cotas Interpoladas')
plt.show()

y = new_y.tolist()
x = new_x.tolist()


arqout = open(nome + '_interpolation.txt', 'w')

p = 0
for linha in y:
    arqout.writelines(f'{x[p]:.2f};{linha:.3f}\n')
    p += 1
    

arq.close()
arqout.close()


   


