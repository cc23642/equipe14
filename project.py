import numpy as np
print("código")
import scipy
from scipy.optimize import linprog
print("código.import scipy")


# Minimizar problema 1
c= [5,1]
A=[[-2,-1],
   [-1,-1],
   [-1,-5]]
b=[-6,-4,10]
bnds=[(0,None),(0,  None)]
res1 = linprog(c,A_ub=A, b_ub=b, bounds = bnds)

print('================================')
print('Problema 1')
print('Status:', res1.message)
print('Valor da função:', res1.fun)
print('Variaveis de X:', res1.x)


# Maximizar problema 2
c=[-2,3]
A=[[1,2],
   [2,-1],
   [-1,0],[0,-1]]
b=[6,8,0,0]
bnds=[(0,None),(0,None)]

res2 = linprog(c,A_ub=A,b_ub=b,bounds=bnds)

print('================================')
print('Problema 2')
print('Status:', res2.message)
print('Valor da função:', -res2.fun)
print('Variaveis de X:', res2.x)


# Maximizar problema 3

c = [-15,-41,11]
A = [[-3,0,0]]
b = [-1]
bnds = [(0,1),(0,1),(0,1)]
res3 = linprog(c,A_ub=A,b_ub=b,bounds=bnds)

print('================================')
print('Problema 3')
print('Status:', res3.message)
print('Valor da função:', -res3.fun)
print('Variaveis de X:', res3.x)


# Maximizar problema 4

c = [0,0,10,10]

A = [[-1,2,0,0],
     [0,-1,2,0],
     [0,0,-1,2]]

b = [0,0,0]

Aeq = [[1,1,1,1]]

beq = [400]

bnds = [(0,None),(0,None),(0,None),(0,0)]

res4 = linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=bnds)

print('================================')
print('Problema 4')
print('Status:', res4.message)
print('Valor da função:', res4.fun)
print('Variaveis de X:', res4.x)


#Problema 5

c = [-2,0,-3]

A = [[1,-1,0],
     [0,1,-1,]]

b = [-1,-1]

Aeq = [[1,1,1]]

beq = [12]

bnds = [(0,None),(0,None),(0,None),(0,0)]

res5 = linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=(0,None))

print('================================')
print('Problema 5')
print('Status:', res5.message)
print('Valor da função:', -res5.fun)
print('Variaveis de X:', res5.x)


# Maximizar Problema 7

c = np.array([9,5])

A = []

for k in range(1, 14):
     A.append([np.sin(k / 13), np.cos(k / 13)])

b = [7]*13

res7 = linprog(-c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

x_opt = res7.x #Valor ótimo da variavel de decisão
f_opt = -res7.fun #Valor ótimo da função objetivo

print("Valor ótimo da função objetivo:", f_opt)
print("Solução ótima para x:", x_opt)
print('================================')
print('Problema 7')
print('Status:', res7.message)
print('Valor da função objetivo:', -res7.fun)
print('Variáveis de decisão:', res7.x)

