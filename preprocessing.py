

import numpy as np

def preprocessing(A,k,N):
    # in python it maps the array
    a=A.copy()
    S=sum(a[:N-k+1])
    B=0
    # for _ in range(N-k+1,N):
    for n in range(2,k+1):
        a[N-k+n-1]=min(A[N-k+n-1],S//(n-1))
        delta= A[N-k+n-1]-a[N-k+n-1]
        B=B+delta
        S=S+a[N-k+n-1]
    return a,B

A=[1,1,3,4,6]
k=3
N=len(A)

a,B=preprocessing(A,k,N)
print(a)
print(B)


def distribution(a, N, k, B):


    S = sum(a)               
    M = S // k              
    B0 = S - M * k            

 
    for n in range(N - B0 + 1, N + 1):
        a[n - 1] -= 1       

    B = B + B0                
    # for optimized
    # a.sort()
    # print("a sorted: ",a)
 
    l = np.zeros(N, dtype=int)  
    r = np.zeros(N, dtype=int)  
    for n in range(1, N + 1):
        l[n - 1] = sum(a[:n-1]) + 1  
        r[n - 1] = sum(a[:n])        

   
    CM = np.zeros((N, M), dtype=float) 

    for i in range(1, k + 1):
        for j in range(1, M + 1):
            for n in range(1, N + 1):
                if l[n - 1] <= j + M * (i - 1) <= r[n - 1]:
                # if l[n - 1] <= i + M * (j - 1) <= r[n - 1]:

                    CM[n - 1, j - 1] = 1 /k

    return a, M, CM



aMod,M,CM=distribution(a,N,k,B)
print('\n')
print(aMod)
print(M)
print(CM)