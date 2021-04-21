import numpy as np

#
# #zadanie1
#
# a = np.arange(4,21*4,4)
# print(a)
#
# #zadanie2
#
# b = np.array([1,2,3,4,5],dtype=float)
# print(b)
# print(b.dtype)
# c = b.copy().astype('int32')
# b[0]=3
# print(c)
# print(c.dtype)
#
# #zadanie3
#
# def ciag(n):
#     print(np.array([2**x for x in range(n**2)]).reshape(n,n))
#
# print(ciag(4))
#
# #zadanie4
#
# def generuj(n, p):
#     return [n**x for x in range(1, p+1)]
#
# print(generuj(2,4))
#
# #zadanie5
#
# def wektor (n):
#     return np.diag(np.linspace(n,0,n),2)
#
# print (wektor (5))
#
# #zadanie7
#
# def macierz(n):
#     tab = [x * 2 for x in range(1, n + 1)]
#     temp = []
#     for x in range(0, n):
#         for y in range(0, n):
#             temp.append(tab[abs(x - y)])
#     wynik = np.array(temp)
#     wynik = wynik.reshape((n, n))
#     return wynik
#
#
# print(macierz(10))
#
#
# #Zad6
# malina = np.array(list('malina'))
# mrowka = np.array(list('mrówka'))
# armata = np.array(list('armata'))
# armata = np.flip(armata)
#
# wykreslanka = np.zeros((6,6), dtype='str')
#
# print(wykreslanka)
#
# wykreslanka = np.diag(mrowka)
# wykreslanka[:, 0] = malina
# wykreslanka[5,::-1] = armata
# wykreslanka[5,:] = armata
# print(wykreslanka)
# print("")
# wykreslanka[:, 0] = mrowka
# wykreslanka[5,::-1] = armata
# for a in range(5):
#     wykreslanka[a,a] = malina[a]
# print(wykreslanka)

#NUMPY2 ------------------------------------------------------------------NUMPY2
#zadanie1

a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(1,3)
c = a * b
print(a)
print(c)

#zadanie2
a = np.arange(9).reshape(3,3)
b = np.arange(16).reshape(4,4)
print(a)
print(a.min(axis=1))
print(a.min(axis=0))
print(b)
print(b.min(axis=1))
print(b.min(axis=0))


#zadanie3
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(1,3)
c = a * b
print(a)
print(c)

#zadanie4
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(1,3)

a = np.ones(3, dtype='int32')
b = np.linspace(0, np.pi, 3)
print(a)
print(a.dtype)
print(b)
print(b.dtype)

c = a * b
print(c)



from math import *
# zadanie5
a = []
c = np.array([[3, 5], [2, 7], [9, 6]])
for x in c:
    for y in range(len(x)):
        a.append(sin(x[y]))
print(a)