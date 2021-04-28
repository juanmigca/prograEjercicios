import csv
import datetime

#Crea el archivo csv.
with open('ejercicio.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Fecha', 'Nombre', 'Edad', 'Peso', 'Altura', 'Hora Inicio', 'Hora fin', 'Duracion', 'Objetivo'])

#Esta funcion lee y desplega el archivo csv con sus elementos.
def leerarchivo():
    with open('ejercicio.csv', 'r', encoding='utf-8') as f:
        leer = csv.reader(f)
        for row in leer:
            print(row)
        menu()
            
#Esta funcion añade un registro al archivo csv.       
def anadirregistro():
    #Lista vacia donde se guardaran los inputs del usuario
    registro = []
    #Inputs del usuario
    registro1 =input('Ingrese la fecha en formato aaaa/mm/dd: ')
    #Convierte el input en un tipo date
    anio, mes, dia = map(int, registro1.split('/'))
    fecha = datetime.date(anio, mes, dia)
    
    registro2 =input('Ingrese su nombre: ')
    registro3 =input('Ingrese su edad: ')
    registro4 =input('Ingrese su peso: ')
    registro5 =input('Ingrese su altura: ')
    registro6 =input('Ingrese la hora de inicio de forma hh:mm y use formato de 24 horas: ')
    registro7 =input('Ingrese la hora final de forma hh:mm y use formato de 24 horas: ')
    #COnvierte los inputs del registro 6 y 7 en tipos time.
    hora1, minuto1 = map(int, registro6.split(':'))
    tiempoinicio = datetime.time(hora1, minuto1)
    hora2, minuto2 = map(int, registro7.split(':'))
    tiempofin = datetime.time(hora2, minuto2)
    #Calcula la duracion del ejercicio
    duracion = datetime.datetime.combine(datetime.date.today(), tiempofin) - datetime.datetime.combine(datetime.date.today(), tiempoinicio)
    #Revisa si el jercicio spero los 30 minutos
    objetivo = ""
    if duracion >= datetime.timedelta(minutes=30):
        objetivo = "Cumplido"
    else:
        objetivo = "No cumplido"
    #Une las variables anterioras a la lista registro
    registro.append(fecha.strftime("%D"))
    registro.append(registro2)
    registro.append(registro3)
    registro.append(registro4)
    registro.append(registro5)
    registro.append(tiempoinicio.strftime("%R"))
    registro.append(tiempofin.strftime("%R"))
    registro.append(str(duracion))
    registro.append(objetivo)
    #Añade el nuevo registro al archivo csv
    with open('ejercicio.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(registro)
    #regresa al menu
    menu()


def masregistros():
    #Abre la columna Nombre como una lista
    with open("ejercicio.csv") as f:
        usuarios = [row["Nombre"] for row in csv.DictReader(f)]
    #Encuentra el registro, osea el usuario, que mas se repite
    frecuente = max(set(usuarios), key = usuarios.count)
    #Imprime el usurio que mas ejercicios ha reportado
    print("La persona que más ha reportado ejercicios es " +str(frecuente))
    #Regresa al menu
    menu()

    
def mayorregistro():
    #Guarda la columna de Duracion como una lista
    with open("ejercicio.csv") as f:
        duraciones = [row["Duracion"] for row in csv.DictReader(f)]
        #Guarda la columna Nombre como una lista
    with open("ejercicio.csv") as f:
        nombres = [row["Nombre"] for row in csv.DictReader(f)]
    #Elimina los ":" de los valores de duraciones
    duraciones2 = [s.replace(':','') for s in duraciones]
    #Convierte los valores de duraciones en int
    duraciones3 = [int(i) for i in duraciones2]
    #Encuentra la duración mas larga
    duracionmax = max(duraciones3)
    #Encuentra la posicion de la duracion mas larga
    duracionmaxpos = duraciones3.index(duracionmax)
    #Utiliza la posicion de la duracion mas larga para encontrar quien fue quien hizo esa sesión
    nombremax = nombres[duracionmaxpos]
    #Imprime quien tuvo la sesión de ejercicio más larga
    print("La persona que más tiempo ha durado haciendo ejercicio en unsa sola sesión es " +str(nombremax))
    menu()

def menu():
    print("\n-----------------------")
    print("Ingrese 1 para leer el archivo, 2 para agregar un nuevo registro, \n3 para desplegar el usuario que más registros ha hecho, 4 para desplegar el usuario que ha hecho el ejercicio mas largo. \nO presione 5 para finalizar.")
    opcion = input("Ingrese el número: ")
    if opcion == "1":
        print("\n-----------------------")
        leerarchivo()
    elif opcion == "2":
        print("\n-----------------------")
        anadirregistro()
    elif opcion == "3":
        print("\n-----------------------")
        masregistros()
    elif opcion == "4":
        print("\n-----------------------")
        mayorregistro()
    elif opcion == "5":
        print("\n-----------------------")
        print("Consola apagada")

menu()
    

    



        
