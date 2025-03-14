
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp

# Set global precision (number of decimal places)
mp.dps = 50  # Set the precision to 50 decimal places

# Define symbols
D1, D2 = symbols('D1, D2')
x_int = Symbol("x_int")
S1, S2 = symbols('S1, S2')
Kd1, Kr1 = symbols('Kd1, Kr1')
Kd2, Kr2 = symbols('Kd2, Kr2')
u_0, u_L = symbols('c_0, c_L')
a1, a2, b1, b2 = symbols('a1, a2, b1, b2')
x_L = Symbol('L')
x_0 = 0
x = Symbol("x")
P = Symbol("P")
u_L = 0

u1 = a1*x + b1
u2 = a2*x + b2

# Define the system of equations
equations = [
    u1.subs(x, x_int)/S1 - u2.subs(x, x_int)/S2,  # Continuity at x_int
    D1*diff(u1, x).subs(x, x_int) - D2*diff(u2, x).subs(x, x_int),  # Flux continuity at x_int
    diff(u1, x).subs(x, x_0) - Kd1*P + Kr1*u1.subs(x, x_0)**2,  # Neumann boundary at x_0
    diff(u1, x).subs(x, x_L) - Kr2*u2.subs(x, x_L)**2  # Neumann boundary at x_L
]

# Substitute numerical values into the parameters
params = {
    D1: 6e-11,  # inconel
    D2: 1.54e-11,  # 316l steel
    S1: sqrt(3e13/(2.68e-30)),
    S2: sqrt(8e11/(2.4e-33)),
    x_0: 0,
    x_int: 0.001,
    x_L: 0.01,
    P: 100000,
    Kd1: 3e13,  # or 6e16
    Kr1: 2.68e-30,
    Kd2: 8e11,  # or 6e16
    Kr2: 2.4e-33,  # or 2e-28
}

# Substitute values into equations
equations_subs = [eq.subs(params) for eq in equations]

# Solve the system numerically
solution = nsolve(equations_subs, [a1, a2, b1, b2], [1, 1, 1, 1])

# Extract the numerical values for a1, a2, b1, b2
a1_num, a2_num, b1_num, b2_num = solution

print(f"a1: {a1_num}, a2: {a2_num}, b1: {b1_num}, b2: {b2_num}")

# Define the solutions for u1 and u2 using the numeric values
u1_sol = a1_num * x + b1_num
u2_sol = a2_num * x + b2_num

# Generate x values for the solution
x1_vals = np.linspace(params[x_0], params[x_int], 100)
x2_vals = np.linspace(params[x_int], params[x_L], 100)

u1_vals = [u1_sol.subs(x, xi) for xi in x1_vals]
u2_vals = [u2_sol.subs(x, xi) for xi in x2_vals]

# Print boundary conditions to check
print(f"C1 = {u1_vals[0]}")
print(f"C2 = {u2_vals[-1]}")

# Calculate W (diffusion-limited reaction)
W = params[Kd1] * params[P] * (
    params[D2] * (params[x_int] - params[x_0]) / params[S1] +
    params[D1] * (params[x_L] - params[x_int]) / params[S2]
) / (params[D2] * params[D1] * params[P] ** 0.5)

print(f"W = {W}")
print("Diffusion limited")

# Plot the solutions
plt.figure(figsize=(8, 5))
plt.plot(x1_vals, u1_vals, label="u1(x)", color="blue")
plt.plot(x2_vals, u2_vals, label="u2(x)", color="red")
plt.axvline(params[x_int], linestyle="--", color="black", label="x_int")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.grid()
plt.show()