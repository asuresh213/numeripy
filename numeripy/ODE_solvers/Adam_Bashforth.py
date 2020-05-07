import numpy as np
import matplotlib.pyplot as plt

'''
Adam Bashforth m step method:
    Function Name: adam_bashforth

    Inputs: f: defining function ( from y' = f(t,y) )
            a: starting Time
            b: ending Time
            alpha: Initial Condition
            h: stepsize
            type: # of steps (the 'm' in m-step scheme)
                                m = 2,3,4 or 5
            N = (optional) to override the number of iterations
                default: N = 0 for normal Adam Bashforth explicit
                    reset N to any finite number i to get i iterations.
                        (i >= type-1, for obvious reasons)
            plot: Binary input
                Default plot = 0: No plotting
                        plot = 1: plots the solution

    Outputs: [t, y]: where
                t: time axis
                y: solution array
'''

#--------------------- RK 4th order method ---------------------------

def RK4_method(f, a, b, t, y, h, N=0):
    if(N == 0):
        N = int((b-a)/h)

    for i in range(N):
        k1 = h*f(t[-1], y[-1])
        yp2 = y[-1] + k1/2
        k2 = h*f(t[-1]+h/2, yp2)
        yp3 = y[-1] + k2/2
        k3 = h*f(t[-1]+h/2, yp3)
        yp4 = y[-1] + k3
        k4 = h*f(t[-1]+h, yp4)
        val = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y.append(y[-1] + val)
        t.append(t[-1] + h)
    return t, y


#----------------- Adam Bashforth explicit methods --------------------

#Adam Bashforth handler
def adam_bashforth(f, a, b, alpha, h, type, N = 0, plot = 0):
    t = [a]
    y = [alpha]
    t, y = RK4_method(f, a, b, t, y, h, type - 1)
    if(N == 0):
        N = int(((b-a)/h) - (type-1))

    if(type == 2):
        t, y = abf2(f, y, t, h, N)
        if(plot == 1):
            plt.plot(t, y, label = "AB %s step solution"%type)
            plt.legend()
            plt.show()

    if(type == 3):
        t, y = abf3(f, y, t, h, N)
        if(plot == 1):
            plt.plot(t, y, label = "AB %s step solution"%type)
            plt.legend()
            plt.show()

    if(type == 4):
        t, y = abf4(f, y, t, h, N)
        if(plot == 1):
            plt.plot(t, y, label = "AB %s step solution"%type)
            plt.legend()
            plt.show()

    if(type == 5):
        t, y = abf5(f, y, t, h, N)
        if(plot == 1):
            plt.plot(t, y, label = "AB %s step solution"%type)
            plt.legend()
            plt.show()

    return [t, y]

#2 step Adam Bashforth
def abf2(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/2)*(3*f(t[-1], y[-1]) - f(t[-2], y[-2])))
        t.append(t[-1] + h)
    return t, y

#3 step Adam Bashforth
def abf3(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/12)*(23*f(t[-1], y[-1]) - 16*f(t[-2], y[-2]) \
                                + 5*f(t[-3], y[-3])))
        t.append(t[-1] + h)
    return t, y

#4 step Adam Bashforth
def abf4(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/24)*(55*f(t[-1], y[-1]) - 59*f(t[-2], y[-2]) \
                                    + 37*f(t[-3], y[-3]) - 9*f(t[-4], y[-4])))
        t.append(t[-1] + h)
    return t, y

#5 step Adam bashforth
def abf5(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/720)*(1901*f(t[-1], y[-1]) - 2774*f(t[-2], y[-2]) \
                                + 2616*f(t[-3], y[-3]) - 1274*f(t[-4], y[-4]) \
                                +251*f(t[-5], y[-5])))
        t.append(t[-1] + h)
    return t, y
