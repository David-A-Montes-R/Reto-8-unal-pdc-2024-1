#Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], 
#utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

#es importante echarle ojo al dominio de la función, ya que poner valores superiores a 1 es bastante fastidiosos
import math
pi=math.pi
def sumatoria_arctan(x:float,aj:int,sumatoria_i:int):
    if (-1<=x<=1):
        for n in range(1,aj+1):
            l=(2*n)+1
            numerador=((-1)**n)*(x**l)
            iteración=numerador/l
            sumatoria_i +=iteración
            sumatoria=sumatoria_i
        return sumatoria
    else:
        return "la función arcotangente según la serie de Maclaurin solo se puede definir entre -1 y 1"
    
if __name__=="__main__":
    r3= 3**(1/2) #la raíz de 3
    x=1/r3 # se elige el reciproco de la raíz cuadrada de 3 ya que su arcotangente es pi/6, lo cual es facil de comparar
    aj=4 #ajuste manual de términos para cumplir con el requisito del 0.1% de error
    #nota adicional porque quise hacer el experimento: 
    #dado que x=1 o x=-1 se sales del dominio de la serie, para dar una aproximación que cumpla con el requisito anterior en estos casos se requieren 318 términos.
    sumatoria_i=x #primer termino de la sumatoria
    arctan=sumatoria_arctan(x,aj,sumatoria_i)
    dif_arctan= math.atan(x)-arctan
    error=(abs(arctan-math.atan(x))/math.atan(x))*100
    print("se calcula mediante una serie de Maclaurin que el valor del arctan(x) en x=",x,"considerando",aj," términos es igual a:",arctan)
    print("al calcular la función arctan(x) en x=",x,"usando la libreria Math, se obtiene que arctan(x)",math.atan(x))
    print("la diferencia entre estos dos valores es de:",dif_arctan)
    print("el porcentaje de error al usar",aj,"términos es de",error,"%")