import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

m = 5
B = 10.0
a = np.ones(m)
epsilon = 1e-6
rng = np.random.default_rng(42)

def risk(x):
    x = np.asarray(x, dtype=float)
    return a / (x + epsilon)

def total_risk(x):
    r = risk(x)
    return float(np.max(r) * np.sum(r))

# random baseline
x_random = rng.dirichlet(np.ones(m)) * B
pre_total = total_risk(x_random)

constraints = [{"type": "ineq", "fun": lambda x: B - np.sum(x)}]
bounds = [(0.0, None) for _ in range(m)]
x0 = np.full(m, B / m)

# ---- log every function evaluation ----
history = []
def total_risk_logged(x):
    val = total_risk(x)
    history.append(val)
    return val

result = minimize(
    total_risk_logged,
    x0,
    method="SLSQP",
    bounds=bounds,
    constraints=constraints,
    options={"maxiter": 500, "ftol": 1e-12, "disp": False},
)

if not result.success:
    raise RuntimeError(f"Optimization failed: {result.message}")

x_opt = result.x
post_total = total_risk(x_opt)

# Plot 1: two bars
plt.figure()
labels = ["Random (pre)", "Optimized (post)"]
values = [pre_total, post_total]
plt.bar(labels, values)
plt.ylabel("Total Risk = max(R_i) + sum(R_i)")
plt.title("Total Risk: Random vs Optimized")
plt.grid(axis="y", alpha=0.3)
for i, v in enumerate(values):
    plt.text(i, v, f"{v:.6f}", ha="center", va="bottom", fontsize=10)
plt.show()

