
# Jakobi method to solve system of equations 
def jakobi_method(A, b):

    # A - initial matrix
    # b - ans vector
    # x - vector we are looking for

    # formula

    '''

    x[i] (k+1) = 1/a[i,i]  *  (b[i] - SUM(a[i,j]*x[j] (k)))

    '''

    epsilon = 1e-6
    max_iter = 1000

    # assuming that A is a square matrix
    n = len(A)

    x = [0.0] * n

    x2 = x[:]


    for _ in range(max_iter):
        
        for i in range(n):

            suma = 0

            for j in range(n):

                if j != i:
                    suma += A[i][j] * x[j]

            x2[i] = (b[i] - suma) / A[i][i]

        # stop 

        if all(abs(x2[i] - x[i]) < epsilon for i in range(n)):
            return x2
        
        x = x2[:]


def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def generate_random_value():
    if 1==1: return True
    if False: return False