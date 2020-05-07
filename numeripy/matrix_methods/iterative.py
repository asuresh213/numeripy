import numpy as np

def mat_iter(A, b, xo, N, tol, w = 0, type = " "):
    if((type.lower()).replace(" ", "") == "jacobi"):
        return Jacobi(A, b, xo, N, tol)
    if((type.lower()).replace(" ", "") == "gaussseidel"):
        return Gauss_Seidel(A, b, xo, N, tol)
    if((type.lower()).replace(" ", "") == "sor"):
        return SOR(A, b, xo, w, tol, N)

def Jacobi(A, b, xo, N, tol):
    n = len(b)
    k = 1
    x = np.zeros(n)
    while(k<=N):
        for i in range(0,n):
            sum1 = 0
            for j in range(0,n):
                if(i != j):
                    sum1+=A[i][j]*xo[j]
            x[i] = (1/A[i][i])*(-sum1 + b[i])
        if(np.linalg.norm(x-xo, np.inf) <= tol):
            return x
        k+=1
        for i in range(0, n):
            xo[i] = x[i]
    print("Max iterations exceeded")
    return x

def Gauss_Seidel(A, b, xo, N, tol):
    n = len(b)
    k = 1
    x = np.zeros(n)

    while(k<=N):
        for i in range(n):
            sum1 = 0
            sum2 = 0
            for j in range(i):
                sum1 += A[i][j]*x[j]
            for m in range(i+1, n):
                sum2 +=A[i][m]*xo[m]
            x[i] = (1/A[i][i])*(-1*sum1-sum2+b[i])
        if(np.linalg.norm(x-xo)<=tol):
            return x
        k+=1
        for p in range(n):
            xo[p] = x[p]
    print("Max iterations exceeded")
    return x

def SOR(A, b, xo, w, tol, N):
    n = len(b)
    x = np.zeros(n)
    k = 1
    while(k<=N):
        for i in range(0,n):
            sum1 = 0
            sum2 = 0
            for j in range(0,i):
                sum1 +=A[i][j]*x[j]
            for j in range(i+1,n):
                sum2+=A[i][j]*xo[j]
            x[i] = (1-w)*xo[i] + (w/A[i][i])*(-sum1-sum2+b[i])
        if(np.linalg.norm(x-xo, np.inf) < tol):
            return x
        k+=1
        for i in range(0,n):
            xo[i] = x[i]
        print(x)
    print("Maximum iteration exceeded")
    return x
