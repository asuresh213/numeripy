import numpy as np

def matrix_fact(n, A, type = " "):
    if(type.lower() == "lu"):
        return LU_fact(n, A)
    if(type == "ldlt"):
        return LDLt(n, A)
    if(type == "cholesky"):
        return cholesky(n, A)


#-------------------------------------------------------------------
def LU_fact(n, A):
    U = np.zeros((n, n))
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if(i == j):
                L[i][j] = 1

    U[0][0] = A[0][0]
    if(U[0][0] == 0):
        print("Factorization not possible!")
        return 0
    for j in range(1, n):
        U[0][j] = A[0][j]/L[0][0]
        L[j][0] = A[j][0]/U[0][0]

    for i in range(1, n-1):
        sum = 0
        for k1 in range(i):
            sum += L[i][k1]*U[k1][i]
        U[i][i] = A[i][i] - sum
        if(U[i][i] == 0):
            print("Factorization not possible!")
            return 0
        for j in range(i+1, n):
            sum1 = 0
            sum2 = 0
            for k2 in range(i):
                sum1 += L[i][k2]*U[k2][j]
                sum2 += L[j][k2]*U[k2][i]
            U[i][j] = (1/L[i][i])*(A[i][j] - sum1)
            L[j][i] = (1/U[i][i])*(A[j][i] - sum2)
    last_sum = 0
    for k3 in range(n-1):
        last_sum+=L[n-1][k3]*U[k3][n-1]
    U[n-1][n-1] = A[n-1][n-1] - last_sum

    return [L, U]


#-------------------------------------------------------------------------------

def LDLt(n, A):
    L = np.zeros((n, n))
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if(i==j):
                L[i][j] = 1

    D[0][0] = A[0][0]

    for i in range(n):
        for j in range(n):
            if(i > j and j == 0):
                L[i][j] = A[i][j]/D[0][0]
    D[1][1] = A[1][1] - (D[0][0]*(L[1][0])**2)
    L[2][1] = (A[2][1] - D[0][0]*L[1][0]*L[2][0])/D[1][1]
    D[2][2] = A[2][2] - (D[0][0]*(L[2][0])**2 + D[1][1]*(L[2][1])**2)
    return [L, D]

#-------------------------------------------------------------------------------

def cholesky(n, A):
    L = np.zeros((n, n))
    L[0][0] = np.sqrt(A[0][0])
    for j in range(1, n):
        L[j][0] = A[j][0]/L[0][0]

    for i in range(1, n-1):
        sum = 0
        for k in range(i):
            sum += L[i][k]**2
        L[i][i] = np.sqrt(A[i][i] - sum)
        for j in range(i+1, n):
            sum2 = 0
            for k2 in range(i):
                sum2 += L[j][k2]*L[i][k2]
            L[j][i] = (A[j][i] - sum2)/L[i][i]
    last_sum = 0
    for k3 in range(n):
        last_sum += L[n-1][k3]**2
    L[n-1][n-1] = np.sqrt(A[n-1][n-1] - last_sum)

    return L
#-------------------------------------------------------------------------------

def crout(n, A, b):
    x = np.zeros(n)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    z = np.zeros(n)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    L[0][0] = Ab[0][0]
    U[0][1] = Ab[0][1]/L[0][0]
    z[0] = Ab[0][n]/L[0][0]
    for i in range(1, n-1):
        L[i][i-1] = Ab[i][i-1]
        L[i][i] = Ab[i][i] - (L[i][i-1]*U[i-1][i])
        U[i][i+1] = Ab[i][i+1]/L[i][i]
        z[i] = (Ab[i][n] - L[i][i-1]*z[i-1])/(L[i][i])
    L[n-1][n-2] = Ab[n-1][n-2]
    L[n-1][n-1] = Ab[n-1][n-1] - L[n-1][n-2]*U[n-2][n-1]
    z[n-1] = (1/L[n-1][n-1])*(Ab[n-1][n] - L[n-1][n-2]*z[n-2])


    x[n-1] = z[n-1]
    for i in range(n-2, -1, -1):
        x[i] = z[i] - U[i][i+1]*x[i+1]
    return x
#-------------------------------------------------------------------------------
