dict1= {
"Euler_key" : ["euler", "eulermethod", "euler'smethod", "forwardeuler"],
"RK_key" : ["rungekutta", "rungekutta4thorder", "rk2", "rk3", "rk4", "rk5",
"rk6", "rungekutta4", "rungekutta2", "rungekutta3", "rungekutta5"],
"AB_key" : ["adambashforth", "ab", "adambashforthexplicit", "adamexplicit"],
"pc_key" : ["predictorcorrector", "pc", "adamspc", "adamsvariablesteppc"
            "adambashforth adammoulton pc, abampc", "variablestepsizepredictorcorrector",
            "pcvariablestepsize", "variablestepsizepc"],
"rkf_key" : ["rungekuttafehlberg", "rkf", "rkfehlberg"],
"taylor_key" : ["taylor", "2ndordertaylor", "secondordertaylor", "3rdordertaylor",
                "thirdordertaylor", "4thordertaylor", "fourthordertaylor",
                "nthordertaylor", "taylorsmethod"],
"meuler_key" : ["modifiedeuler", "meuler", "modifiedforwardeuler", "eulermodified",
                "eulerm", "modifiedeulermethod"]
}






def help(kw = " "):
    if((kw.lower()).replace(" ", "") in dict1["Euler_key"]):
        Notes_euler = '''
        Euler's method:
            Function Name: Euler

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
        print(Notes_euler)

    if((kw.lower()).replace(" ", "") in dict1["meuler_key"]):
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
        print(Notes_m_euler)


    if((kw.lower()).replace(" ", "") in dict1["AB_key"]):
        Notes = '''
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
                                (i >= type-1, because there will be type-1
                                            RK4 runs needed for any AB method)
                    plot: Binary input
                        Default plot = 0: No plotting
                                plot = 1: plots the solution

            Outputs: [t, y]: where
                        t: time axis
                        y: solution array
        '''
        print(Notes)

    if((kw.lower()).replace(" ", "") in dict1["pc_key"]):
        Notes = '''
        Does not work on Atom (involves user input - run from console).

         Predictor Corrector scheme (Predictor: Adam Bashforth; Corrector: Adam-Moulton)
             Function Name: predict_correct

             Inputs: f: defining function ( from y' = f(t,y) )
                     alpha: Initial value of the solution
                     a: Initial time
                     b: Final time
                     pred: # steps for predictor (the 'm' in Adam Bashforth m-step)
                     corr: # steps for corrector (the 'm' in Adam Moulton m-step)
                     var_step: Binary input
                        Default var_step = 0: Runs regular predictor corrector
                                var_step = 1: Runs Adams variable step size predictor corrector
                                                (assumes pred = 4, corr = 3)
                     plot: Binary input
                        Default plot = 0: No plotting
                                plot = 1: Plots the solution

                    !! -- Note: depending on user input for var_step, user inputs are
                            requested for h, max h, min h and tol. -- !!

             Outputs:
                    var_step = 0:
                    [t, y]: where
                                t: time axis
                                y: solution array
                    var_step = 1:
                    [t, y, step]: where
                                    t = time axis
                                    y = solution array
                                    step = step-size array

         '''
        print(Notes)

    if((kw.lower()).replace(" ", "") in dict1["RK_key"]):
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
                    alpha: Array of initial conditions [u1(a), u2(a), ..., um(a)]
                    a: starting time
                    b: ending time
                    h: stepsize
                    plot: Binary input
                       Default plot = 0: No plotting
                               plot = 1: Plots the solution


            Outputs:
                    [tsol, ysol]:
                        ysol: An array of arrays of solutions [u1, u2, ..., um]
                        tsol: Time axis

        =========================== Examples =============================
        Example 1: System of 1 ODE
            Problem:
                y' = (y/t) - (y/t)^2
                t in [1, 4]
                y(1) = 1
                h = 0.1

            #example function to pass into the method:
            def func(t, y):
                dy = np.zeros(len(y))         #len(y) = 1
                dy[0] = (y[0]/t) - (y[0]/t)**2
                return dy

            #declaring variables
            a = 1
            b = 4
            alpha = [1]
            h = 0.1

            #function call
            ODE_Solvers.RK4(func, alpha, a, b, h, plot = 1)
        _______________________________________________________________

        Example 2: higher order ODE (order = 2)
            Problem:
                y'' = t*e**t + 2y' - y
                t in [1, 4]
                y(1) = 1
                y'(1) = 2
                h = 0.1

            {
            #Note: this ode has the following system
            Let u1 = y, u2 = y'
            u1' = u2
            u2' = t*e**t + 2u2 - u1
            with IC
            u1(1) = 1,
            u2(1) = 2
            }

            #example function to pass into the method
            def func(t,y):
                e = np.e
                dy = np.zeros(len(y))           #len(y) = 2, with y[0] = y, and y[1] = y'
                dy[0] = y[1]                    #dy[0] = (u_1)' = y' = u2
                dy[1] = t*e**t + 2*y[1] - y[0]  #dy[1] = (u_2)' = y'' = t*e**t + 2y' - y
                return dy

            #declaring variables
            a = 1
            b = 4
            alpha = [1, 2]
            h = 0.1

            #function call
            ODE_Solvers.RK4(func, alpha, a, b, h, plot = 1)
        ____________________________________________________________

        Example 3: System of first order ODE (Predator-Prey, Volterra Model)
            Problem:
                y1' = k1*y1 - k2*y1*y2
                y2' = k3*y1*y2 - k4*y2
                t in [0, 4]
                y1(0) = 1000
                y2(0) = 500
                h = 0.1

            #example function to pass into the method
            def func(t,y):
                k1 = 3 #change values as needed
                k2 = 0.02 #change values as needed
                k3 = 0.006 #change values as needed
                k4 = 0.5 #change values as needed
                dy = np.zeros(len(y))               #len(y) = 2, with y[0] = u1, and y[1] = u2
                dy[0] = k1*y[0] - k2*y[0]*y[1]      #dy[0] = (u_1)' = y1' = k1*u1 - k2*u1*u2
                dy[1] = k3*y[0]*y[1] - k4*y[1]      #dy[1] = (u_2)' = y2' = k3*u1*u2 - k4*u2
                return dy

            #declaring variables
            a = 0
            b = 4
            alpha = [1000, 500]
            h = 0.1

            #function call
            ODE_Solvers.RK4(func, alpha, a, b, h, plot = 1)

        ___________________________________________________________

        '''
        print(Notes)

    if((kw.lower()).replace(" ", "") in dict1["rkf_key"]):
        Notes = '''
        Runge-Kutta Fehlberg:
            Function Name: RKF

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
        print(Notes)

    if((kw.lower()).replace(" ", "") in dict1["taylor_key"]):
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
        print(Notes)

    return 0
