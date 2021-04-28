#Ejercicio 3 parte 1

#Variables
print("Ingrese un nombre en cada espacio:")
nombre1 = input("1:")
nombre2 = input("2:")
nombre3 = input("3:")
nombre4 = input("4:")
nombre5 = input("5:")
print("Ingrese un apellido:")
apellido = input("Apelllido:")

puntaje = 0 
puntoscri1 = 10
puntoscrit2 = 5
puntoscrit3 = 10
puntoscrit4 = 20

nombres_list = []
nombres_list.append(nombre1)
nombres_list.append(nombre2)
nombres_list.append(nombre3)
nombres_list.append(nombre4)
nombres_list.append(nombre5)

def countLettersN(nombre):
    letrasN1 = len(nombre)
    return letrasN1
def countLettersA(apellido):
    len(apellido)


def criterio1():
    crit1list = [countLettersN(i) for i in nombres_list]
    

        