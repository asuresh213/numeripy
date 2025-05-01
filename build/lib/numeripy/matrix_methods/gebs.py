import numpy as np


def gaussian_elim(n, A, b, ver = 0):
    if (ver == 0):
        sol = gebs(n, A, b)
    if(ver == 1):
        sol = gebs_2(n, A, b)
    if(ver == 2):
        sol = gebs_3(n, A, b)

    return sol

#Gaussian Elimination and Backward Substitution
def gebs(n, A, b):
    Ab = np.hstack([A, b.reshape(-1, 1)])
    x = np.zeros(n)
    #step 1
    for i in range(n):
        #step 2
        p = 99999
        for q in range(i, n):
            if(Ab[q][i] !=0):
                p = q
                break
        if(p == 99999):
            print("No unique solution exists!")
            return 0
        #step 3
        if(p != i):
            print("swapping rows %s and %d!" % (p, i))
            Ab[[p, i]] = Ab[[i, p]]
        #step 4
        for j in range(i+1, n):
            #step 5
            m_ji = Ab[j][i]/Ab[i][i]
            #step 6
            Ab[j] = Ab[j] - m_ji*Ab[i]
    if(Ab[n-1][n-1] == 0):
        print("No unique solution exists!")
        return 0
    x[n-1] = Ab[n-1][n]/Ab[n-1][n-1]
    for r in range(n-2, -1, -1):
        temp_sum = 0
        for j in range(r+1, n):
            temp_sum += Ab[r][j]*x[j]
        x[r] = (Ab[r][n] - temp_sum)/Ab[r][r]

    return x

#-------------------------------------------------------------------------------

#Algorithm 6.2
#Gaussian Elimination and Backward Substitution with partial pivoting
def gebs_2(n, A, b):
    Ab = np.hstack([A, b.reshape(-1, 1)])
    x = np.zeros(n)
    nrow = np.zeros(n)
    #step 1
    for i in range(n):
        nrow[i] = i
    #step 2
    for i in range(n-1):
        #step 3
        p = 99999
        max = -1
        for q in range(i,n):
            if(np.abs(Ab[int(nrow[q])][i]) > max):
                max = np.abs(Ab[int(nrow[q])][i])
        for d in range(i,n):
            if(np.abs(Ab[int(nrow[d])][i]) == max):
                p = d
                break
        if(Ab[int(nrow[p])][i] == 0):
            print("no unique solution exists")
            return 0
        if(nrow[i] != nrow[p]):
            print("exchanging rows %u and %a"%(int(nrow[i] +1), int(nrow[p] +1)))
            ncopy = nrow[i]
            nrow[i] = nrow[p]
            nrow[p] = ncopy
        for j in range(i+1, n):
            m_ji = Ab[int(nrow[j])][i]/Ab[int(nrow[i])][i]
            Ab[int(nrow[j])] = Ab[int(nrow[j])] - m_ji*Ab[int(nrow[i])]
        if(Ab[int(nrow[n-1])][n-1] == 0):
            print("no unique solution exists")
            return 0

    x[n-1] = Ab[int(nrow[n-1])][n]/Ab[int(nrow[n-1])][n-1]
    for r in range(n-2, -1, -1):
        temp_sum = 0
        for j in range(r+1, n):
            temp_sum += Ab[int(nrow[r])][j]*x[j]
        x[r] = (Ab[int(nrow[r])][n] - temp_sum)/Ab[int(nrow[r])][r]
    return x

#-------------------------------------------------------------------------------

#Algotithm 6.3
#Gaussian Elimination and Backward Substitution with scaled pivoting
def gebs_3(n, A, b):
    Ab = np.hstack([A, b.reshape(-1, 1)])
    s = np.zeros(n)
    x = np.zeros(n)
    nrow = np.zeros(n)
    #step 1
    max = 0
    for i in range(n):
        for j in range(n):
            if(np.abs(Ab[i][j]) > max):
                max = np.abs(Ab[i][j])
        s[i] = max
        if(s[i] == 0):
            print("No solution exists!")
            return 0
        else:
            nrow[i] = i
    #step 2
    for i in range(n-1):
        #step 3
        p = 99999
        max = -1
        for q in range(i,n):
            if(np.abs(Ab[int(nrow[q])][i])/s[int(nrow[q])] > max):
                max = np.abs(Ab[int(nrow[q])][i])/s[int(nrow[q])]
        for d in range(i,n):
            if(np.abs(Ab[int(nrow[d])][i])/s[int(nrow[d])] == max):
                p = d
                break
        if(Ab[int(nrow[p])][i] == 0):
            print("no unique solution exists")
            return 0
        if(nrow[i] != nrow[p]):
            print("exchanging rows %u and %a"%(int(nrow[i] +1), int(nrow[p] +1)))
            ncopy = nrow[i]
            nrow[i] = nrow[p]
            nrow[p] = ncopy
        for j in range(i+1, n):
            m_ji = Ab[int(nrow[j])][i]/Ab[int(nrow[i])][i]
            Ab[int(nrow[j])] = Ab[int(nrow[j])] - m_ji*Ab[int(nrow[i])]
        if(Ab[int(nrow[n-1])][n-1] == 0):
            print("no unique solution exists")
            return 0

    x[n-1] = Ab[int(nrow[n-1])][n]/Ab[int(nrow[n-1])][n-1]
    for r in range(n-2, -1, -1):
        temp_sum = 0
        for j in range(r+1, n):
            temp_sum += Ab[int(nrow[r])][j]*x[j]
        x[r] = (Ab[int(nrow[r])][n] - temp_sum)/Ab[int(nrow[r])][r]
    return x
