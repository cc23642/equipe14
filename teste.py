import numpy as np
from scipy.optimize import linprog
from scipy.optimize import minimize
import scipy

print(scipy.__version__)
print(np.__version__)




# # import numpy

# # from scipy.optimize import linprog
# import scipy

# print(scipy.__version__)


# # Coeficientes da função objetivo
# c = [-1, -2]

# # Coeficientes das restrições de desigualdade
# A = [[-1, 1],
#      [1, 1]]

# # Termos independentes das restrições de desigualdade
# b = [1, 2]

# # Chamando a função linprog
# res = linprog(c, A_ub=A, b_ub=b, method='simplex')

# # Exibindo os resultados
# print('Status:', res.message)
# print('Valor da função objetivo:', res.fun)
# print('Variáveis de decisão:', res.x)



# # =====felipe=====
# import numpy as np

# # Problema 1:
# c = [5,1]

# A = [[-2,-1],[-1,-1],[-1,-5]]
# b = [-6,-4,-10]  #Deve se multiplicar tudo por - 1 para que a inequeação "seja oposta"

# bnds = [(0,None),(0,None)]

# res1 = linprog(c,A_ub=A, b_ub=b, bounds = bnds)


# print('Problema 1')
# print('Status:', res1.message)
# print('Valor da função:', res1.fun)
# print('Variaveis de X:', res1.x)


# # Problema 2

# c = [-2,3]

# A = [[1,2],[2,-1],[-1,0],[0,-1]]

# b = [6,8,0,0]

# bnds = [(0,None),(0,None)]

# res2 = linprog(c,A_ub=A,b_ub=b,bounds=bnds)

# print('================================')
# print('Problema 2')
# print('Status:', res2.message)
# print('Valor da função:', -res2.fun) #Por conta do linprog usar a minização e a maximização pode ser dada pelo oposto da minização
# print('Variaveis de X:', res2.x)

# #Problema 3

# c = [-15,-41,11]

# A = [[-3,0,0]]

# b = [-1]

# print('================================')
# print('Problema 3')
# print('Status:', res3.message)
# print('Valor da função:', -res3.fun)
# print('Variaveis de X:', res3.x)

# #Problema 4

# c = [0,0,10,10]

# A = [[-1,2,0,0],
#      [0,-1,2,0],
#      [0,0,-1,2]]

# b = [0,0,0]

# Aeq = [[1,1,1,1]]

# beq = [400]

# bnds = [(0,None),(0,None),(0,None),(0,0)]

# res4 = linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=bnds)

# print('================================')
# print('Problema 4')
# print('Status:', res4.message)
# print('Valor da função:', res4.fun)
# print('Variaveis de X:', res4.x)

# #Problema 5

# c = [2,0,-3,0]

# A = [[-1,0,0,0],
#      [0,-1,0,0]]

# b = [(0,1,0,0),(0,0,1,0)]

# Aeq = [[1,1,1,0]]

# beq = [12]

# bnds = [(0,None),(0,None),(0,None),(0,0)]

# res5 = linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=bnds)

# print('================================')
# print('Problema 5')
# print('Status:', res5.message)
# print('Valor da função:', -res5.fun)
# print('Variaveis de X:', res5.x)



c = [-5, 3, 3]

A = [
    [1, -1, 0],
    [0, 1, -1]
]
b = [-1, -1]

A_eq = [
    [1, 1, 1]
]
b_eq = [12]

x_bounds = [(0, None), (0, None), (0, None)]

res5 = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='highs')

print('================================')
print('Problema 5 [TESTE]')
print('Status:', res5.message)
print('Valor da função:', -res5.fun)
print('Variaveis de X:', res5.x)


# import numpy as np
# from scipy.optimize import linprog

# Coeficientes da função objetivo (convertendo para minimização)
c = [5, -3, -3]

# Coeficientes das restrições de desigualdade
A = [
    [1, -1, 0],  # x1 - x2 <= -1
    [0, 1, -1]   # x2 - x3 <= -1
]
b = [-1, -1]

# Coeficientes das restrições de igualdade
A_eq = [
    [1, 1, 1]  # x1 + x2 + x3 = 12
]
b_eq = [12]

# Limites das variáveis (todas >= 0)
x_bounds = [(0, None), (0, None), (0, None)]

# Resolver o problema
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='highs')

# Mostrar o resultado
print("================Chat-GPT code===============")
print('Status:', result.message)
print('Solução ótima:', result.x)
print('Valor da função objetivo:', -result.fun)  # Multiplicar por -1 para obter o valor da maximização original



#Problema 5

c = np.array([-2,3,3])

A = [[1,-1,0],
     [0,1,-1]]

b = [-1,-1]

Aeq = [[1,1,1]]

beq = [12]

res5 = linprog(-c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=(0,None))

print('==========FELIPE VERSION======================')
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


print('================================')
print('Problema 7')
print('Status:', res7.message)
print('Valor da função objetivo:', -res7.fun)
print('Variáveis de decisão:', res7.x)
print("Valor ótimo da função objetivo:", f_opt)
print("Solução ótima para x:", x_opt)




# import numpy as np
# from scipy.optimize import linprog

# Coeficientes da função objetivo (usando valores negativos para maximização)
c = [-9, -5]

# Coeficientes das restrições de desigualdade
A = []
b = []

# Criando as restrições baseadas na função trigonométrica para k = 1 a 13
for k in range(1, 14):
    A.append([np.sin(k / 13), np.cos(k / 13)])
    b.append(7)

# Convertendo para arrays numpy
A = np.array(A)
b = np.array(b)

# Limites das variáveis (todas >= 0)
x_bounds = [(0, None), (0, None)]

# Resolver o problema
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Mostrar o resultado
print('============Chat-GPT code====================')
print('Problema 7')
print('Status:', result.message)
print('Solução ótima:', result.x)
print('Valor da função objetivo:', -result.fun)  # Multiplicar por -1 para obter o valor da maximização original

