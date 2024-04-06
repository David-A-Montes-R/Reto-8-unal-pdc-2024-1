#Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. 
#Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

import math
pi=math.pi
def sumatoria_seno(x:float,aj:int,sumatoria_i:int):
    for n in range(1,aj+1):
        l=(2*n)+1
        numerador=((-1)**n)*(x**l)
        if l==0:
            m=l
        elif (l>0):
            m=l
            while(l>1):
                l=l-1
                m=m*l
                if l==0:
                    m=1
        iteración=numerador/m
        sumatoria_i +=iteración
        sumatoria=sumatoria_i
    return sumatoria
if __name__=="__main__":
    x= pi/2 # se eligío pi/2 como valor de x para poder comprobar el valor del seno, ya que el valor del seno de pi/2 es igual a 1
    sumatoria_i=x #primer termino de la sumatoria
    aj=3 #este es el ajuste manual para cumplir con el requisito del 0.1% de error
    sen=sumatoria_seno(x,aj,sumatoria_i)
    dif_sen= math.sin(x)-sen
    error=(abs(sen-math.sin(x))/math.sin(x))*100
    print("se calcula mediante una serie de Maclaurin que el valor del sen(x) en x=",x,"considerando",aj," términos es igual a:",sen)
    print("al calcular la función sen(x) en x=",x,"usando la libreria Math, se obtiene que sen(x)",math.sin(x))
    print("la diferencia entre estos dos valores es de:",dif_sen)
    print("el porcentaje de error al usar",aj,"términos es de",error,"%")