import json

Contador=0
IDs=0

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
        "Laboratorio":{
             "Capacidad":45,
             "Horarios": ["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"]
        },
    },
    "Profesores":{
        "Idania Urrutia":["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"],
        "Alejandro Piad":["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"],
        "Celia González": ["09:15", "10:40", "12:05", "13:30", "14:55", "16:20", "17:45"]
    },
    "Materiales":{
        "Proyector": {
            "Cantidad": 2
        }
    }
}

Used_resources=[]

Control_de_Cuentas=[]

#Me inventé un verificador de tipos

def verificar_tipo(texto):
    try:
        valor_int = int(texto)
        return "int"
    except ValueError:
        try:
            valor_float = float(texto)
            return "float"
        except ValueError:
            return "str"

def guardar_datos():
    try:
        datos={
            "Unused_Resources": Unused_Resources,
            "Used_Resources": Used_resources
        }
        with open("eventos_guardados.json","w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except:
        print("No fue posible guardar sus datos")

def cargar_datos():
    global Unused_Resources, Used_resources,IDs
    try:
        with open("eventos_guardados.json", "r", encoding="utf-8") as archivo:
            datos=json.load(archivo)
            Unused_Resources=datos["Unused_Resources"]
            Used_resources=datos["Used_Resources"]
            if Used_resources:
                Last_Event=Used_resources[-1]
                IDs=Last_Event[0]
            else:
                IDs=0
    except:
        print("No se encontraron datos de recursos usados guardados, iniciando programa")

def guardar_usuario():
    try:
        with open("Usuarios.json","w", encoding="utf-8") as cuentas:
            json.dump(Control_de_Cuentas, cuentas, indent=4, ensure_ascii=False)
    except:
        print("No fue posible guardar sus datos")

def cargar_usuario():
    global Control_de_Cuentas
    try:
        with open("Usuarios.json", "r", encoding="utf-8") as cuentas:
            Usuarios=json.load(cuentas)
            Control_de_Cuentas=Usuarios
    except:
        print("No se encontraron datos de usuario guardados, iniciando programa")
#Aquí creé unas funciones que me permitan crear o sobrescribir un archivo .json, a partir de los diccionarios y listas ya creados y a partir de ese archivo reconstruir los diccionarios y listas

while Contador==0:
    cargar_datos()
    cargar_usuario()
    print("")
    Contador=1
    Bienvenida_Cuenta=input("Sea bienvenido al organizador de eventos. Este programa fue creado para que los líderes de grupo pudiese organizar consultas con sus profesores, por lo tanto, aquí podrá elegir un horario, local y profesor para realizar su consulta. Tiene usted ya una cuenta creada?: ")
    if Bienvenida_Cuenta.lower() in ["si", "sí", "s", "yes", "y"]:
        Nombre_Usuario=input("Por favor, introduzca su nombre de usuario: ")
        Contraseña=input("Por favor, introduzca su contraseña: ")
        if [Nombre_Usuario, Contraseña] in Control_de_Cuentas:
            print("")
            print("")
            print("Bienvenido al organizador de eventos, " + Nombre_Usuario + " a continuación se le presentarán las opciones disponibles")
            print("Opciones: ")
            print("1- Organizar un evento")
            print("2- Ver eventos organizados")
            print("3- Cancelar un evento")
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
                if len(Nombre_Usuario)>=1 and verificar_tipo(Nombre_Usuario)=="str":    
                    Profesor_Elegido=input("Introduzca el nombre del profesor con el que desea organizar la conferencia teniendo en cuenta los que se encuentran disponibles: ")
                    Aula_Elegida=input("Introduzca el aula en la que desea realizar la conferencia teniendo en cuenta las aulas disponibles: ")
                    Horario_Elegido=input("Introduzca la hora en la que desea realizar la conferencia teniendo en cuenta los horarios disponibles: ")
                    Personas_Asignadas=input("Introduzca el número de personas que van a asistir a su evento: ")
                    Material_Elegido=input("Desea utilizar un proyector? (si/no): ")
                    print("")

                    #Voy a hacer esta pequeña sección para que el usuario tenga mayor flexibilidad y pueda trabajar con algunos errores
                    if Profesor_Elegido.lower() in ["idania", "idania urrutia"]:
                        Profesor_Elegido="Idania Urrutia"
                        PID="1"
                    elif Profesor_Elegido.lower() in ["alejandro", "piad", "alejandro piad"]:
                        Profesor_Elegido="Alejandro Piad"
                        PID="2"
                    elif Profesor_Elegido.lower() in ["celia", "celia gonzalez", "celia gonzález"]:
                        Profesor_Elegido=("Celia González")
                        PID="3"
                    #Ahora el usuario puede escribir el nombre del profesor de distintas maneras sin preocuparse por mayúsculas ni apellidos

                    if Aula_Elegida.lower() in ["1", "aula 1", "aula1"]:
                        Aula_Elegida="Aula 1"
                        SID="1"
                    elif Aula_Elegida.lower() in ["5", "aula 5", "aula5"]:
                        Aula_Elegida="Aula 5"
                        SID="2"
                    elif Aula_Elegida.lower() in ["laboratorio", "lab"]:
                        Aula_Elegida="Laboratorio"
                        SID="3"
                    #Ahora el usuario puede escribir el aula en la que desea realizar la conferencia de manera más simplificada

                    if Horario_Elegido == "09:15":
                        TID="1"
                    elif Horario_Elegido == "10:40":
                        TID="2"
                    elif Horario_Elegido == "12:05":
                        TID="3"
                    elif Horario_Elegido == "13:30":
                        TID="4"
                    elif Horario_Elegido == "14:55":
                        TID="5"
                    elif Horario_Elegido == "16:20":
                        TID="6"
                    elif Horario_Elegido == "17:45":
                        TID="7"
                    else:
                        TID="0"

                    #Aquí se va a chequear la disponibilidad de los recursos
                    if not Profesor_Elegido=="Alejandro Piad" and Aula_Elegida=="Laboratorio":
                        print("Solo Alejandro Piad puede dar clases en el laboratorio")
                        Contador=0
                    else:
                        if Profesor_Elegido in Unused_Resources["Profesores"] and Aula_Elegida in Unused_Resources["Aulas"]:
                            if Horario_Elegido in Unused_Resources["Aulas"][Aula_Elegida]["Horarios"] and Horario_Elegido in Unused_Resources["Profesores"][Profesor_Elegido]:
                                if verificar_tipo(Personas_Asignadas)=="int":
                                    if int(Personas_Asignadas)<=Unused_Resources["Aulas"][Aula_Elegida]["Capacidad"] and int(Personas_Asignadas)>0:

                                        #En caso de que los recursos estén disponibles, se van a eliminar de los recursos disponibles y se van a añadir a los recursos en uso, pero como las aulas y los profesores se pueden utilizar varias veces a lo largo del día, solo se eliminarán los horarios
                                        IDs=int(SID+PID+TID)
                                        Personas_Asignadas=int(Personas_Asignadas)
                                        evento=(IDs,Nombre_Usuario,Aula_Elegida,Profesor_Elegido,Horario_Elegido,Personas_Asignadas)
                                        if Material_Elegido.lower() in ["sí", "si"]:
                                            if Unused_Resources["Materiales"]["Proyector"]["Cantidad"]>0:
                                                Unused_Resources["Materiales"]["Proyector"]["Cantidad"]-=1
                                                evento=evento+("Proyector",)
                                                print("Se ha asignado un proyector")
                                            else:
                                                print("No quedan proyectores disponibles")
                                        elif Material_Elegido.lower=="no":
                                            print("No se le ha asignado un proyector")
                                        else:
                                            print("No ha sido posible interpretar lo que ha escrito, pero se asumirá que no desea el proyector")
                                        Used_resources.append(evento)
                                        Unused_Resources["Aulas"][Aula_Elegida]["Horarios"].remove(Horario_Elegido)
                                        Unused_Resources["Profesores"][Profesor_Elegido].remove(Horario_Elegido)
                                        print("Su evento ha sido añadido exitosamente, el ID de su evento es: " + str(IDs))
                                        guardar_datos()

                                        #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
                                        Repetir=input("Desea realizar otra operación?: ")
                                        if Repetir.lower() in ["sí", "si"]:
                                            Contador=0
                                        elif Repetir.lower()=="no":
                                            print("Vale, gracias por utilizar mi programa")
                                            Contador=1
                                        else:
                                            print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
                                            Contador=1

                                    else:
                                        print("El aula que ha elegido no tiene capacidad para ese número de personas")
                                else:
                                    print("Solo puede ingresar valores enteros positivos para la capacidad")
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
                        print("ID de evento: " + str(Elemento[0]) + ", organizador: " + Elemento[1] + ", local: " + Elemento[2], ", profesor: " + Elemento[3] + ", horario: " + Elemento[4] + ", capacidad reservada: " + str(Elemento[5]) + ", material: " + Elemento[6] if len(Elemento)>6 else "Ninguno")
                else:
                    print("No se ha registrado ningún evento")

                #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
                Repetir=input("Desea realizar otra operación?: ")
                if Repetir.lower() in ["sí", "si"]:
                    Contador=0
                    print("")
                elif Repetir.lower()=="no":
                    print("Vale, gracias por utilizar mi programa")
                    Contador=1
                else:
                    print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
                    Contador=1
            
            #El usuario va a escribir el ID de su evento y e caso de que este evento esté registrado bajo el nombre del usuario va a poder hacerlo
            elif Opcion_Elegida=="3":
                found=False
                ID_Elegido=input("Introduzca el ID del evento que desea eliminar: ")
                if verificar_tipo(ID_Elegido)=="int":
                    ID_Elegido=int(ID_Elegido)
                    for Elemento in Used_resources:    
                        if ID_Elegido==Elemento[0] and Nombre_Usuario==Elemento[1]:
                            if Elemento[4] not in Unused_Resources["Aulas"][Elemento[2]]["Horarios"]:
                                Unused_Resources["Aulas"][Elemento[2]]["Horarios"].append(Elemento[4])
                            if Elemento[4] not in Unused_Resources["Profesores"][Elemento[3]]:
                                Unused_Resources["Profesores"][Elemento[3]].append(Elemento[4])
                            if len(Elemento)>6 and Elemento[6]=="Proyector":
                                Unused_Resources["Materiales"]["Proyector"]["Cantidad"]+=1
                            Used_resources.remove((Elemento))
                            print("Su evento ha sido eliminado exitosamente")
                            guardar_datos()
                            found=True
                            break
                    if not found:
                        print("No existe ningún evento creado por usted con ese ID")

                    #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
                    Repetir=input("Desea realizar otra operación?: ")
                    if Repetir.lower() in ["sí", "si"]:
                        Contador=0
                    elif Repetir.lower()=="no":
                        print("Vale, gracias por utilizar mi programa")
                        Contador=1
                    else:
                        print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
                        Contador=1
                        
                else:
                    print("Usted ha introducido un ID inválido")
                    Contador=0
            else:
                print("Usted ha elegido una opción inválida, por favor vuelva a intentarlo")
                Contador=0
        else:
            print("Lo sentimos, usted no posee una cuenta en nuestras bases de datos, por favor, vuelva a intentarlo.")
    elif Bienvenida_Cuenta.lower() in ["no", "n"]:
        Desea_Crear=input("Desea crear una cuenta?: ")
        if Desea_Crear.lower() in ["yes", "y", "si", "sí", "s"]:
            Nombre_Usuario=input("Introduzca su nombre de usuario: ")
            Contraseña=input("Introduzca la contraseña (Debe tener cuatro o más caracteres): ")
            if len(Nombre_Usuario)>=1 and verificar_tipo(Nombre_Usuario)=="str" and len(Contraseña)>=4:
                Cuenta_Existente=False
                if len(Control_de_Cuentas)>=1:
                    for Elemento in Control_de_Cuentas:
                        if Nombre_Usuario in Elemento:
                            print("Ese nombre de usuario  ya está en uso")
                            Cuenta_Existente=True
                            Contador=0
                            break
                        elif Nombre_Usuario not in Elemento:
                            Cuenta_Existente=False
                if Cuenta_Existente==False:
                    Control_de_Cuentas.append([Nombre_Usuario, Contraseña])
                    guardar_usuario()
                    print("Su cuenta ha sido registrada con éxito")
                    Contador=0
            else:
                print("Lo sentimos, los datos introducidos son inválidos")
                Contador=0
        elif Desea_Crear.lower() in ["no", "n"]:
            print("Vale, como desee")
            Contador=1
        else:
            print("Supondré que no lo desea")
            Contador=1
    else:
        print("Usted ha dado una respuesta inválida")
        Contador=0


