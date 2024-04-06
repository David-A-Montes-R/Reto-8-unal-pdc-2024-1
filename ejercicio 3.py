#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
def pares(n:int):
    if (n%2==0):
        for a in range(n,1,-2):
            print(a)
    else:
        for a in range(n-1,1,-2):
            print(a)
if __name__ =="__main__":
    n=int(input("introduzca un número n:"))
    p=pares(n)