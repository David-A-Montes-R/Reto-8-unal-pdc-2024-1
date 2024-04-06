

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

#creo que se podría hacer una versión más simplificada pero de momento lo voy a dejar así