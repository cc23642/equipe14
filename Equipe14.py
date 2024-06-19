import numpy as np
import scipy
from scipy.optimize import linprog
import matplotlib.pyplot as plt

#O código foi feito utilizando o python e a bibloteca Scipy que inclui o método optimize.linprog que tem por objetivo fazer a minização,
#ou maximização dependendo de como será escrito, de uma função linear que tenha conjunto de restrições lineares.
#Em outras palavras podemos dizer que essa função tem como objetivo usar o método Simplex
#Porém o linprog necessita que os valores sejam passados em matrizes para que seja possível realizar o cálculo.

#Descrição de como ler o código:
#Chamando a função linprog(c,A_ub,b_ub,A_eq,b_ub,bounds)

#c - coeficientes da função

# A_ub - coefiecientes das restrições de uma inequeção
# A_eq - coefiecientes das restrições de uma equação
#**Cada vetor dentro do vetor representa um linha de uma inequação diferentes.

#b_ub - termos independentes das restrições de uma inequeção
#b_eq - termos independentes das restrições de uma equação
#**Cada valor no vetor é de uma linha de sua respectiva inequação


#bounds - Restições do valor minino e máximo que as variaveis em incognitas podem possuir.

#**Quando definimos o apenas um valor só no bounds faz com que esse seja o valor padrão de restrição para todas as variaveis.

#Também vale lembrar que o linprog faz normalmente a minizição e para que se torne uma maximização é necessário multiplicar o coeficientes da função e o seu resultado por -1
#Use como exemplo o problema 1 a seguir:

# Problema 1:

# Coeficientes da função objetivo
c = [5,1] #5x1 + x2

# Coeficientes das restrições das inequações

A = [[-2,-1], #2x1 + x2 ≥ 6     O Linprog utiliza normalmente o menor ou igual (<=)
     [-1,-1], # x1 + x2 ≥ 4     E para virar maior ou igual (>=) deve se multiplicar a inequação inteira por -1
     [-1,-5]] # x1 + 5x2 ≥ 10

# Termos independentes das restrições das inequações
b = [-6,-4,-10]  #Deve se multiplicar tudo por - 1 para que a inequeação "seja oposta"

# Chamando a função linprog
res1 = linprog(c,A_ub=A, b_ub=b, bounds = (0,None))
#Não foi preciso criar uma variavel para os bounds, pois todos os variaveis tem a mesma restrição

# Exibindo os resultados
print('Problema 1')
print('Valor da função:', res1.fun)
print('Variaveis de X:', res1.x)




# Problema 2

c = [-2,3] # 2x1 − 3x2, Multiplicamos o coeficientes por -1 por ser uma maximização

A = [[1,2],  # x1 + 2x2 ≤ 6
     [2,-1]] # 2x1 − x2 ≤ 8

b = [6,8]

res2 = linprog(c,A_ub=A,b_ub=b,bounds=(0,None))

print('================================')
print('Problema 2')
print('Valor da função:', -res2.fun) #Por conta do linprog usar a minização e a maximização pode ser dada pelo oposto da minização
print('Variaveis de X:', res2.x)

#Problema 3

c = [-15,-41,11] #15(x1 + 2x2) + 11(x2 − x3) fazendo a distributiva temos 15x1 + 41x2 - 11x3

A = [[-3,0,0]] #3x1 ≥ x1 + x2 + x3

b = [-1]

bnds = [(0,1),(0,1),(0,1)] #0 ≤ xj ≤ 1

res3 = linprog(c,A_ub=A,b_ub=b,bounds=bnds)

print('================================')
print('Problema 3')
print('Valor da função:', -res3.fun)
print('Variaveis de X:', res3.x)

#Problema 4

c = [0,0,10,10] #Minimzar 10(x3 + x4) fazendo a distributiva temos 0x1 + 0x2 + 10x3 + 10x4 

# xj − 2xj+1 ≥ 0        j = 1, 2, 3
A = [[-1,2,0,0], #x1 - 2x2 >= 0
     [0,-1,2,0], #x2 - 2x3 >= 0
     [0,0,-1,2]] #x3 - 2x4 >= 0

b = [0,0,0] #Termo independente das inequações

Aeq = [[1,1,1,1]] #x1 + x2 + x3 + x4 = 400

beq = [400]

bnds = [(0,None),(0,None),(0,None),(0,0)] #O quatro elemento colocamos 0,0 pois não tem uma restrição no problema

res4 = linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=bnds)

print('================================')
print('Problema 4')
print('Valor da função:', res4.fun)
print('Variaveis de X:', res4.x)


#Problema 5

# Coeficientes da função objetivo, multiplicando por -1 pra ser maximização
c = np.array([-2,0,3])

#xj + 1 <= xj+1 -> xj - xj+1 <= -1  j = 1,2
A = [[1,-1,0],  # x1 - x2 <= -1
     [0,1,-1]]  # x2 - x3 <= -1
               

b = [-1,-1]

# Coeficientes das restrições de igualdade
Aeq = [[1,1,1]] #x1 + x2 + x3 = 12

beq = [12]

res5 = linprog(-c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=(0,None))

print('================================')
print('Problema 5')
print('Valor da função:', -res5.fun) # Multiplicar por -1 para obter o valor da maximização
print('Variaveis de X:', res5.x)

# Maximizar Problema 7

c = np.array([-9,-5]) #9x1 + 5x2

# sen(k/13)x1 + cos(k/13)x2 ≤ 7        k = 1, . . . , 13

A = []

for k in range(1, 14):
     A.append([np.sin(k / 13), np.cos(k / 13)])

b = [7]*13

res7 = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))


variaveisx = [round(x,2) for x in res7.x]
print('================================')
print('Problema 7')
print('Valor da função inteiro:', -res7.fun)
print('Variáveis de X inteiro:', res7.x)
print('Valor da função arrendondado:', round(-res7.fun,2))
print('Variáveis de X arrendondado:', variaveisx)


#Para testar o código é necessário colocar o seguinte comando no terminal:
#python Equipe14.py ou python3 Equipe14.py

#Fazendo o gráfico das respostas do Problema 1

#Definindo as restrições
x = np.linspace(0, 10, 400)
y1 = (6 - 2 * x)
y2 = (4 - x)
y3 = (10 - x) / 5

#Colocando no gráfico as inequações
plt.plot(x, y1, label=r'$2x_1 + x_2 \geq 6$')
plt.plot(x, y2, label=r'$x_1 + x_2 \geq 4$')
plt.plot(x, y3, label=r'$x_1 + 5x_2 \geq 10$')

#Área da região factivél
y4 = np.maximum(y1, y2)
y5 = np.maximum(y4, y3)
plt.fill_between(x, 0, y5, where=(y5 >= 0), color='green', alpha=0.5)

#Coordenada da solução ótima
plt.plot(res1.x[0], res1.x[1], 'ro', label='Solução Ótima')


plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()
plt.title('Problema 1')

#Mostrar o gráfico
plt.show()