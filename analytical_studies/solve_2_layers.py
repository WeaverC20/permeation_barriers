
from sympy import *

#  # non normalised
D1, D2 = symbols('D1, D2')
x_int = Symbol("x_int")
S1, S2 = symbols('S1, S2')
u_0, u_L = symbols('c_0, c_L')
a1, a2, b1, b2 = symbols('a1, a2, b1, b2')
x_L = Symbol('L')
x_0 = 0
x = Symbol("x")
f = Symbol("f")


u1 = -1/2*f/D1*x**2 + a1*x + b1
u2 = -1/2*f/D2*x**2 + a2*x + b2


list_of_equations = [
    u1.subs(x, x_int)/S1 - u2.subs(x, x_int)/S2,
    D1*diff(u1, x).subs(x, x_int) - D2*diff(u2, x).subs(x, x_int),
    u1.subs(x, x_0) - u_0,
    u2.subs(x, x_L) - u_L
]


res = solve(list_of_equations, a1, a2, b1, b2)

print(simplify(res[a1]))
print(simplify(res[a2]))

# import numpy as np
# import matplotlib.pyplot as plt
# x1 = np.linspace(x_0, x_int)
# x2 = np.linspace(x_int, x_L)
# y1 = -1/2*f/D1*x1**2 + res[a1]*x1 + res[b1]
# y2 = -1/2*f/D2*x2**2 + res[a2]*x2 + res[b2]

# plt.plot(x1, y1)
# plt.plot(x2, y2)
# plt.show()
# print(simplify(res[a2]))
# print(res[a2])

#  ##### normalised
c_L = Symbol('c_L')
c_0 = 1
alpha, beta, gamma = symbols('alpha, beta, gamma')
a1, a2, b1, b2 = symbols('a1, a2, b1, b2')
x_L = 1
x_0 = 0
x = Symbol("x")
f1 = Symbol("f1")
f2 = Symbol("f2")


u1 = -1/2*f1*x**2 + a1*x + b1
u2 = -1/2*f2*x**2 + a2*x + b2


list_of_equations = [
    u1.subs(x, gamma)*beta - u2.subs(x, gamma),
    diff(u1, x).subs(x, gamma) - alpha*diff(u2, x).subs(x, gamma),
    u1.subs(x, x_0) - c_0,
    u2.subs(x, x_L) - c_L
]


res = solve(list_of_equations, a1, a2, b1, b2)

print(simplify(res[a1]).subs(f1, f*alpha**0.5).subs(f2, f*alpha**-0.5))
print(simplify(res[a2]).subs(f1, f*alpha**0.5).subs(f2, f*alpha**-0.5))
