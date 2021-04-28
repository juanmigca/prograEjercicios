#Evaluacion individual 1
#Juan Miguel Gonzalez-Campo
#Carnet: 21077

#Importar modulo turtle
import turtle
#Variable que cambiara el numero de turnos
Turno = 0
#Funcion donde el usuario ingresa sus respuestas a las preguntas
def preguntas():
    print("Por favor conteste las preguntas solamente con \"Si\" o \"No\"")
    condicion1 = input("¿Es trabajador de establecimientos de salud asistencial que atienden pacientes con COVID-19? ")
    condicion2 = input("¿Es trabajador de establecimientos de salud asistencial no incluidos en sub-fase 1 y comunitarios de apoyo? ")
    condicion3 = input("¿Es estudiante de ciencias de la salud y afines que realizan prácticas asistenciaales en establecimientos de salud? ")
    condicion4 = input("¿Pertence a cuerpos de socorro, es trbajador funerario o es personal que labora en instituciones de adultos mayores? ")
    condicion5 = input("¿Es una persona internada en hogar o institución de adulto mayor? ")
    condicion6 = input("¿Trabaja en el sector de salud como administrativo? ")
    condicion7 = input("¿Tiene 70 años o más? ")
    condicion8 = input("¿Tiene una o más de las condiciones siguientes: Hipertensión arterial que requiere medicamento, diabetes mellitus, enfermedad pulmonar crónica,enfermedad renal crónica,enfermedades cardiovasculares y cerebrovasculares, inmunosupresión(VIH, cáncer, uso de inmunosupresores) u obesidad (IMC ≥30)? ")
    #lista donde se guardaran las respuestas
    condiciones = []
    #Se guardan las respuestas en la lista
    condiciones.append(condicion1)
    condiciones.append(condicion2)
    condiciones.append(condicion3)
    condiciones.append(condicion4)
    condiciones.append(condicion5)
    condiciones.append(condicion6)
    condiciones.append(condicion7)
    condiciones.append(condicion8)
    return condiciones

#Esta funcion cambia el formato de las respuestas para mas facil interpretacion
def interpretarInputs():
    #Llama funcion preguntas
    condiciones = preguntas()
    #Quita los espacios antes y despues de la respuesta
    condiciones0 = [x.strip() for x in condiciones]
    #Vuelve las respuestas minusculas
    condiciones1 = [x.lower() for x in condiciones0]
    #Cambia las respuestas de si o no a valores booleanos
    condiciones2 = [True if x == "si" else False for x in condiciones1]
    return condiciones2

def evaluarPaciente():
    #Llama funcion interpretarInputs
    condiciones = interpretarInputs()
    #Revisa si alguna de las respuestas es verdad y si si le da un turno
    if any(condiciones) == True:
        crearTurno()
    else:
        noTurno()

        
def crearTurno():
    #Llama a la variable turno
    global Turno
    #Sube 1 a turno cada vez que alguien cumple las condiciones y obtiene un turno
    Turno += 1
    #limpia la consola de turtle
    turtle.clear()
    #Le da al usuario su turno
    turtle.hideturtle()
    turtle.Screen().bgcolor("green")
    turtle.write("El turno asignado es: \n" +str(Turno), align='center', font=('Arial', 40, 'normal'))
    #El titulo de la ventana indica que no se debe cerrar para evitar errores de turtle
    turtle.title("No cierre esta pestaña")
    #Inicia la funcion fin
    fin()
    
def noTurno():
    #Crea el octagono rojo
    turtle.clear()
    turtle.hideturtle()
    turtle.pensize(8)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(45)
    turtle.forward(120)
    turtle.left(45)
    turtle.forward(120)
    turtle.left(45)
    turtle.forward(120)
    turtle.left(45)
    turtle.forward(120)
    turtle.left(45)
    turtle.forward(120)
    turtle.left(45)
    turtle.forward(120)
    turtle.left(45)
    turtle.forward(120)
    turtle.left(45)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    #Le dice al usuario que no tiene un turno
    turtle.write("No pertenece \n al grupo actual \n de vacunación", align='center', font=('Arial', 20, 'normal'))
    #El titulo de la ventana indica que no se debe cerrar para evitar errores de turtle
    turtle.title("No cierre esta pestaña")
    fin()
    
#Pregunta al usuario si se va ingresar los datos de otro paciente o si se va a finalizar
def fin():
    print("---------------------------------------------")
    print("Si desea ingresar los datos de un nuevo usuario ingrese cualquier letra, de lo contrario ingrese “fin”. ")
    otravez = input("Otro usuario o fin: ")
    #Si se escribe fin se finaliza el programa
    if otravez == "fin":
        turtle.bye()
        print("Gracias por su tiempo.")
    else: #Si escribe cualquier cosa que no sea fin comienza el programa de nuevo
        print("------------------------")
        turtle.clear()
        evaluarPaciente()
        
#Esta linea comienza el programa llamando a la funcion evaluarPaciente
evaluarPaciente()