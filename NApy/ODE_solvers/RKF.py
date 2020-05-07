import numpy as np
import matplotlib.pyplot as plt

#---------------------- Runge-Kutta-Fehlberg method ------------------
Notes = '''
Runge-Kutta Fehlberg:
    Function Name: RKF_method

    Inputs: f: defining function ( from y' = f(t,y) )
            a: starting Time
            b: ending Time
            alpha: Initial Condition
            tol: Tolerance
            hmax: maximum step size
            hmin: minimum step size
            plot: Binary input
                Default plot = 0: No plotting
                        plot = 1: plots the solution

    Outputs: y: solution array
             t: time array
             step: stepsize array
'''

def RKF(f, a, b, alpha, tol, hmax, hmin, plot = 0):
    t = a
    w = alpha
    h = hmax
    flag = 1
    time = [a] #time array
    y = [alpha] #solution array
    step = [hmax] #step size array
    while(flag == 1):
        k1 = h*f(t, w)
        k2 = h*f(t + (1/4)*h, w + (1/4)*k1)
        k3 = h*f(t + (3/8)*h, w + (3/32)*k1 + (9/32)*k2)
        k4 = h*f(t + (12/13)*h, w + (1932/2197)*k1 - (7200/2197)*k2 + (7296/2197)*k3)
        k5 = h*f(t + h, w + (439/216)*k1 - (8)*k2 + (3680/513)*k3 - (845/4104)*k4)
        k6 = h*f(t + (1/2)*h, w - (8/27)*k1 + (2)*k2 - (3544/2565)*k3 + (1859/4104)*k4 - (11/40)*k5)
        R = (1/h)*np.abs((1/360)*k1 - (128/4275)*k3 - (2197/75240)*k4 + (1/50)*k5 + (2/55)*k6)
        if(R <= tol):
            t += h
            w += (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5
            time.append(t)
            step.append(h)
            y.append(w)
        delta = 0.84*(tol/R)**(1/4)
        if(delta <= 0.1):
            h = 0.1*h
            step.append(h)
        elif(delta >= 4):
            h = 4*h
            step.append(h)
        else:
            h = delta*h
            step.append(h)
        if(h > hmax):
            h = hmax
            step[-1] = h
        if(t >= b):
            flag = 0
        elif(t + h > b):
            h = b - t
            step[-1] = h
        elif(h<hmin):
            flag = 0
            print("min h exceeded")
            print("completed unsuccessfully")

    if(plot == 1):
        plt.plot(y, time, label = "RKF Solution")
        plt.legend()
        plt.show()

    return y, time, step
