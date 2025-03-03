from sympy import *

# non normalised
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
u2 = -1/2*f/D2*x**2 + a2*x

list_of_equations = [
    u1.subs(x, x_int)/S1 - u2.subs(x, x_int)/S2,  # Continuity at x_int
    D1*diff(u1, x).subs(x, x_int) - D2*diff(u2, x).subs(x, x_int),  # Flux continuity at x_int
    u1.subs(x, x_L),  # Concentration = 0 at x_L
    # diff(u2, x).subs(x, x_L),  # Neumann boundary condition: flux = 0 at x_L
    # diff(u1, x).subs(x, x_0),  # Neumann boundary condition: flux = 0 at x_L
]

res = solve(list_of_equations, a1, a2, b1)

print(simplify(res[a1]))
print(simplify(res[a2]))
print(simplify(res[b1]))





import numpy as np
import matplotlib.pyplot as plt

# Substitute numerical values for all parameters into the solutions
params = {
    D1: 1.0,
    D2: 10.0,
    S1: 1.0,
    S2: 5.0,
    x_int: 0.2,
    x_L: 1.0,
    f: 1.0
}

# Substitute the solutions into u1 and u2 and evaluate them numerically
u1_sol = u1.subs(res).subs(params)
u2_sol = u2.subs(res).subs(params)

# Now evaluate the symbolic expressions to ensure no symbolic variables remain
u1_num = lambdify(x, u1_sol, "numpy")
u2_num = lambdify(x, u2_sol, "numpy")

# Generate x values for plotting
x1_vals = np.linspace(x_0, params[x_int], 100)
x2_vals = np.linspace(params[x_int], params[x_L], 100)

# Compute numerical values for u1 and u2
u1_vals = u1_num(x1_vals)
u2_vals = u2_num(x2_vals)

# Plot the solution
plt.figure(figsize=(8, 5))
plt.plot(x1_vals, u1_vals, label="u1(x)", color="blue")
plt.plot(x2_vals, u2_vals, label="u2(x)", color="red")
plt.axvline(params[x_int], linestyle="--", color="black", label="x_int")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.grid()
plt.show()





# # normalized

# c_L = Symbol('c_L')
# c_0 = 1
# alpha, beta, gamma = symbols('alpha, beta, gamma')
# a1, a2, b1, b2 = symbols('a1, a2, b1, b2')
# x_L = 1
# x_0 = 0
# x = Symbol("x")
# f1 = Symbol("f1")
# f2 = Symbol("f2")

# # Define the normalized solutions
# u1 = -1/2*f1*x**2 + a1*x + b1
# u2 = -1/2*f2*x**2 + a2*x + b2

# # Create the system of equations for the normalized boundary and continuity conditions
# list_of_equations = [
#     u1.subs(x, gamma)*beta - u2.subs(x, gamma),  # Continuity at gamma
#     diff(u1, x).subs(x, gamma) - alpha*diff(u2, x).subs(x, gamma),  # Flux continuity at gamma
#     diff(u1, x).subs(x, x_0),  # Neumann boundary condition: flux = 0 at x_0
#     diff(u2, x).subs(x, x_L),  # Neumann boundary condition: flux = 0 at x_L
# ]

# # Solve the system for the normalized coefficients a1, a2, b1, b2
# res = solve(list_of_equations, a1, a2, b1, b2)

# # Output the results for the normalized case
# print(simplify(res[a1]).subs(f1, f*alpha**0.5).subs(f2, f*alpha**-0.5))
# print(simplify(res[a2]).subs(f1, f*alpha**0.5).subs(f2, f*alpha**-0.5))