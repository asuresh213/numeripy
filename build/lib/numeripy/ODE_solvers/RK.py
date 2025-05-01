import numpy as np
import matplotlib.pyplot as plt

Notes = '''
RK for systems (of m equations):
    Note: This function was heavily influenced by the style of Dr. Andasari (BU)
    website: http://people.bu.edu/andasari/courses/numericalpython/python.html

    Function Name: RK4_sys

    Inputs: func: The defining functions written in the following style
                func(t, y):
                    dy = [0, 0, ..., 0]
                    dy[0] = u1' = f1(t, y[j]); j in 1,2,..., m
                    dy[1] = u2' = f2(t, y[j]); j in 1,2,..., m
                    .
                    .
                    .
                    dy[m] = um' = fm(t, y[j]); j in 1,2,..., m
                    return dy
            yinit: Array of initial conditions [u1(a), u2(a), ..., um(a)]

            x_range: The array [a, b]

            h: stepsize

    Outputs:
            [tsol, ysol]:
                ysol: An array of arrays of solutions [u1, u2, ..., um]
                tsol: Time axis
'''


def RK(f, yinit, a, b, h, order = 4, plot = 0):
    if(order == 3):
        [xsol, solutions] = RK3(f, yinit, a, b, h,  plot = plot)
        return [xsol, solutions]
    if(order == 4):
        [xsol, solutions] = RK4(f, yinit, a, b, h,  plot = plot)
        return [xsol, solutions]
    if(order == 6):
        [xsol, solutions] = RK6(f, yinit, a, b, h,  plot = plot)
        return [xsol, solutions]
    else:
        print("Orders supported: 3, 4 and 6")

    return 0


#---------------------------RK 3rd order method--------------------------------
def RK3(f, yinit, a, b, h,  plot = 0):

    m = len(yinit)
    n = int((b - a)/h)

    x = a
    y = yinit

    # Containers for solutions
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = f(x, y)
        yp2 = y + k1*(h/2)
        k2 = f(x+h/2, yp2)
        yp3 = y - k1*h + 2*k2*h
        k3 = f(x+h, yp3)
        for j in range(m):
            y[j] = y[j] + (h/6)*(k1[j] + 4*k2[j] + k3[j])
        x = x + h
        xsol = np.append(xsol, x)
        for r in range(len(y)):
            ysol = np.append(ysol, y[r])

    solutions = []
    for q in range(m):
        temp = ysol[q::m]
        solutions.append(temp)
        temp = []
    if(plot == 1):
        for i in range(len(solutions)):
            plt.plot(xsol, solutions[i], label = "u_%s"%(i+1))
        plt.legend()
        plt.show()
    return [xsol, solutions]


#--------------------- RK 4th order method ---------------------------

def RK4(f, yinit, a, b, h,  plot = 0):

    m = len(yinit)
    n = int((b - a)/h)

    x = a
    y = yinit

    # Containers for solutions
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = f(x, y)
        yp2 = y + k1*(h/2)
        k2 = f(x+h/2, yp2)
        yp3 = y + k2*(h/2)
        k3 = f(x+h/2, yp3)
        yp4 = y + k3*h
        k4 = f(x+h, yp4)
        for j in range(m):
            y[j] = y[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])
        x = x + h
        xsol = np.append(xsol, x)
        for r in range(len(y)):
            ysol = np.append(ysol, y[r])

    solutions = []
    for q in range(m):
        temp = ysol[q::m]
        solutions.append(temp)
        temp = []
    if(plot == 1):
        for i in range(len(solutions)):
            plt.plot(xsol, solutions[i], label = "u_%s"%(i+1))
        plt.legend()
        plt.show()
    return [xsol, solutions]

#------------------------ RK6th order -------------------------------

def RK6(f, yinit, a, b, h,  plot = 0):

    m = len(yinit)
    n = int((b - a)/h)

    x = a
    y = yinit

    # Containers for solutions
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = h*f(x, y)
        yp2 = y + k1
        k2 = h*f(x+h, yp2)
        yp3 = y + (1/8)*(3*k1 + k2)
        k3 = h*f(x+h/2, yp3)
        yp4 = y + (1/27)*(8*k1 + 2*k2 + 8*k3)
        k4 = h*f(x+ (2*h/3), yp4)
        yp5 = y + (1/392)*(3*(3*np.sqrt(21) -7)*k1 - 8*(7-np.sqrt(21))*k2 + 48*(7-np.sqrt(21))*k3 - 3*(21 - np.sqrt(21))*k4 )
        k5 = h*f(x + (h/14)*(7-np.sqrt(21)), yp5)
        yp6 = y + (1/1960)*(-5*(231 + 51*np.sqrt(21))*k1 - 40*(7 + np.sqrt(21))*k2 - 320*np.sqrt(21)*k3 + 3*(21 + 121*np.sqrt(21))*k4 + 392*(6 + np.sqrt(21))*k5)
        k6 = h*f(x + (h/14)*(7+np.sqrt(21)), yp6)
        yp7 = y + (1/180)*(15*(22 + 7*np.sqrt(21))*k1 + 120*k2 + 40*(7*np.sqrt(21) - 5)*k3 - 63*(3*np.sqrt(21) -2)*k4 - 14*(49 + 9*np.sqrt(21))*k5 + 70*(7-np.sqrt(21))*k6)
        k7 = h*f(x+h, yp7)

        for j in range(m):
            y[j] = y[j] + (1/180)*(9*k1[j] + 64*k2[j] + 49*k5[j] + 49*k6[j] + 9*k7[j])
        x = x + h
        xsol = np.append(xsol, x)
        for r in range(len(y)):
            ysol = np.append(ysol, y[r])

    solutions = []
    for q in range(m):
        temp = ysol[q::m]
        solutions.append(temp)
        temp = []
    if(plot == 1):
        for i in range(len(solutions)):
            plt.plot(xsol, solutions[i], label = "u_%s"%(i+1))
        plt.legend()
        plt.show()
    return [xsol, solutions]
