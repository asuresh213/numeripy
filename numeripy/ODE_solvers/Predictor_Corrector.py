import numpy as np
import matplotlib.pyplot as plt

Notes = '''
Predictor Corrector scheme (Predictor: Adam Bashforth; Corrector: Adam-Moulton)
    Function Name: predict_correct

    Inputs: f: defining function ( from y' = f(t,y) )
            t: Initial time array [a]
            y: Initial solution array [alpha]
            pred: # steps for predictor (the 'm' in Adam Bashforth m-step)
            corr: # steps for corrector (the 'm' in Adam Moulton m-step)
            alpha: Initial Condition
            a: Initial time
            b: Final time
            h: Step size

    Outputs: y: Solution array


Adams variable stepsize predictor corrector

    Note: This method uses 4 step Adam bashforth and 3 step Adam Moulton
    as Predictor and Corrector Respectively.

    Function Name: Adam_PC_variable_step

    Inputs: f: defining function ( from y' = f(t,y) )
            t: Initial time array [a]
            y: Initial solution array [alpha]
            a: Initial time
            b: Final time
            tol: Tolerance value
            hmax: maximum stepsize
            hmin: minimum stepsize

    Outputs: Index: Array of indices (as time array is not of uniform step size)
             t: Time array
             y: Solution array
             h: Step size array

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

def adam_bashforth(f, a, b, alpha, h, type, N = 0):
    t = [a]
    y = [alpha]
    t, y = RK4_method(f, a, b, t, y, h, type - 1)
    if(N == 0):
        N = int(((b-a)/h)- (type-1))

    if(type == 2):
        y = abf2(f, y, t, h, N)
    if(type == 3):
        y = abf3(f, y, t, h, N)
    if(type == 4):
        y = abf4(f, y, t, h, N)
    if(type == 5):
        y = abf5(f, y, t, h, N)

    return y

#2 step Adam Bashforth
def abf2(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/2)*(3*f(t[-1], y[-1]) - f(t[-2], y[-2])))
        t.append(t[-1] + h)
    return y

#3 step Adam Bashforth
def abf3(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/12)*(23*f(t[-1], y[-1]) - 16*f(t[-2], y[-2]) \
                                + 5*f(t[-3], y[-3])))
        t.append(t[-1] + h)
    return y

#4 step Adam Bashforth
def abf4(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/24)*(55*f(t[-1], y[-1]) - 59*f(t[-2], y[-2]) \
                                    + 37*f(t[-3], y[-3]) - 9*f(t[-4], y[-4])))
        t.append(t[-1] + h)
    return y

#5 step Adam bashforth
def abf5(f, y, t, h, N):
    for i in range(N):
        y.append(y[-1] + (h/720)*(1901*f(t[-1], y[-1]) - 2774*f(t[-2], y[-2]) \
                                + 2616*f(t[-3], y[-3]) - 1274*f(t[-4], y[-4]) \
                                +251*f(t[-5], y[-5])))
        t.append(t[-1] + h)
    return y


#----------------------------------------------------------------------


#------ Adam Moulton Implicit method (for predictor corrector)----------

#Adam Moulton method handler
def adam_moulton(f, t, y, h, type, wp):

    if(type == 2):
        t, y = abm2(f, y, t, h, 1, wp)
    if(type == 3):
        t, y = abm3(f, y, t, h, 1, wp)
    if(type == 4):
        t, y = abm4(f, y, t, h, 1, wp)

    return t, y

#2 step Adam Moulton
def abm2(f, y, t, h, N, wp):
    for i in range(N):
        y.append(y[-1] + (h/12)*(5*f(t[-1] + h, wp) + 8*f(t[-1], y[-1]) \
                            - f(t[-2], y[-2])))
        t.append(t[-1] + h)
    return t, y

#3 step Adam Moulton
def abm3(f, y, t, h, N, wp):
    for i in range(N):
        y.append(y[-1] + (h/24)*(9*f(t[-1]+h, wp) + 19*f(t[-1], y[-1]) \
                                - 5*f(t[-2], y[-2]) + f(t[-3], y[-3])))
        t.append(t[-1] + h)
    return t, y

#4 step Adam Moulton
def abm4(f, y, t, h, N, wp):
    for i in range(N):
        y.append(y[-1] + (h/720)*(251*f(t[-1]+h, wp) + 646*f(t[-1], y[-1]) \
                                - 264*f(t[-2], y[-2]) + 106*f(t[-3], y[-3]) \
                                -19*f(t[-4], y[-4])))
        t.append(t[-1] + h)
    return t, y


#--------------- Predictor Corrector -------------------------

def predict_correct(f, alpha, a, b, pred, corr,  var_step = 0, plot = 0):
    t = [a]
    y = [alpha]
    if(var_step == 1):
        print("Using pred = 4, corr = 3")
        hmax = float(input("Enter maximum threshold for step-size: "))
        hmin = float(input("Enter minimum threshold for step-size: "))
        tol = float(input("Enter tolerance value: "))
        index, t, y, step = Adam_PC_variable_step(f, t, y, a, b, hmax, hmin, tol)
        if(plot == 1):
            plt.plot(t, y, label = "Variable h PC")
            plt.legend()
            plt.show()
        return [t, y, step]

    h = float(input("Enter the step-size: "))
    N = int(((b-a)/h)- (pred-1))
    t, y = RK4_method(f, a, b, t, y, h, pred - 1)
    for i in range(N):
        #the following predictor is very inefficient.
        #But it works for smaller problems.
        #It can, and will be optimized in further updates

        wp_arr = adam_bashforth(f, a, b, alpha, h, pred, i+1)
        wp = wp_arr[-1]
        t, y = adam_moulton(f, t, y, h, corr, wp)
    if(plot == 1):
        plt.plot(t, y, label = "Predictor Corrector Solution")
        plt.legend()
        plt.show()

    return [t, y]

#-------------------------------------------------------------

#------------------------------------------------------------
#Adam's Predictor Corrector method with variable step size

def Adam_PC_variable_step(f, t, y, a, b, tol, hmax, hmin):
    def RK4(h, v0, x0):
        x = [x0, 0, 0, 0]
        v = [v0, 0, 0, 0]
        for j in range(1,4):
            k1 = h*f(x[j-1], v[j-1])
            k2 = h*f(x[j-1] + h/2, v[j-1] + k1/2)
            k3 = h*f(x[j-1] + h/2, v[j-1] + k2/2)
            k4 = h*f(x[j-1] + h, v[j-1] + k3)
            v[j] = v[j-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
            x[j] = x[j-1] + h

        return x[1:], v[1:]

    index = [0]
    step = [hmax]
    t0 = a
    w0 = y[0]
    h = hmax
    flag = 1
    last = 0

    tpr, ypr = RK4(h, w0, t0)
    for i in range(len(tpr)):
        t.append(tpr[i])
        y.append(ypr[i])


    nflag = 1
    i = 4
    time = t[i-1] + h

    while(flag == 1):
        wp = y[i-1] + (h/24)*(55*f(t[i-1], y[i-1]) - 59*f(t[i-2], y[i-2]) \
                                    + 37*f(t[i-3], y[i-3]) - 9*f(t[i-4], y[i-4]))
        wc = y[i-1] + (h/24)*(9*f(time, wp) + 19*f(t[i-1], y[i-1]) \
                                - 5*f(t[i-2], y[i-2]) + f(t[i-3], y[i-3]))
        sigma = (19/(270*h))*np.abs(wc - wp)

        if(sigma < tol):

            y.append(wc)
            t.append(time)

            if(nflag == 1):
                for j in range(i-3, i+1):
                    step.append(h)
                    index.append(j)
            else:
                step.append(h)
                index.append(i)

            if(last == 1):
                flag = 0
            else:
                i = i + 1
                nflag = 0

                if(sigma < 0.1*tol or t[i-1] + h > b):

                    q = (tol/(2*sigma))**(1/4)

                    if(q > 4):
                        h = 4*h
                    else:
                        h = q*h

                    if(h > hmax):
                        h = hmax

                    if(t[i-1] + 4*h > b):
                        h = (b - t[i-1])/4
                        last = 1

                    temp1 = []
                    temp2 = []
                    temp1, temp2 = RK4(h, y[i-1], t[i-1])
                    for v in range(len(temp1)):
                        t.append(temp1[v])
                        y.append(temp2[v])
                    nflag = 1
                    i = i+3

        else:

            q = (tol/(2*sigma))**(1/4)


            if(q < 0.1):
                h = 0.1*h
            else:
                h = q*h
            if(h < hmin):
                flag = 0
                print("min h exceeded")
            else:
                if(nflag == 1):
                    i = i-3
                y = y[:i]
                t = t[:i]
                temp3 = []
                temp4 = []
                temp3, temp4 = RK4(h, y[i-1], t[i-1])

                for v in range(len(temp3)):
                    t.append(temp3[v])
                    y.append(temp4[v])
                i = i+3
                nflag = 1
        time = t[i-1] + h
    return index, t, y, step
