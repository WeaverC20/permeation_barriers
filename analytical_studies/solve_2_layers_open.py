from sympy import *

# non normalised
D1, D2 = symbols('D1, D2')
x_int = Symbol("x_int")
S1, S2 = symbols('S1, S2')
Kd, Kr = symbols('Kd, Kr')
u_0, u_L = symbols('c_0, c_L')
a1, a2, b1, b2 = symbols('a1, a2, b1, b2')
x_L = Symbol('L')
x_0 = 0
x = Symbol("x")
P = Symbol("P")
u_L = 0

u1 = a1*x + b1
u2 = a2*x + b2

list_of_equations = [
    u1.subs(x, x_int)/S1 - u2.subs(x, x_int)/S2, # Continuity at x_int
    D1*diff(u1, x).subs(x, x_int) - D2*diff(u2, x).subs(x, x_int), # Flux continuity at x_int
    diff(u1, x).subs(x, x_0) - Kd*P + Kr*u1.subs(x, x_0), # Neumann boundary condition at x_0
    u2.subs(x, x_L), #concentration = 0 at x_L

    # Kd*P-Kr1*u1.subs(x, x_0)**2 + D1*(u1.subs(x, x_int) - u1.subs(x, x_0))/(x_int-x_0), # Flux Continuity at x_0
    # u1.subs(x, x_int)/S1 - u2.subs(x, x_int)/S2,  # Continuity at x_int
    # D1*diff(u1, x).subs(x, x_int) - D2*diff(u2, x).subs(x, x_int),  # Flux continuity at x_int
    # -D2*(u2.subs(x, x_L) - u2.subs(x, x_int))/(x_L-x_int) - Kr2*u2.subs(x, x_L)**2, #Flux continuity at x_L
    # u2.subs(x, x_L),  # Concentration = 0 at x_L

    # diff(u2, x).subs(x, x_L),  # Neumann boundary condition: flux = 0 at x_L
    # diff(u1, x).subs(x, x_0),  # Neumann boundary condition: flux = 0 at x_L
]

res = solve(list_of_equations, a1, a2, b1, b2)

print("a1 :", simplify(res[a1]))
print("a2 :", simplify(res[a2]))
print("b1 :", simplify(res[b1]))
print("b2 :", simplify(res[b2]))




import numpy as np
import matplotlib.pyplot as plt

# Substitute numerical values for all parameters into the solutions
params = {
    D1: 1, # tungsten
    D2: 10, # eurofer
    S1: 1,
    S2: 5,
    x_int: 0.1,
    x_L: 1,
    P: 100,
    Kd: 1,
    Kr: 1,
}

# # Substitute numerical values for all parameters into the solutions
# params = {
#     D1: 4e-10, # tungsten
#     D2: 1e-8, # eurofer
#     S1: 1.13e20,
#     S2: 1.77e20,
#     x_int: 0.01,
#     x_L: 0.1,
#     P: 100000,
#     Kd: 1.5e-24, # no dissociation coeff
#     Kr: 1.5e-23, # tungsten
# }

# sub soolutions into u1 u2
u1_sol = u1.subs(res).subs(params)
u2_sol = u2.subs(res).subs(params)

# evaluating symbolic expressions
u1_num = lambdify(x, u1_sol, "numpy")
u2_num = lambdify(x, u2_sol, "numpy")

x1_vals = np.linspace(x_0, params[x_int], 100)
x2_vals = np.linspace(params[x_int], params[x_L], 100)
u1_vals = u1_num(x1_vals)
u2_vals = u2_num(x2_vals)

plt.figure(figsize=(8, 5))
plt.plot(x1_vals, u1_vals, label="u1(x)", color="blue")
plt.plot(x2_vals, u2_vals, label="u2(x)", color="red")
plt.axvline(params[x_int], linestyle="--", color="black", label="x_int")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.grid()
plt.show()





# normalized

c_L = Symbol('c_L')
c_0 = 1
alpha, beta, gamma = symbols('alpha, beta, gamma') # gamma = x_int
a1, a2, b1, b2 = symbols('a1, a2, b1, b2')
x_L = 1
x_0 = 0
x = Symbol("x")

u1 = a1*x + b1
u2 = a2*x + b2

list_of_equations = [
    u1.subs(x, gamma)*beta - u2.subs(x, x_int), # Continuity at x_int
    diff(u1, x).subs(x, gamma) - alpha*diff(u2, x).subs(x, gamma), # Flux continuity at x_int
    diff(u1, x).subs(x, x_0) - Kd*P + Kr*u1.subs(x, x_0), # Neumann boundary condition at x_0
    u2.subs(x, x_L), #concentration = 0 at x_L
]

list_of_equations = [
    u1.subs(x, x_int)/S1 - u2.subs(x, x_int)/S2, # Continuity at x_int
    D1*diff(u1, x).subs(x, x_int) - D2*diff(u2, x).subs(x, x_int), # Flux continuity at x_int
    diff(u1, x).subs(x, x_0) - Kd*P + Kr*u1.subs(x, x_0), # Neumann boundary condition at x_0
    u2.subs(x, x_L), #concentration = 0 at x_L
]

res = solve(list_of_equations, a1, a2, b1, b2)

# print(simplify(res[a1]).subs(f1, f*alpha**0.5).subs(f2, f*alpha**-0.5))
# print(simplify(res[a2]).subs(f1, f*alpha**0.5).subs(f2, f*alpha**-0.5))