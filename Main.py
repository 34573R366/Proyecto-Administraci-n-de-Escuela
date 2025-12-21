print("Bienvenido al organizador de eventos, a continuación se le presentarán las opciones disponibles")
print("Opciones: ")
print("1- Organizar un evento")
print("2- Ver eventos organizados")
Contador=0
Contador_de_eventos=0

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

Used_resources=[]

while Contador==0:
    Contador=1
    Opcion_Elegida=int(input("Introduzca el número de la opción que desea: "))

    #En el caso de que el usuario haya elegido organizar un evento
    if Opcion_Elegida==1:
        #Imprimiendo una tabla con las aulas y sus características
        print ("Aulas".ljust(10) + "Capacidad".ljust(13)+ "Horarios".ljust(0))
        print ("-"*70)
        for aula, datos in Unused_Resources["Aulas"].items():
            horarios= ", ".join(datos["Horarios"])
            fila=aula.ljust(13) +str(datos["Capacidad"]).ljust(10) + horarios
            print(fila)

        print("")
        
        #Imprimiendo una tabla con los profes y sus horarios
        print ("Profesores".ljust(20) + "Horarios".ljust(0))
        print ("-"*67)
        for profe, horario in Unused_Resources["Profesores"].items():
            horarios=", ".join(horario)
            fila=profe.ljust(20) + horarios
            print(fila)
        print("")
        print("A continuación se le va a pedir que introduzca las opciones deseadas, por favor, asegúrese de escribir teniendo en cuenta la disponbilidad de los recursos mostrados anteriormente, así como el formato en el que se encuentran escritos")
        print("")

        #Aquí el usuario va a elegir qué elementos desea en su evento
        Nombre_Organizador=input("Introduzca su nombre y apellidos: ")
        Profesor_Elegido=input("Introduzca el nombre del profesor con el que desea organizar la conferencia teniendo en cuenta los que se encuentran disponibles: ")
        Aula_Elegida=input("Introduzca el aula en la que desea realizar la conferencia teniendo en cuenta las aulas disponibles: ")
        Horario_Elegido=input("Introduzca la hora en la que desea realizar la conferencia teniendo en cuenta los horarios disponibles: ")
        print("")

        #Aquí se va a chequear la disponibilidad de los recursos
        if Profesor_Elegido in Unused_Resources["Profesores"] and Aula_Elegida in Unused_Resources["Aulas"]:
            if Horario_Elegido in Unused_Resources["Aulas"][Aula_Elegida]["Horarios"] and Horario_Elegido in Unused_Resources["Profesores"][Profesor_Elegido]:

                #En caso de que los recursos estén disponibles, se van a eliminar de los recursos disponibles y se van a añadir a los recursos en uso, pero como las aulas y los profesores se pueden utilizar varias veces a lo largo del día, solo se eliminarán los horarios
                Used_resources.append((Nombre_Organizador, Aula_Elegida, Profesor_Elegido, Horario_Elegido))
                Unused_Resources["Aulas"][Aula_Elegida]["Horarios"].remove(Horario_Elegido)
                Unused_Resources["Profesores"][Profesor_Elegido].remove(Horario_Elegido)
                print("Su evento ha sido añadido exitosamente")

                #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
                Repetir=input("Desea realizar otra operación?: ")
                if Repetir.lower() in ["sí", "si"]:
                    Contador=0
                elif Repetir.lower()=="no":
                    print("Vale, gracias por utilizar mi programa")
                else:
                    print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")

            else:
                print("Usted ha intentado usar un recurso que no se encuentra disponible")
        else:
            print("Error, valores no válidos, vuelva a intentarlo")
            Contador=0
    #En el caso de que el usuario haya decidido ver la lista de eventos pendientes
    elif Opcion_Elegida==2:
        for Elemento in Used_resources:
            print("Evento número: " + str(Contador_de_eventos+1) + ", organizador: " + Elemento[0] + ", Aula: " + Elemento[1], ", profesor: " + Elemento[2] + ", horario: " + Elemento[3])
            Contador_de_eventos+=1

        #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
        Repetir=input("Desea realizar otra operación?: ")
        if Repetir.lower() in ["sí", "si"]:
            Contador=0
        elif Repetir.lower()=="no":
            print("Vale, gracias por utilizar mi programa")
        else:
            print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
    else:
        print("Usted ha elegido una opción inválida, por favor vuelva a intentarlo")
        Contador=0