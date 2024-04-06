#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
def listar_numeros(a):
    print("el listado de números impares es:")
    for a in range(1,1000,2):
            print(a)
    print("el listado de los números pares es:")
    for a in range(2,1001,2):
        print(a)

if __name__ == "__main__":
    l=listar_numeros(a)