import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# A short example for econimic dispatch.
# There are three generators with a squared cost function.
# The cost functions are approximated linear piecewise and solved with linear programming.
# c contains the slopes of the approximated lines.

if __name__ == '__main__':
    c = np.array([12.46, 13.07, 13.58, 11.29, 12.11, 12.82, 11.83, 12.54, 13.20])
    A_eq = np.zeros((9, 9))
    A_eq[0, :] = 1
    b_eq = np.zeros(9)
    b_eq[0] = 267.5
    ll = np.zeros(9)
    uu = np.array([50, 60, 40, 32.5, 60, 20, 45, 50, 40])
    bounds = np.concatenate((ll, uu)).reshape((2, ll.shape[0])).T
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    x_opt = np.round(res.x)
    P = np.array([x_opt[0:3].sum(), x_opt[3:6].sum(), x_opt[6:].sum()])
    print('x_optimal: ' + str(x_opt))
    print('P' + str(P))