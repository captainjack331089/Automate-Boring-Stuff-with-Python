
# 4 * x + 0.25*y ==  100
#     y == 100 -x
#     return(x,y)
# 4 * x + 0.25*(100-x) = 100



from sympy import *
x = Symbol('x')
y = Symbol('y')

a = int(solve(4 * x + 0.25*(100-x) - 100)[0])
b  = 100 - a

print(a,b)

