
# un poco difícil aplicar el ejemplo a este caso, así que tocará echarle cabeza igualmente
# tras un rato echandole mucha cabeza creo que mejor revisaré un tutorial de youtube
# al final decidí echarle un ojo al código de mi kamarada Alejandro Bello y al final salío lo siguiente:
import math
e=math.e
sumatoria_i=1 #primer termino de la sumatoria
def sumatoria(x:float,aj:int,sumatoria_i:int):
    for n in range(1,aj+1):
        numerador=x**n
        if n==0:
            m=1
        elif (n>0):
            m=n
            while(n>1):
                n=n-1
                m=m*n
                if n==0: 
                    m=1
        iteración=numerador/m
        sumatoria_i +=iteración
        sumatoria=sumatoria_i
    return sumatoria
if __name__=="__main__":
    x=1 #este es el ajuste manual de x para el valor de la función e^x, en este caso se pone x=1 para que la función retorne el valor de e

    #he decidido según el criterio del 0.1% de error, colocar 5 términos para el experimento, tras determinar manualmente
    #Apunte importante: Colocar valores mayores a 16 hace que para python la diferencia sea visualmente(es decir, al imprimir los valores) despreciable
    #sin embargo, si el valor de x aumenta, el porcentaje de error también, por lo que es necesario aumentar también el número de términos de la serie
    aj=5
    sum=sumatoria(x,aj,sumatoria_i)
    print("Se calcula mediante una serie de Maclaruin que la función e^x en",x,"considerando",aj,"términos es igual a:",sum)
    dif_e= e**x-sum
    print("al calcular la función e^x en x=",x,"usando la libreria Math, se obtiene que e^x=",e**x)
    print("la diferencia entre estos dos valores es de:",dif_e)
    error= (abs(sum-(e**x))/(e**x))*100 #tras buscar en internet, la función abs de python es la que se usa para este cálculo
    print("el porcentaje de error al usar",aj,"términos es de",error,"%")
