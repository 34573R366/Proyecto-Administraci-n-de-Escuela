print("Bienvenido al organizador de eventos, a continuación se le presentarán las opciones disponibles")
print("Opciones: ")
print("1- Organizar un evento")
print("2- Ver eventos pendientes")
Contador=0

Unused_Resources={
    "Aulas":{
        "Aula 1":{
             "Capacidad":30,
             "Horarios": ["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"]
        },
        "Aula 5":{
             "Capacidad":40,
             "Horarios": ["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"]
        },
        "Aula 6":{
             "Capacidad":45,
             "Horarios": ["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"]
        },
    },
    "Profesores":{
        "Idania Urrutia":["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"],
        "Alejandro Piad":["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"],
        "Celia González": ["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"]
    },
}

Used_resources={
    "Organizador":[],
    "Aulas":{
        "Aula 1": {
            "Horarios":[]
        },
        "Aula 5": {
            "Horarios":[]
        },
        "Aula 6": {
            "Horarios":[]
        },
    },
    "Profesores":{
        "Idania Urrutia":[],
        "Alejandro Piad": [],
        "Celia González": []
    },
}

while Contador==0:
    Contador==1
    Opcion_Elegida=int(input("Introduzca el número de la opción que desea: "))
    if Opcion_Elegida==1:
        print("Aulas disponibles: " + str(Unused_Resources["Aulas"]))
        print("Rofesores disponibles: " + str(Unused_Resources["Profesores"]))
        print("")
        print("A continuación se le va a pedir que introduzca las opciones deseadas, por favor, asegúrese de escribir teniendo en cuenta la disponbilidad de los recursos mostrados anteriormente, así como el formato en el que se encuentran escritos")

        #Aquí el usuario va a elegir qué elementos desea en su evento
        Nombre_Organizador=input("Introduzca su nombre y apellidos: ")
        Profesor_Elegido=input("Introduzca el nombre del profesor con el que desea organizar la conferencia teniendo en cuenta los que se encuentran disponibles: ")
        Aula_Elegida=input("Introduzca el aula en la que desea realizar la conferencia teniendo en cuenta las aulas disponibles: ")
        Horario_Elegido=input("Introduzca la hora en la que desea realizar la conferencia teniendo en cuenta los horarios disponibles: ")

        #Aquí se va a chequear la disponibilidad de los recursos
        if Horario_Elegido in Unused_Resources["Aulas"[Aula_Elegida["Horarios"]]] and Horario_Elegido in Unused_Resources["Profesores"[Profesor_Elegido]]:

            #En caso de que los recursos estén disponibles, se van a eliminar de los recursos disponibles y se van a añadir a los recursos en uso, pero como las aulas y los profesores se pueden utilizar varias veces a lo largo del día, solo se eliminarán los horarios
            Used_resources["Organizador"].append(Nombre_Organizador)
            Used_resources["Aulas"[Aula_Elegida["Horarios"]]].append(Horario_Elegido)
            Used_resources["Profesores"[Profesor_Elegido]].append(Horario_Elegido)
            Unused_Resources["Aulas"[Aula_Elegida["Horarios"]]].remove(Horario_Elegido)
            Unused_Resources["Profesores"[Profesor_Elegido]].remove(Horario_Elegido)
            print("Su evento ha sido añadido exitosamente")

            #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
            Repetir=input("Desea realizar otra operación?: ")
            if Repetir.lower()=="si" or Repetir.lower=="sí":
                Contador==0
            elif Repetir.lower=="no":
                print("Vale, gracias por utilizar mi programa")
                Contador==1
            else:
                print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
        else:
            print("Usted ha intentado usar un recurso que no se encuentra disponible")   