import numpy as np
import matplotlib.pyplot as plt

Notes = '''
nth order Taylor method (n = 2, 3, 4, 5):
    Function Name: Taylor

    Inputs: y0: Initial condition
            h = step size
            a: starting Time
            b: ending Time
            plot: Binary input
                Default plot = 0: No plotting
                        plot = 1: plots the solution
            F = f (the defining function y' = f(t, y))
            Fpr = derivative of f
            F2pr = second derivative of f
            F3pr = third derivative of f
            F4pr = fourth derivative of f

            Specify only to requirement.
                -------Example 1:

                Suppose we want to use 2nd order Taylor. Then define
                functions f and f' then call function as follows

                def Taylor(y0, h, a, b, plot = 0, F=f, Fpr=f'):

                -------Example 2:

                Suppose we want to use 3rd order Taylor. Then define
                functions f, f' and f'' then call function as follows

                def Taylor(y0, h, a, b, plot = 0, F=f, Fpr=f', F2pr = f''):


    Output:  [t, y] where
                y: solution array
                t: time array

'''
def temp_func(t, y):
    return 0

#Computing T^(n)
def T_n(t, y, h, F, Fpr, F2pr, F3pr, F4pr):
    if(F==0):
        F = temp_func
    if(Fpr==0):
        Fpr = temp_func
    if(F2pr==0):
        F2pr = temp_func
    if(F3pr==0):
        F3pr = temp_func
    if(F4pr==0):
        F4pr = temp_func
    return F(t, y)+(h/2)*(Fpr(t,y))+(h**2/6)*(F2pr(t,y))+(h**3/24)*(F3pr(t,y)) + (h**4/120)*(F4pr(t, y))


def Taylor(y0, h, a, b, plot = 0, F=0, Fpr=0, F2pr=0, F3pr=0, F4pr=0):
    t = [a]
    y = [y0]
    N = int((b-a)/h)
    for i in range(N):
        y.append(y[-1] + h*(T_n(t[-1], y[-1], h, F, Fpr, F2pr, F3pr, F4pr)))
        t.append(t[-1] + h)
    if(plot == 1):
        plt.plot(t, y, label = 'solution')
        plt.legend()
        plt.show()
    return [t, y]
