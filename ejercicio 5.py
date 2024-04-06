#Calcular el valor de 2 elevado a la potencia n usando ciclos for
def potencias(a:int, n:int):
    a:int=2
    print("el valor de 2 elevado a la potencia de",n,"es:")
    for n in range(0,n-1):
        a=a*2
    return a
if __name__ =="__main__":
    n= int(input("introduzca un número para el cual quiera saber su exponencial de 2:"))
    p=potencias(a,n)
    if n==0:
        print("1")
    else:
        print(p)