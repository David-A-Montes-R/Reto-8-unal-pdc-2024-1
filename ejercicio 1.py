#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
def cuadrado(a):
    b=a**2
    return b
if __name__ == "__main__":
    for a in range(1,101):
        b=cuadrado(a)
        print("el respectivo cuadrado del número",a,"es el número:",b)