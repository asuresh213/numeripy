import numpy as np
import matplotlib.pyplot as plt

Notes_m_euler = '''
Modified Euler's method:
    Function Name: modified_euler

    Inputs: f: defining function ( from y' = f(t,y) )
            a: starting Time
            b: ending Time
            alpha: Initial Condition
            h: stepsize
            plot: Binary input
                Default plot = 0: No plotting
                        plot = 1: plots the solution

    Outputs: [t, y] where
        y: solution array
        t: time axis
'''
def modified_euler(f, a, b, alpha, h, plot = 0):
    t = [a]
    y = [alpha]
    N = int((b-a)/h)
    for i in range(N):
        val = f(t[-1],y[-1])
        y.append(y[-1]  + (h/2)*(val + f(t[-1]+h, y[-1]+h*val)))
        t.append(t[-1] + h)

    if(plot == 1):
        plt.plot(t, y, label = "Modified Euler Solution")
        plt.legend()
        plt.show()

    return [t, y]
