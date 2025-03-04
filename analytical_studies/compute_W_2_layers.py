import sympy as sp

# Define symbols
Kd1, Kd2, Kr1, Kr2, Ks1, Ks2= sp.symbols('Kd1 Kd2 Kr1 Kr2 Ks1 Ks2')
c1, cm1, cm2, c2 = sp.symbols('c1 cm1 cm2 c2')
D1, D2 = sp.symbols('D1 D2')
P = sp.Symbol('P')
x = sp.Symbol('x')

# Flux balance
expr1 = Kd1*P - Kr1*c1**2
expr2 = -D1*(c1 - cm2/Ks2*Ks1)/x
expr3 = -D2*(cm2/Ks1*Ks2 - c2)/x
expr4 = Kr2*c2**2

# Dimensionless surface limited flux
JSL = Kd1*P * (1 + (Kr1-Kr2)/(Kr1+Kr2))

# Flux continuity equations
eq1 = sp.Eq(expr1/JSL, expr2/JSL)
eq2 = sp.Eq(expr2/JSL, expr3/JSL)
eq3 = sp.Eq(expr3/JSL, expr4/JSL)

# Combine them
all_eqs = sp.And(eq1, eq2, eq3)

print(all_eqs)