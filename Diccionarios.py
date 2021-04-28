#Ejercicio 3 parte 2

#Diccionarios------------------------------------------------

#Productos y precios
Precios = {"Leche": 1.19, "Galletas": 1.45, "Mantequilla": 1.90, "Queso": 2.59, "Pan": 4.99, "Jalea": 3.65, "Yogurt": 3.15, "Manzanas": 2.15, "Naranjas": 0.99, 'Bananos': 1.29}
#Productos y existencias
Existencias = {'Leche': 20, 'Galletas': 32, 'Mantequilla': 15, 'Queso': 15, 'Pan': 20, 'Jalea': 18, 'Yogurt': 35, 'Manzanas': 35, 'Naranjas': 40, 'Bananos': 23}


#Funciones---------------------------------------------------------------

#El usuario ingresa los datos de su factura y compra
def crearCompra():
    nombre = input("Ingrese su nombre: ")
    print("Ingrese la cantidad deseada de cada producto, si no desea ninguno coloque 0.")
    compra_full  = {}
    compra = {}
    #Asegura que el input sea un int
    try:
        leche = int(input("Leche: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        leche = int(input("Leche: "))
    
    try:
        galletas = int(input("Galletas: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        galletas = int(input("Galletas: "))

    try:
        mantequilla = int(input("Mantequilla: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        mantequilla = int(input("Mantequilla: "))

    try:
        queso= int(input("Queso: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        queso= int(input("Queso: "))
        
    try:
        pan= int(input("Pan: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        pan= int(input("Pan: "))
        
    try:
        jalea= int(input("Jalea: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        jalea= int(input("Jalea: "))
    
    try:
        yogurt= int(input("Yogurt: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        yogurt= int(input("Yogurt: "))
    
    try:
        manzanas= int(input("Manzanas: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        manzanas= int(input("Manzanas: "))

    try:
        naranjas= int(input("Naranjas: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        naranjas= int(input("Naranjas: "))

    try:
        bananos= int(input("Bananos: "))
    except ValueError:
        print("Solo utilice numeros, si no desea ninguno coloque 0")
        bananos = int(input("Bananos: "))
    #Asigna los values a las keys del diccionario
    compra["Leche"] = leche
    compra["Galletas"]= galletas
    compra["Mantequilla"]= mantequilla
    compra["Queso"]= queso
    compra["Pan"]= pan
    compra["Jalea"]= jalea
    compra["Yogurt"]= yogurt
    compra["Manzanas"]= manzanas
    compra["Naranjas"]= naranjas
    compra["Bananos"]= bananos
    #Elimina los keys que son 0.
    for k, v in compra.items():
        if v != 0:
            compra_full[k] = v
                
    return compra_full,nombre

#Asignar variables compras y nombres
compras, nombres = crearCompra()
    


#Calcula el precio de cada producto individual
def calcularPrecios():
    itemsround = {}
    itemsescogidos = {k : v * Precios[k] for k, v in compras.items() if k in Precios}
    #Redondea los numeros
    for key in itemsescogidos:
        itemsround[key] = round(itemsescogidos[key], 2)
    return itemsround

#Asignar variable items
items = calcularPrecios()

#Calcula las nuevas existencias
#Input: 
def nuevasExistencias():
    ExistenciasNew =  {k : v - items[k] for k, v in Existencias.items() if k in items}
    Existencias.update(ExistenciasNew)
    return Existencias

#Actualizar existencias
Existencias = nuevasExistencias()

#Calcula los totales
#Input: lista = itemsNombre
def totales():
    total = 0
    for i in items:
        total = total+items[i]
    return round(total, 2)

#Asignar varibale total
totals = totales()

#Imprime el recibo
#Inputs: lista = comprasNombre, lista2 = itemsNombre, total = totalNombre, nombre = Nombre
def recibo():
    #Crea lista de las cantidades ordenadas
    cantidades = list(compras.values())
    #Crea lista de los nombres de los productos ordenados
    nombresP = list(items.keys())
    #Precios unitarios
    preciou = list(Precios.values())
    #Crea lista de el valor de cada producto
    precio = list(items.values())
    #Junta las listas anteriores en una lista de listas
    complete = [cantidades, nombresP, preciou, precio]
    
    #Crea separación
    print("------------------------")
    
    print("Recibo de " + str(nombres) + " \n")
    
    #Imprime las listas verticalmente una al lado de la otra
    for a in zip(*complete):
        print(*a)
        
    #Imprime total
    print("\nTotal: " + str(totals))
    
    print("------------------------")
    #Ejecuta funcion fin
    fin()
    

#Da opcion de terminar o hacer otra compra
def fin():
    print("Inserte cualquier cosa para realizar otra compra o inserte ""Fin"" para terminar")
    otravez = input("Otra compra o Fin: ")
    if otravez == "Fin":
        print("Gracias por comprar!")
    else:
        ejecutar()


#Ejecuta el codigo de nuevo
def ejecutar():
    crearCompra()
    compra, nombre = crearCompra()
    items = calcularPrecios()
    total = totales()
    Existencias = nuevasExistencias()
    recibo()
    

recibo()









   






    
        




