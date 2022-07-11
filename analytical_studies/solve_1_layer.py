
from sympy import *


D = 1
u_0, u_L = 0, 0 #symbols('c_0, c_L')
a = Symbol("a")
b = Symbol("b")
x_L = 1#Symbol('L')
x_0 = 0#Symbol('x_0')
x = Symbol("x")
f = 2#Symbol("f")


u = -1/2*f/D*x**2 + a*x + b


list_of_equations = [
    u.subs(x, x_0) - u_0,
    u.subs(x, x_L) - u_L,
]


res = solve(list_of_equations, a, b)

# print(simplify(res[a1]))

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(x_0, x_L)
y = -1/2*f/D*x**2 + res[a]*x + res[b]

plt.plot(x, y)
plt.show()
