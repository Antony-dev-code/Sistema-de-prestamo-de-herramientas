from GestionJson import cargar,guardar,generar_id
from validaciones import validar_entero, validar_nombre_espacios, validar_estado, validar_herramienta_existente, validar_cantidad_herramientas
from GestioHerramientas_Admin import ver_herramienta
from datetime import date,datetime,timedelta



ARCHIVO="G_herramientas.json"
ARCHIVO1= "G_solicitudes.json"

def agregar_solicitud():
    G_solicitudes=cargar(ARCHIVO1)

    nombre_solicitud=input('Ingrese el nombre de la persona que solicitará la herramienta: ')
    while validar_nombre_espacios(nombre_solicitud)==False:
        nombre_solicitud=input('Ingrese un nombre de persona valido: ')

    ver_herramienta()
    herramientaS=input('Ingrese la herramienta a solicitar: ')
    
    while validar_nombre_espacios(herramientaS)==False:
        herramientaS=input('Ingrese un nombre valido para la herramienta: ')
    while validar_herramienta_existente(herramientaS)==False:
        herramientaS=input('Ingrese un nombre de una herramienta existente: ')

    cantidadp=validar_entero('Ingrese el número de herramientas  a solicitar: ')
    while cantidadp==None:
        cantidadp=validar_entero('Ingrese el numero de herramientas sin puntos ni letras: ')

    while validar_cantidad_herramientas(cantidadp,herramientaS)==False:
        cantidadp=validar_entero('Ingrese un número de herramientas a solicitar existentes: ')
        while cantidadp==None:
            cantidadp=validar_entero('Ingrese el numero de herramientas sin puntos ni letras y que tenga existencia: ')
        cantidadp=validar_cantidad_herramientas(cantidadp,herramientaS)

#actualizar cantidades
    ARCHIVO3="G_logs.json"
    G_logs=cargar(ARCHIVO3)
    falso_contador=0
    falso_contador2=0
    fecha_inicio=date.today()
    print('La fecha de inicio del prestamo es ',fecha_inicio)
    dia_final=validar_entero('Ingrese el día de entrega: ')
    mes_final=validar_entero('ingrese el mes de entrega del prestamo: ')
    año_final=validar_entero('Ingrese el año de entrega de la herramienta: ')
    print('La fecha de entrega es',año_final,'/',mes_final,'/',dia_final,'/')
    fecha_final=date(año_final,mes_final,dia_final)
    resta_dias=(fecha_final-fecha_inicio).days
    if resta_dias<0:
            falso_contador+=1
            reporte_solicitud_vencida={
                        "tipo de reporte": "Reporte por solicitud vencida",
                        "nombre_solicitud": nombre_solicitud,
                        "herramienta": herramientaS,
                        "fecha_inicio": str(fecha_inicio),
                        "fecha_final": str(fecha_final),
                        "dias de vencido": resta_dias,
                        "Numero de reporte": falso_contador
                    }
            G_logs.append(reporte_solicitud_vencida)
            guardar(ARCHIVO3,G_logs)
            print('Se ha generado un reporte por solicitud vencida')
    


    opcion_observaciones=validar_entero('Desea reportar observaciones y/o novedades en la herramienta a solicitar? presione 1.SI  o   2.NO: ')
    while opcion_observaciones<1 or opcion_observaciones>2:
        opcion_observaciones=validar_entero('Unicos valores validos 1 y 2.  presione 1.SI  o   2.NO: ')
    if opcion_observaciones == 1:
        Observaciones=(input('Ingrese observaciones y/o novedades al recibir la herramienta: ' ))
        falso_contador2+=1
        reporte_observacion_solicitud={
                    "tipo de reporte": "observaciones en la herramienta recibida",
                    "nombre_solicitud": nombre_solicitud,
                    "herramienta": herramientaS,
                    "fecha_inicio": str(fecha_inicio),
                    "Observaciones": Observaciones,
                    "Numero de reporte": falso_contador2
                }
        G_logs.append(reporte_observacion_solicitud)
        guardar(ARCHIVO3,G_logs)
        print('Se ha generado un reporte por observaciones')


    nueva_solicitud={
        "id": generar_id(G_solicitudes),
        "nombre_solicitud": nombre_solicitud,
        "herramienta": herramientaS,
        "cantidad": cantidadp,
        "fecha_inicio": str(fecha_inicio),
        "fecha_entrega": str(fecha_final),
        "dias_restantes": str(resta_dias)
    }

    G_solicitudes.append(nueva_solicitud)
    guardar(ARCHIVO1,G_solicitudes)
    print('Nuevo solicitud realizada con exito de un buen uso a la herramienta')

    #Log
    ARCHIVO_LOGS = "G_logs2.json"
    G_logs=cargar(ARCHIVO_LOGS)

    nuevo_log={
    "accion": "Crear solicitud",
    "detalle": f"Se creo solicitud para la herramienta {herramientaS}"
    
    }

    G_logs.append(nuevo_log)
    guardar(ARCHIVO_LOGS, G_logs)





def bajo_stock():
    ver_reportes_bajas_existencias()
#necesito citar logs que coincidan con "tipo_de_reporte": "Reporte por bajas existencias"
#imprimirlos solo citando herramientas y cantidad 




def prestamos_on():
    ver_solicitudes()


def prestamos_off():
    ver_reportes_solicitudes_vencidas()
#citar logs que coincidan con "tipo de reporte": "Reporte por solicitud vencida" e imprimir todo




def historial_prestamos():
    ver_solicitudes()


def ver_solicitudes():
    G_solicitudes=cargar(ARCHIVO1)

    if not G_solicitudes:
        print("No hay solicitudes de momento \n")
        return
    
    for elemento in G_solicitudes:
        print(f'ID: {elemento["id"]} -> Nombre del solicitante: {elemento["nombre_solicitud"]}')
        print(f'Herramienta: {elemento["herramienta"]} -> Cantidad: {elemento["cantidad"]}')
        print(f'Fecha de inicio del prestamo: {elemento["fecha_inicio"]} -> Fecha de entrega {elemento["fecha_entrega"]}')
        print(f'Dias restantes hasta la entrega: {elemento["dias_restantes"]} \n')

def disponibilidad_herramientas_y_fechas():
    ver_solicitudes()
    #Log
    ARCHIVO_LOGS="G_logs2.json"
    G_logs=cargar(ARCHIVO_LOGS)

    nuevo_log={
        "accion": "Consulta de disponibilidad",
        "detalle": "El usuario consulto las herramientas disponibles"
    }

    G_logs.append(nuevo_log)
    guardar(ARCHIVO_LOGS, G_logs)


def top_herramientas():
    ver_herramienta()

def mi_funcion():
    from GestionUsuarios_Admin import ver_usuarios
    ver_usuarios()

def top_usuarios():
   mi_funcion()


def devolver_herramientas():
    ver_solicitudes()
    ARCHIVO3="G_logs.json"
    G_solicitudes=cargar(ARCHIVO1)
    G_herramientas=cargar(ARCHIVO)
    G_logs=cargar(ARCHIVO3)
    contador=0
    dia_hora=str(datetime.now())

    id_solicitud=validar_entero("Escoja el ID de su respectiva solicitud: ")
    while(id_solicitud==None):
        print ('Se ha generado un reporte por ID erroneo a la hora de entregar las herramientas')
        reporte_ID_erroneo_entrega={

                                "Fecha": str(dia_hora),
                                "Nombre del usuario": "Jaime Jaimes",
                                "operacion realizada" "Intento de devolucion no valido por ID erroneo"
                                "tipo_de_reporte": "Reporte por falso ID_EXAMEN",
                                "Numero de reporte": contador
                            }
        G_logs.append(reporte_ID_erroneo_entrega)
        guardar(ARCHIVO3,G_logs)
        print('Se ha generado un reporte por bajas existencias y solicitud mayor al inventario actual')

        id_solicitud=validar_entero("Error, Escoja el ID que respecte a una solicitud: ")
        
    for index, elemento in enumerate(G_solicitudes):
        
        if id_solicitud==elemento["id"]:

            cantidad_sumar=elemento["cantidad"]
            herramienta_devolver=elemento["herramienta"]

            
            for herramienta in G_herramientas:
                if herramienta["nombre_herramienta"] == herramienta_devolver:
                    herramienta["cantidad"] += cantidad_sumar
                    break

            G_solicitudes.pop(index)
            guardar(ARCHIVO, G_herramientas)
            guardar(ARCHIVO1, G_solicitudes)
            print('Herramienta entregada!')
            
            return

    print("No existen solicitudes. \n")
    print ('Se ha generado un reporte por ID erroneo a la hora de entregar las herramientas')
    reporte_ID_erroneo_entrega={

                            "Fecha": str(dia_hora),
                            "Nombre del usuario": "Jaime Jaimes",
                            "operacion realizada" "Intento de devolucion no valido por ID erroneo"
                            "tipo_de_reporte": "Reporte por falso ID_EXAMEN",
                            "Numero de reporte": contador
                        }
    G_logs.append(reporte_ID_erroneo_entrega)
    guardar(ARCHIVO3,G_logs)
    print('Se ha generado un reporte por bajas existencias y solicitud mayor al inventario actual')

    id_solicitud=validar_entero("Error, Escoja el ID que respecte a una solicitud: ")

    #Logs entrega herramientas no prestadas






    #Log

    ARCHIVO_LOGS="G_logs2.json"
    G_logs=cargar(ARCHIVO_LOGS)

    nuevo_log={
        "accion": "Devolver herramienta",
        "detalle": f"Se devolvio la herramienta {herramienta_devolver}"

    }

    G_logs.append(nuevo_log)
    guardar(ARCHIVO_LOGS, G_logs)




def ver_logs():
    ARCHIVO_LOGS="G_logs2.json"
    G_logs=cargar(ARCHIVO_LOGS)

    if not G_logs:
        print("No hay logs registrados.\n")
        return

    print(" LISTA DE LOGS \n")

    for log in G_logs:
        print("Acción:", log["accion"])
        print("Detalle:", log["detalle"])
        print("\n")



def ver_reportes_bajas_existencias():
    ARCHIVO_LOGS="G_logs.json"
    G_logs1=cargar(ARCHIVO_LOGS)

    if not G_logs1:
        print("No hay reportes registrados.\n")
        return

    print(" REPORTES POR BAJAS EXISTENCIAS \n")

    for reporte in G_logs1:
        if reporte.get("tipo_de_reporte")=="Reporte por bajas existencias":
            print("Herramienta:", reporte["herramienta"])
            print("Cantidad restante:", reporte["cantidad"])
            print("Número de reporte:", reporte["Numero de reporte"])
            print("FIN DEL REPORTE")


def ver_reportes_solicitudes_vencidas():
    ARCHIVO_LOGS="G_logs.json"
    G_logs1=cargar(ARCHIVO_LOGS)
    if not G_logs1:
        print("No hay reportes registrados.\n")
        return
    print(" REPORTES POR SOLICITUD VENCIDA \n")

    for reporte in G_logs1:
        if reporte.get("tipo de reporte") == "Reporte por solicitud vencida":
            print("Nombre:", reporte["nombre_solicitud"])
            print("Herramienta:", reporte["herramienta"])
            print("Fecha inicio:", reporte["fecha_inicio"])
            print("Fecha final:", reporte["fecha_final"])
            print("Días vencido:", reporte["dias de vencido"])
            print("Número de reporte:", reporte["Numero de reporte"])
            print("FIN DEL REPORTE")


print('Implementada la nueva función que permite ordenar personas por su color de piel')