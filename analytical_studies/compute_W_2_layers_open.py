import sympy as sp

# Define symbols
Kd1, Kd2, Kr1, Kr2, Ks1, Ks2= sp.symbols('Kd1 Kd2 Kr1 Kr2 Ks1 Ks2')
c1, cm1, cm2, c2 = sp.symbols('c1 cm1 cm2 c2')
D1, D2 = sp.symbols('D1 D2')
P = sp.Symbol('P')
x = sp.Symbol('x')
xL, xint, x0 = sp.symbols('xL xint x0')
e1, e2 = sp.symbols('e1 e2')

# Flux balance
expr1 = Kd1*P - Kr1*c1**2
expr2 = -D1*(c1 - cm2/Ks2*Ks1)/x
expr3 = -D2*(cm2/Ks1*Ks2 - c2)/x
exprD = -D2*((D1*(xL-xint)*c1 + D2*(xint-x0)*c2)/(D2*(xint-x0) + D1*(xL-xint)*Ks1/Ks2) - c2)
expr4 = Kr2*c2**2

# Dimensionless surface limited flux
JSL = Kd1*P * (1 + (Kr1-Kr2)/(Kr1+Kr2))

# Flux continuity equations
eq1 = sp.Eq(expr1/JSL, expr2/JSL)
eq2 = sp.Eq(expr2/JSL, expr3/JSL)
eq3 = sp.Eq(expr3/JSL, expr4/JSL)

eq1 = sp.Eq(expr1/JSL, exprD/JSL)
eq2 = sp.Eq(exprD/JSL, expr4/JSL)
# eq4 = sp.Eq(Ks1, (Kd1/Kr1)**(1/2))

# Combine them
# all_eqs = sp.And(eq1, eq2, eq3)
all_eqs = sp.And(eq1, eq2)

# Factoring Eqs
factored_eqs = sp.factor_terms(all_eqs)
sp.pprint(factored_eqs)

print("\n\n\n")

# extracting factors of important vars
important_vars = [c1, c2]
collected_eqs = [sp.collect(eq.lhs - eq.rhs, var) for eq in [eq1, eq2] for var in important_vars]
for eq in collected_eqs:
    sp.pprint(eq)


print('\n\n\n')

u, v = sp.symbols('x, y')
exprD2 = D1*(xL-xint)*(Kd1*Kr1*P)**(-1/2)*v + D2*(xint-x0)*(Kd1*Kr2*P)**(-1/2)*u
factored_expr = exprD2.collect([u, v])
print(factored_expr)

expr5 = (Ks2*(Kd1/Kr1*Kr2/Kd2*P*(1+Kd2/(Kd1+Kd2)))**(1/2))
expr5 = sp.simplify(expr5)
print("\n\n\n\n")
sp.pprint(expr5)

# import sympy as sp

# # Define symbols
# Kd1, Kd2, Kr1, Kr2, Ks1, Ks2 = sp.symbols('Kd1 Kd2 Kr1 Kr2 Ks1 Ks2')
# c1, cm1, cm2, c2 = sp.symbols('c1 cm1 cm2 c2')
# D1, D2 = sp.symbols('D1 D2')
# P, x = sp.symbols('P x')

# # Flux balance
# expr1 = Kd1*P - Kr1*c1**2
# expr2 = -D1*(c1 - cm2 / (Ks2 * Ks1)) / x
# expr3 = -D2*(cm2 / (Ks1 * Ks2) - c2) / x
# expr4 = Kr2*c2**2

# # Dimensionless surface-limited flux
# JSL = Kd1*P * (1 + (Kr1 - Kr2) / (Kr1 + Kr2))

# # Flux continuity equations
# eq1 = sp.Eq(expr1 / JSL, expr2 / JSL)
# eq2 = sp.Eq(expr2 / JSL, expr3 / JSL)
# eq3 = sp.Eq(expr3 / JSL, expr4 / JSL)

# # Convert equations to expressions for simplification
# eqs_exprs = [eq.lhs - eq.rhs for eq in [eq1, eq2, eq3]]

# # Factors to extract
# factor1 = c1 / (Ks1 * sp.sqrt(P))
# factor2 = c2 / (Ks2 * sp.sqrt(P))

# # Collecting expressions with respect to the factors
# factored_exprs = [sp.collect(expr, [factor1, factor2]) for expr in eqs_exprs]

# # Convert back to equations
# factored_eqs = [sp.Eq(expr, 0) for expr in factored_exprs]

# # Print results
# for eq in factored_eqs:
#     sp.pprint(eq)