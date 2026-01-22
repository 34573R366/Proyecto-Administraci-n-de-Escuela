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
#Me inventé un verificador de tipos STR, en caso de que el usuario escriba un valor que sea posible convertir a float, ese valor por supuesto quedaría descartado como un nombre y clasificado como False
def Verificar_STR (Texto):
    try: 
        float(Texto)
        return False
    except ValueError:
        return True

def Verificar_INT (Texto):
    try: 
        int(Texto)<20
        return True
    except ValueError:
        return False


while Contador==0:
    print("")
    Contador=1
    print("Bienvenido al organizador de eventos, a continuación se le presentarán las opciones disponibles")
    print("Opciones: ")
    print("1- Organizar un evento")
    print("2- Ver eventos organizados")
    Opcion_Elegida=input("Introduzca el número de la opción que desea: ")

    #En el caso de que el usuario haya elegido organizar un evento
    if Opcion_Elegida=="1":
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
        if len(Nombre_Organizador)>=1 and Verificar_STR(Nombre_Organizador)==True:    
            Profesor_Elegido=input("Introduzca el nombre del profesor con el que desea organizar la conferencia teniendo en cuenta los que se encuentran disponibles: ")
            Aula_Elegida=input("Introduzca el aula en la que desea realizar la conferencia teniendo en cuenta las aulas disponibles: ")
            Horario_Elegido=input("Introduzca la hora en la que desea realizar la conferencia teniendo en cuenta los horarios disponibles: ")
            Personas_Asignadas=input("Introduzca el número de personas que van a asistir a su evento: ")
            print("")

            #Aquí se va a chequear la disponibilidad de los recursos
            if Profesor_Elegido in Unused_Resources["Profesores"] and Aula_Elegida in Unused_Resources["Aulas"]:
                if Horario_Elegido in Unused_Resources["Aulas"][Aula_Elegida]["Horarios"] and Horario_Elegido in Unused_Resources["Profesores"][Profesor_Elegido]:
                    if Verificar_INT(Personas_Asignadas)==True:
                        if int(Personas_Asignadas)<=Unused_Resources["Aulas"][Aula_Elegida]["Capacidad"]:

                            #En caso de que los recursos estén disponibles, se van a eliminar de los recursos disponibles y se van a añadir a los recursos en uso, pero como las aulas y los profesores se pueden utilizar varias veces a lo largo del día, solo se eliminarán los horarios
                            Used_resources.append((Nombre_Organizador, Aula_Elegida, Profesor_Elegido, Horario_Elegido, Personas_Asignadas))
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
                            print("El aula que ha elegido no tiene capacidad para ese número de personas")
                    else:
                        print("Solo puede ingresar valores enteros para la capacidad")
                else:
                    print("Usted ha intentado usar un recurso que no se encuentra disponible en el horario indicado")
            else:
                print("Error, ha cometido un error al escribir el aula o profesor")
        else:
            print("Solamente se admiten valores alfabéticos")
        Contador=0
    
    #En el caso de que el usuario haya decidido ver la lista de eventos pendientes
    elif Opcion_Elegida=="2":
        if len(Used_resources) != 0:
            for Elemento in Used_resources:
                print("Evento número " + str(Contador_de_eventos+1) + ", organizador: " + Elemento[0] + ", local: " + Elemento[1], ", profesor: " + Elemento[2] + ", horario: " + Elemento[3] + ", capacidad reservada: " + Elemento[4])
                Contador_de_eventos+=1
        else:
            print("No se ha registrado ningún evento")

        #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
        Repetir=input("Desea realizar otra operación?: ")
        if Repetir.lower() in ["sí", "si"]:
            Contador=0
            print("")
        elif Repetir.lower()=="no":
            print("Vale, gracias por utilizar mi programa")
        else:
            print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
    else:
        print("Usted ha elegido una opción inválida, por favor vuelva a intentarlo")
        Contador=0
