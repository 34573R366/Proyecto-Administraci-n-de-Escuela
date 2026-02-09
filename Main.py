import json
from datetime import datetime, timedelta

#Declaración de variables, listas y diccioarios a usar

Contador=0
IDs=0
hora_min=datetime.strptime("09:15","%H:%M")
hora_max=datetime.strptime("17:45","%H:%M")
Más_Operaciones=True

Cantidad_eventos_profesor={
    "Alejandro Piad":0,
    "Celia González":0,
    "Idania Urrutia":0,
}

Unused_Resources={
    "Aulas":{
        "Aula 1":{
             "Capacidad":30,
        },
        "Aula 5":{
             "Capacidad":40,
        },
        "Laboratorio":{
             "Capacidad":45,
        },
    },
    "Profesores":{
        "Idania Urrutia": 3-Cantidad_eventos_profesor["Idania Urrutia"],
        "Alejandro Piad": 3-Cantidad_eventos_profesor["Alejandro Piad"],
        "Celia González": 3-Cantidad_eventos_profesor["Celia González"],
    },
    "Materiales":{
        "Proyector": {
            "Cantidad": 2
        }
    }
}

Used_resources=[]

Control_de_Cuentas=[]

#Declaración de funciones a usar

#Esta función se encarga de revisar primeramente si algún evento se solapa con otro. En caso de que el evento no se solape con ninguno va a estar permitido. En caso de que se solape con alguno va a ir buscando yendo de 5 minutos en 5 minutos buscando un hueco disponible
def recomendador_inteligente(aula, profesor, usados, hora_min, hora_max, duración=85):
    inicio=hora_min
    while inicio+timedelta(minutes=duración) <=hora_max:
        candidato=(inicio,inicio+timedelta(minutes=duración))
        conflicto=False
        for evento in usados:
            if (evento[2]==aula or evento[3]==profesor) and intervalos_solapan(candidato, evento[4]):
                conflicto=True
                break
        if not conflicto:
            return candidato
        inicio+=timedelta(minutes=5)
    return None

#Esta función se encarga de crear los intervalos a partir de un str introducido por el usuario con una duración predeterminada de 85 minutos. Va a establecer un inicio convirtiendo lo escrito por el usuario en formato datetime, va a establecer un final sumando el tiempo al inicio y va a retornar una tupla
def crear_intervalo(hora_str, duración_min=85):
    try:
        inicio=datetime.strptime(hora_str, "%H:%M")
        fin=inicio+timedelta(minutes=duración_min)
        if hora_min<=inicio<=hora_max and fin<=hora_max:
            return (inicio,fin)
        else:
            print("El horario debe estar entre 09:15 y 17:45")
            return None
    except Exception as e:
        print(f"Formato inválido. Use HH:MM. Error: {e}")
        return None

#Esta función se encarga de revisar si los intervalos se cruzan entre sí (es básicamente la cabeza de la organización de eventos). Va a revisar si el inicio de un evento se cruza con el final de otro y viceversa
def intervalos_solapan(i1, i2):
    try:
        inicio1,fin1=i1
        inicio2,fin2=i2
        return inicio1<fin2 and inicio2<fin1
    except Exception as e:
        print(f"Error, ha usado un intervalo inválido. Intente de nuevo. Error: {e}" )
        return None
    
#Esta función se encarga de verificar el tipo de un input, lo hice para verificar el formato de los nombres de los profesores y cuentas, así como para la escritura de los horarios deseados en el momento de organizar las consultas (para que no me salten errores inesperados)
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

#Esta función se encarga de coger los datos de los diccionarios en este archivo de formato python y llevarlos a otro archivo de formato json donde estarán almacenados y podrán ser accedidos posteriormente. Crea un diccionario con etiquetas de igual nombre que los diccionarios del archivo python y luego abre el json en modo de escritura para copiar el diccionario creado. Además esta función es de vital importancia pues permite el correcto almacenamiento de los datos datetime
def guardar_datos():
    try:
        datos_para_guardar = {
            "Unused_Resources": json.loads(json.dumps(Unused_Resources)),
            "Used_Resources": [],
            "Cantidad_eventos_profesor": Cantidad_eventos_profesor.copy()
        }
        
        for evento in Used_resources:
            evento_lista = list(evento)
            if len(evento_lista) > 4:
                inicio, fin = evento_lista[4]
                evento_lista[4] = [inicio.isoformat(), fin.isoformat()]
            datos_para_guardar["Used_Resources"].append(evento_lista)
        
        with open("eventos_guardados.json","w", encoding="utf-8") as archivo:
            json.dump(datos_para_guardar, archivo, indent=4, ensure_ascii=False)
        
        print("Datos guardados exitosamente")
        
    except Exception as e:
        print(f"No fue posible guardar sus datos. Error: {e}")

#Esta función se encarga de convertir las listas de strings traídas desde el archivo json en formato datetime para que puedan ser trabajadas con mayor facilidad sin tener que pasar por conversiones datetime.strptime ni datetime.strftime cada vez que se desea trabajar con los datos. Funciona tomando el inicio y el fin del intervalo(en los índices 0 y 1 respectivamente) y convirtiéndolos en formato datetime para posteriormente convertirlos en una tupla, ya que en el archivo json era imposible trabajar con tuplas
def reconstruir_intervalo(lista):
    try:
        if isinstance(lista, tuple) and len(lista) == 2:
            if isinstance(lista[0], datetime) and isinstance(lista[1], datetime):
                return lista
        if isinstance(lista, list) and len(lista) == 2:
            inicio_str = str(lista[0])
            fin_str = str(lista[1])
            if " " in inicio_str and "T" not in inicio_str:
                inicio_str = inicio_str.replace(" ", "T")
            if " " in fin_str and "T" not in fin_str:
                fin_str = fin_str.replace(" ", "T")
            inicio = datetime.fromisoformat(inicio_str)
            fin = datetime.fromisoformat(fin_str)
            return (inicio, fin)
        return None
    except Exception as e:
        print(f"Error reconstruyendo intervalo: {e}")
        return None

#Esta función se encarga de revisar los datos guardados en el archivo json usando el modo lectura. En caso de que el mismo esté vacío se trabajaría con los diccionarios ya alojados en el archivo python, en caso de que existan datos en el json, son copiados hacia el .py para reemplazar los diccionarios existentes
def cargar_datos():
    global Unused_Resources, Used_resources, IDs, Cantidad_eventos_profesor
    try:
        with open("eventos_guardados.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            Unused_Resources = datos["Unused_Resources"]
            Used_resources = datos["Used_Resources"]
            Cantidad_eventos_profesor = datos["Cantidad_eventos_profesor"]
            
            if Used_resources:
                Last_Event = Used_resources[-1]
                IDs = Last_Event[0]
            else:
                IDs = 0
        for i, evento in enumerate(Used_resources):
            if len(evento) > 4:
                intervalo = reconstruir_intervalo(evento[4])
                if intervalo:
                    nuevo_evento = list(evento)
                    nuevo_evento[4] = intervalo
                    Used_resources[i] = tuple(nuevo_evento)
        
        print("Datos cargados correctamente")
        
    except FileNotFoundError:
        print("No se encontraron datos de recursos usados guardados, iniciando programa")
    except Exception as e:
        print(f"Error al cargar datos: {e}")

#Esta función se encarga de tomar los datos introducidos por el usuario y guardados en forma de tupla para copiarlos en el .json
def guardar_usuario():
    try:
        with open("Usuarios.json","w", encoding="utf-8") as cuentas:
            json.dump(Control_de_Cuentas, cuentas, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"No fue posible guardar sus datos. Error: {e}")

#Esta función se encarga de tomar los datos de usuarios y cargarlos directamente en la lista Control_de_Cuentas (en caso de que no contenga ningún dato se trabajaría con los datos almacenados en el .py)
def cargar_usuario():
    global Control_de_Cuentas
    try:
        with open("Usuarios.json", "r", encoding="utf-8") as cuentas:
            Usuarios=json.load(cuentas)
            Control_de_Cuentas=Usuarios
    except Exception as e:
        print(f"No se encontraron datos de usuario guardados, iniciando programa. Error: {e}")

#Inicio del programa

while Contador==0:
    intervalo_usuario=None
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
            while Más_Operaciones==True:
                intervalo_usuario=None
                cargar_datos()
                cargar_usuario()
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
                    print ("Aulas".ljust(10) + "Capacidad".ljust(13))
                    print ("-"*19)
                    for aula, datos in Unused_Resources["Aulas"].items():
                        fila=aula.ljust(13) +str(datos["Capacidad"]).ljust(10)
                        print(fila)
                    print("")
                    #Imprimiendo una tabla con los profes y sus horarios
                    print ("Profesores".ljust(20))
                    print ("-"*14)
                    for profe, horario in Unused_Resources["Profesores"].items():
                        fila=profe.ljust(20)
                        print(fila)
                    print("")

                    print("A continuación se le va a pedir que introduzca las opciones deseadas, por favor, asegúrese de escribir teniendo en cuenta la disponbilidad de los recursos mostrados anteriormente, así como el formato en el que se encuentran escritos")
                    print("")
                    #Aquí el usuario va a elegir qué elementos desea en su evento
                    if len(Nombre_Usuario)>=1 and verificar_tipo(Nombre_Usuario)=="str":    
                        while intervalo_usuario is None:
                            Profesor_Elegido=input("Introduzca el nombre del profesor con el que desea organizar la conferencia teniendo en cuenta los que se encuentran disponibles: ")
                            Aula_Elegida=input("Introduzca el aula en la que desea realizar la conferencia teniendo en cuenta las aulas disponibles: ")
                            #Voy a hacer esta pequeña sección para que el usuario tenga mayor flexibilidad y pueda trabajar con algunos errores
                            #Ahora el usuario puede escribir el nombre del profesor de distintas maneras sin preocuparse por mayúsculas ni apellidos
                            if Profesor_Elegido.lower() in ["idania", "idania urrutia"]:
                                Profesor_Elegido="Idania Urrutia"
                                PID="1"
                            elif Profesor_Elegido.lower() in ["alejandro", "piad", "alejandro piad"]:
                                Profesor_Elegido="Alejandro Piad"
                                PID="2"
                            elif Profesor_Elegido.lower() in ["celia", "celia gonzalez", "celia gonzález"]:
                                Profesor_Elegido=("Celia González")
                                PID="3"

                            #Ahora el usuario puede escribir el aula en la que desea realizar la conferencia de manera más simplificada
                            if Aula_Elegida.lower() in ["1", "aula 1", "aula1"]:
                                Aula_Elegida="Aula 1"
                                SID="1"
                            elif Aula_Elegida.lower() in ["5", "aula 5", "aula5"]:
                                Aula_Elegida="Aula 5"
                                SID="2"
                            elif Aula_Elegida.lower() in ["laboratorio", "lab"]:
                                Aula_Elegida="Laboratorio"
                                SID="3"
                            
                            #Aquí el usuario va a recibir una sugerencia por parte del programa basándose en su elección de profesor y aula para que pueda hacer su consulta lo más temprano posible
                            sugerencia=recomendador_inteligente(Aula_Elegida, Profesor_Elegido, Used_resources, hora_min, hora_max)
                            if sugerencia:
                                print("La hora más temprana disponible es: " + sugerencia[0].strftime("%H:%M"))
                            else:
                                print("No hay huecos disponibles en el rango permitido")
                            Horario_Elegido=input("Introduzca la hora en la que desea realizar la conferencia teniendo en cuenta los horarios disponibles: ")
                            intervalo_usuario=crear_intervalo(Horario_Elegido)
                        Personas_Asignadas=input("Introduzca el número de personas que van a asistir a su evento: ")
                        Material_Elegido=input("Desea utilizar un proyector? (si/no): ")
                        print("")

                        #Aquí se va a chequear la disponibilidad de los recursos. Se van a ver cuestiones como que los profesores que el usuario escribió estén en el listado al igual que las aulas, que los horarios no se solapen, que la cantidad de personas sea congruente con la capacidad de las aulas, así como que haya disponibilidad en la cantidad de proyectores y la cantidad de consultas que han sido asignadas a cada profesor
                        if not Profesor_Elegido=="Alejandro Piad" and Aula_Elegida=="Laboratorio":
                            print("Solo Alejandro Piad puede dar clases en el laboratorio")
                            Más_Operaciones=True
                        else:
                            if Profesor_Elegido in Unused_Resources["Profesores"] and Aula_Elegida in Unused_Resources["Aulas"]:
                                if verificar_tipo(Personas_Asignadas)=="int":
                                    if int(Personas_Asignadas)<=Unused_Resources["Aulas"][Aula_Elegida]["Capacidad"] and int(Personas_Asignadas)>0:
                                        if Cantidad_eventos_profesor[Profesor_Elegido]<3:
                                            Solapamiento=False
                                            for elemento in Used_resources:
                                                if intervalos_solapan(intervalo_usuario, elemento[4]) and Profesor_Elegido==elemento[3]:
                                                    Solapamiento=True
                                                    break
                                                else:
                                                    Solapamiento=False
                                                    continue
                                            if Solapamiento==False:

                                                #En caso de que los recursos estén disponibles, se van a eliminar de los recursos disponibles y se van a añadir a los recursos en uso, pero como las aulas y los profesores se pueden utilizar varias veces a lo largo del día, solo se van a agregar en forma de tuplas a la lista de los recursos usados y se van a eliminar los materiales usados. 
                                                IDs=int(SID+PID+str(Cantidad_eventos_profesor[Profesor_Elegido]))+len(Used_resources)
                                                Personas_Asignadas=int(Personas_Asignadas)
                                                evento=(IDs,Nombre_Usuario,Aula_Elegida,Profesor_Elegido,intervalo_usuario,Personas_Asignadas)
                                                if Material_Elegido.lower() in ["sí", "si"]:
                                                    if Unused_Resources["Materiales"]["Proyector"]["Cantidad"]>0:
                                                        Unused_Resources["Materiales"]["Proyector"]["Cantidad"]-=1
                                                        evento=evento+("Proyector",)
                                                        print("Se ha asignado un proyector")
                                                    else:
                                                        print("No quedan proyectores disponibles")
                                                elif Material_Elegido.lower()=="no":
                                                    print("No se le ha asignado un proyector")
                                                else:
                                                    print("No ha sido posible interpretar lo que ha escrito, pero se asumirá que no desea el proyector")
                                                Used_resources.append(evento)
                                                Cantidad_eventos_profesor[Profesor_Elegido]+=1
                                                print("Su evento ha sido añadido exitosamente, el ID de su evento es: " + str(IDs))
                                                guardar_datos()

                                                #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
                                                Repetir=input("Desea realizar otra operación?: ")
                                                if Repetir.lower() in ["sí", "si"]:
                                                    Más_Operaciones=True
                                                elif Repetir.lower()=="no":
                                                    print("Vale, gracias por utilizar mi programa")
                                                    Más_Operaciones=False
                                                    Contador=1
                                                else:
                                                    print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
                                                    Contador=1
                                                    Más_Operaciones=False
                                            else:
                                                print("El profesor o local escogido ya está ocupado en ese horario")

                                        else: print("El profesor elegido ya ha tenido demasiadas consultas por hoy, vuelva a intentarlo otro día")
                                    else:
                                        print("El aula que ha elegido no tiene capacidad para ese número de personas")
                                else:
                                    print("Solo puede ingresar valores enteros positivos para la capacidad")
                            else:
                                print("Error, ha cometido un error al escribir el aula o profesor")
                    else:
                        print("Solamente se admiten valores alfabéticos")
                    Más_Operaciones=True
                
                #En el caso de que el usuario haya decidido ver la lista de eventos pendientes
                elif Opcion_Elegida=="2":
                    if len(Used_resources) != 0:
                        for Elemento in Used_resources:
                            print("ID de evento: " + str(Elemento[0]) + ", organizador: " + Elemento[1] + ", local: " + Elemento[2] + ", profesor: " + Elemento[3] + ", horario: " + Elemento[4][0].strftime("%H:%M") + ", capacidad reservada: " + str(Elemento[5]) + ", material: " + (Elemento[6] if len(Elemento) > 6 else "Ninguno"))

                    #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
                    Repetir=input("Desea realizar otra operación?: ")
                    if Repetir.lower() in ["sí", "si"]:
                        Más_Operaciones=True
                        print("")
                    elif Repetir.lower()=="no":
                        print("Vale, gracias por utilizar mi programa")
                        Contador=1
                        Más_Operaciones=False
                    else:
                        print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
                        Contador=1
                        Más_Operaciones=False
                
                #El usuario va a escribir el ID de su evento y en caso de que este evento esté registrado bajo el nombre del usuario va a poder hacerlo
                elif Opcion_Elegida=="3":
                    found=False
                    ID_Elegido=input("Introduzca el ID del evento que desea eliminar: ")
                    if verificar_tipo(ID_Elegido)=="int":
                        ID_Elegido=int(ID_Elegido)
                        for Elemento in Used_resources:    
                            if ID_Elegido==Elemento[0] and Nombre_Usuario==Elemento[1]:
                                if len(Elemento)>6 and Elemento[6]=="Proyector":
                                    Unused_Resources["Materiales"]["Proyector"]["Cantidad"]+=1
                                Used_resources.remove((Elemento))
                                Cantidad_eventos_profesor[Elemento[3]]-=1
                                print("Su evento ha sido eliminado exitosamente")
                                guardar_datos()
                                found=True
                                break
                        if not found:
                            print("No existe ningún evento creado por usted con ese ID")

                        #Aquí se le va a dar al usuario la opción de elegir si desea volver a ejecutar el programa
                        Repetir=input("Desea realizar otra operación?: ")
                        if Repetir.lower() in ["sí", "si"]:
                            Más_Operaciones=True
                        elif Repetir.lower()=="no":
                            print("Vale, gracias por utilizar mi programa")
                            Contador=1
                            Más_Operaciones=False
                        else:
                            print("No comprendo qué quiso decir con eso, pero vale, voy a asumir que no desea realizar más operaciones")
                            Contador=1
                            Más_Operaciones=False
                            
                    else:
                        print("Usted ha introducido un ID inválido")
                        Más_Operaciones=True
                else:
                    print("Usted ha elegido una opción inválida, por favor vuelva a intentarlo")
                    Más_Operaciones=True
        else:
            print("Lo sentimos, usted no posee una cuenta en nuestras bases de datos, por favor, vuelva a intentarlo.")
            Contador=0
    #Esta es la sección encargada de la creación de una cuenta de usuario. En caso de que el nombre de usuario no se encuentre registrado en el programa: se le permitirá crearse una cuenta y entrar al organizador. Además, aquí se va a chequear que el nombre de usuario tenga al menos un caracter y que su contraseña tenga entre 4 y 8 caracteres
    elif Bienvenida_Cuenta.lower() in ["no", "n"]:
        Desea_Crear=input("Desea crear una cuenta?: ")
        if Desea_Crear.lower() in ["yes", "y", "si", "sí", "s"]:
            Nombre_Usuario=input("Introduzca su nombre de usuario: ")
            Contraseña=input("Introduzca la contraseña (Debe tener cuatro o más caracteres): ")
            if len(Nombre_Usuario)>=1 and verificar_tipo(Nombre_Usuario)=="str" and len(Contraseña)>=4 and len(Contraseña)<=8:
                Cuenta_Existente=False
                if len(Control_de_Cuentas)>=1:
                    for Elemento in Control_de_Cuentas:
                        if Nombre_Usuario==Elemento[0]:
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


