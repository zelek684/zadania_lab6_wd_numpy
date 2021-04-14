import numpy as np

#zadanie1

a = np.arange(4,21*4,4)
print(a)

#zadanie2

b = np.array([1,2,3,4,5],dtype=float)
print(b)
print(b.dtype)
c = b.copy().astype('int32')
b[0]=3
print(c)
print(c.dtype)

#zadanie3

def ciag(n):
    print(np.array([2**x for x in range(n**2)]).reshape(n,n))

print(ciag(4))

#zadanie4

def generuj(n, p):
    return [n**x for x in range(1, p+1)]

print(generuj(2,4))

#zadanie5

def wektor (n):
    return np.diag(np.linspace(n,0,n),2)

print (wektor (5))

#zadanie7


