"""Coating on the inside
"""
from sympy import *


e = Symbol("e")
D1, D2 = symbols('D1, D2')
# x_int = Symbol("x_int")
S1, S2 = symbols('S1, S2')
u_0, u_L = symbols('c_0, c_L')
a1, a2, b1, b2 = symbols('a1, a2, b1, b2')
L = Symbol('L')
r_0 = Symbol("r_0")
r = Symbol("r")

u1 = a1*log(r) + b1
u2 = a2*log(r) + b2

list_of_equations = [
    u1.subs(r, r_0 + e)/S1 - u2.subs(r, r_0 + e)/S2,
    D1*(r*diff(u1, r)).subs(r, r_0 + e) - D2*(r*diff(u2, r)).subs(r, r_0 + e),
    u1.subs(r, r_0) - u_0,
    u2.subs(r, r_0 + L + e) - u_L
]

# for some reason takes a bit of time...
res = solve(list_of_equations, a1, a2, b1, b2)


def compute_flux(e, r_0, D1, D2, S1, S2, L, c_0):
    new_a = res[a2]
    new_a = new_a.subs("e", e)
    new_a = new_a.subs("r_0", r_0)
    new_a = new_a.subs("D1", D1)
    new_a = new_a.subs("S1", S1)
    new_a = new_a.subs("c_0", c_0)
    new_a = new_a.subs("c_L", 0)
    new_a = new_a.subs("L", L)
    new_a = new_a.subs("D2", D2)
    new_a = new_a.subs("S2", S2)
    flux = -D2 * new_a
    return flux


def compute_PRF_coating_inside(e, r_0, D1, D2, S1, S2, L, pressure):
    flux_with_barrier = compute_flux(e, r_0 - e, D1, D2, S1, S2, L, pressure**0.5*S1)
    flux_wo_barrier = compute_flux(0, r_0 , D2, D2, S2, S2, L, pressure**0.5*S2)
    return flux_wo_barrier/flux_with_barrier


PRF_inside = simplify(compute_PRF_coating_inside(
            e=e, r_0=r_0, D1=D1, S1=S1,
            D2=D2, S2=S2, L=L, pressure=Symbol("P")))


if __name__ == "__main__":
    print(PRF_inside)
    print(latex(PRF_inside))
