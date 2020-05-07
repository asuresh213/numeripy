import numpy as np
import matplotlib.pyplot as plt

Notes_euler = '''
Euler's method:
    Function Name: Euler

    Inputs: f: defining function ( from y' = f(t,y) )
            a: starting Time
            b: ending Time
            y0: Initial Condition
            h: stepsize
            plot: Binary input
                Default plot = 0: No plotting
                        plot = 1: plots the solution

    Outputs: [t, y] where
        y: solution array
        t: time axis
'''


def Euler(f, a, b, y0, h, plot = 0):
    t = [a]
    y = [y0]
    N = int((b-a)/h)
    for i in range(N):
        y.append(y[-1] + h*f(t[-1], y[-1])) #euler update
        t.append(t[-1] + h) #time update

    if(plot == 1):
        plt.plot(t, y, label = "solution")
        plt.legend()
        plt.show()

    return [t, y]
