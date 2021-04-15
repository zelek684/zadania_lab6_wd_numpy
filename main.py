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

def macierz(n):
    tab = [x * 2 for x in range(1, n + 1)]
    temp = []
    for x in range(0, n):
        for y in range(0, n):
            temp.append(tab[abs(x - y)])
    wynik = np.array(temp)
    wynik = wynik.reshape((n, n))
    return wynik


print(macierz(10))
