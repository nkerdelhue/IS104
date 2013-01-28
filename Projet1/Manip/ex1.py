#Import des bibliotheques
import numpy as np


def power(x,n):
    # Function which return y = x^n 
    if(n == 0):
        y = 1;
    elif(n == 1):
        y = x;
    elif(n % 2 == 0):
        tmp = power(x, n/2);
        y = tmp * tmp;
    else:
        tmp = power(x, (n - 1) / 2);
        y = tmp * tmp;

    return y;


def fibo(n):
    if(n == 0 or n == 1):
        y = 1;
    else:
        y = fibo(n - 1) + fibo(n -2);

    return y;



m = np.arange(10, 10);

print(np.m[0,2]);



def ord_matrix(n):
    #Compute a matrix M n * n, with M[i, j] = i = j
    if(n == 0):
        return 0;
    else:
         m = np.zeros((n,n));
         for i in range(len(m)):
             for j in range(len(m)):
                 np.m[i,j] =  i;

    return m;

#Divers Tests
#print(power(2, 32));

#print(fibo(100));

print(ord_matrix(3));
