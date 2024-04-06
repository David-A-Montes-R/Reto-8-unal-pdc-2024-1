# Reto 8 PDC Unal 2024-1
<div align='center'>
<figure> <img src="https://i.postimg.cc/HkMddSNw/error-418.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

## por: David Alejandro Montes Rodríguez

## 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
Se define una función que eleva cada número a su cuadrado, luego se imprime cada número con su respectivo cuadrado
```python
def cuadrado(a):
    b=a**2
    return b
if __name__ == "__main__":
    for a in range(1,101):
        b=cuadrado(a)
        print("el respectivo cuadrado del número",a,"es el número:",b)
```
## 2.Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
se definen dos bucles ``for``, uno en el que la cuenta empieza en 1 y va avanzando de a 2 hasta 999 y otro en el que la cuenta empieza en 2 y va avanzando de a 2 hasta 1000, estos dos casos se imprimen consecutivamente.
```python
def listar_numeros(a):
    print("el listado de números impares es:")
    for a in range(1,1000,2):
            print(a)
    print("el listado de los números pares es:")
    for a in range(2,1001,2):
        print(a)

if __name__ == "__main__":
    l=listar_numeros(a)
```
## 3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
En ambos casos se va avanzando dentro del bucle ``for`` de forma descendente de a 2, hasta que el número anterior a 1(que en este caso, al ser de forma descendente, sería 2),solo que en el caso de que el número ``n`` inicial sea impar, se le restará 1.
```python
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
```
## 4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
Se recicla el código del reto 7 para el factorial y se implementa un bucle ``for`` para imprimir la lista de números y factoriales. También se valoran los casos de que se ingresen valores ``n`` menores a 1, para lo cual el programa envía una respuesta según el caso.

```python
def factorial_casero(n:int):
    m=n
    if n==0:
        print("el factorial del número 0 es 1")
    elif (n>0):
        while(n>1):
            n=n-1
            m=m*n
    return m

if __name__ =="__main__":
    n=int(input("introduzca un número natural:"))
    if n>0:
        x=1
        for x in range(1,n+1):
            f=factorial_casero(x)
            print("el factorial del numero",x,"es el número",f)
            x= x+1
    else:
        print("el menor factorial que se puede sacar es el factorial de 0")
        print("el factorial de 0 es 1")
        print("no es posible sacar el factorial de un número negativo")
```
## 5.Calcular el valor de 2 elevado a la potencia n usando ciclos for
Se define una variable cuyo valor inicial es 2, luego esta variable se va multiplicando por 2 hasta que el ciclo ``for`` finaliza (como la variable ``a`` almacena su último valor calculado, el bucle solo se ejecutará hasta el número anterior a n, ya que de multiplicarse hasta llegar a ``n``, el programa devolverá la potencia siguiente a la potencia ``n``). También se valora el caso en el que ``n`` sea igual a 0.
```python
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
```
## 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
Para este ejercicio, el cual sería la generalización del anterior, se hace algo parecido a lo que se hace para calcular el factorial usando ciclos ``while`` en el reto 7, definiendo 3 variables, dos las cuales serán la base y el exponente, y una tercera que para calcular la potencia tendrá el valor inicial de la base. Sucede lo mismo que con el ciclo ``for`` del anterior, y se valoran los casos de 0^0 y b^0. para los cuales el programa da una respuesta correspondiente.
```python
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
```
## 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
En este programa se definen un número ``a`` que es la variable que aumenta dentro del ciclo ``for`` y una variable ``c``, que inicialmente es igual a 1 y después de cada bucle ``for`` que correspondería a cada tabla, se va sumando 1, hasta llegar hasta 9.
```python
#este es de esos que va a tocar hacer de forma no tan bonita, pero funcional
a:int=1
c:int=1
def tablas(a:int,c:int):
    print("la tabla del 1 es:")
    for a in range(1,11):
        print(c,"x",a,":",a)
    print("la tabla del 2 es:")
    c=c+1
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    print("la tabla del 3 es:") 
    c=c+1 
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    print("la tabla del 4 es:")
    c=c+1
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    print("la tabla del 5 es:")
    c=c+1
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    print("la tabla del 6 es:")
    c=c+1
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    print("la tabla del 7 es:")
    c=c+1
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    print("la tabla del 8 es:")
    c=c+1
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    print("la tabla del 9 es:")
    c=c+1
    for a in range(1,11):
        print(c,"x",a,":",a*c)
    return ""

if __name__=="__main__":
    t=tablas(a,c)
    print(t)

```
## 8. Diseñar una función que permita una aproximación de la fnción exponencial alrededor de 0 para cualquier valor x (real.), utilizando los primeros n términos de la serie de Maclaurin. Nota: Use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
Para realizar este ejercicio se utilizó la serie de Maclaurin brindada por el profesor en clase ( la verdad fue un poco díficil implementarla en python, pero se logró), definiendo una cantidad de términos meidante el valor ``aj``, definiendo el primer término de la sumatoria como una constante igual a 1(la cual solo funciona en el caso de esta función), y luego sumando cada término a este valor. Luego se hicieron las comparaciones solicitadas en el enunciado.
```python
#aquí es importante echarle un repasito al repo de la clase para ver como se hacen las sumatorias
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
```
## 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
Para este ejercicio se utilizó la serie de Maclaurin dada por el profesor,se puede entender que este ejercicio es una generalización del ejercicio anterior, reinterpretada para la sumatoria dada, por lo que ahora el valor inicial de la sumatoria es el mismo valor ``x``.

```python
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

```
## 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

Este es un caso similar al ejercicio anterior, solo que en este caso el valor de ``x`` no puede ser ni menor o igual a -1, ni mayor o igual a 1 debido a que el uso de la serie de Maclaurin para una aproximación fidedigna lo permite (aunque con motivos de experimentación, el programa diseñado permite que ``x`` también pueda agarrar valores de -1 o 1).

```python

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
```