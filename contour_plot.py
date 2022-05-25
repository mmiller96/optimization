import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.latex.preamble']=[r"\usepackage{lmodern}"]
params = {'text.usetex' : True,
          'font.size' : 24,
          'font.family' : 'lmodern',
          }
plt.rcParams.update(params) 

# shows the concept of the lagriange multipliers by a simple example
# f(x, y) is the objective function
# g(x, y) is the constraint function
# the gradient vectors of f and g have to be parallel and the found solution should match with the constraint (g(x, y)=0)
# --> optimal solution

if __name__ == "__main__":
    def f(x, y):
        return 2*x + y 
    def grad_fx(x, y):
        return 2
    def grad_fy(x, y):
        return 1

    def g(x, y):
        return x**2 + y**2
    def grad_gx(x, y):
        return 2*x
    def grad_gy(x, y):
        return 2*y

    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    dx = grad_fx(x, y)
    dy = grad_fy(x, y)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    G = g(X, Y)
    
    dg_x = grad_gx(X, Y)
    dg_y = grad_gy(X, Y)

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(5, 3))
    axes[0].set_title(r'$f(x, y) = 2x + y$')
    axes[0].contourf(X, Y, Z, 20, cmap='RdGy')
    axes[0].quiver(X, Y, dx, dy, color='b')
    axes[1].set_title(r'$g(x, y) = x^2 + y^2$')
    axes[1].contourf(X, Y, G, 20, cmap='RdGy')
    axes[1].quiver(X, Y, dg_x, dg_y, color='g')
    axes[2].set_title(r'$\nabla g(x, y) = [2x \; 2y]^T \: \nabla f(x, y) = [2 \; 1]^T$')
    axes[2].quiver(X, Y, dg_x, dg_y, color='g')
    axes[2].quiver(X, Y, dx, dy, color='b')
    plt.show()