#Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
def x_elevado_n(b:float,c:float,n:int):
    if b==0 and n==0:
        return "La potencia de 0 elevado a la 0 es indeterminada (aunque dependiendo del contexto puede considerarse como 1)"
    if n==0 and not(b==0):
        return "1.0"
    else:
        for n in range(0,n-1):
            b=b*c
        return b
if __name__ == "__main__":
    b=float(input("Introduzca la base:"))
    c:float=b
    n=int(input("introduzca el exponente:"))
    x=x_elevado_n(b,c,n)
    print("el valor de",b,"elevado a la potencia de",n,"es:")
    print(x)