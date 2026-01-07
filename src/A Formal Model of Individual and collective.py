import sympy as sp

U = sp.symbols('U1 U2 U3')
r = {U[0]: sp.symbols('r1'), U[1]: sp.symbols('r2'), U[2]: sp.symbols('r3')}
R = sum(r.values())

s = sp.symbols('s', nonnegative=True)
delta = {U[0]: -s, U[1]: 0, U[2]: s}  # U1给U3
r_prime = {u: r[u] + delta[u] for u in U}

print("R:", R)
print("r':", {str(k): str(v) for k,v in r_prime.items()})
print("守恒:", sum(r_prime.values()) - R)  # 0
