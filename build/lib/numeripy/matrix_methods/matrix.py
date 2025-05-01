import numpy as np

def Matmul(A, B):
    if(len(A[0]) != len(B)):
        print("Matrices not compatible")
    res = np.zeros((len(A), len(B[0])))
    # iterate through rows of X
    for i in range(len(A)):
       # iterate through columns of Y
       for j in range(len(B[0])):
           # iterate through rows of Y
           for k in range(len(B)):
               res[i][j] += A[i][k] * B[k][j]
    return res


def determinant(A):
    n = len(A)
    AM = np.copy(A)
    def Upper_T(n, AM):
        for diag in range(n):
            for i in range(diag +1, n):
                if(AM[diag][diag] == 0):
                    AM[diag][diag] = 1*10**(-16)
                temp = AM[i][diag]/AM[diag][diag]
                for j in range(n):
                    AM[i][j] = AM[i][j] - temp*AM[diag][j]
        return AM
    res = Upper_T(n, AM)
    
    prod = 1.0
    for i in range(n):
        prod *= AM[i][i]

    return prod
