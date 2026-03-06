from GestionJson import cargar,guardar,generar_id
from datetime import date, datetime, timedelta


ARCHIVO="G_herramientas.json"
ARCHIVO3="G_logs.json"
ARCHIVO5="G_Solcitudes"
def validar_menu(mensaje, minimo, maximo):
    try:
        opcion=int(input(mensaje))
        if opcion<minimo or opcion>maximo:
            return None
        else:
            return opcion
    except:
        return None
    

def validar_entero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validar_nombre_espacios(nombre):

    if nombre.strip()=="":
        print("Casilla vacia, por favor ingrese un nombre")
        return False
    return True

def validar_estado(estado):
    if estado.lower().strip()=='disponible' or estado.lower().strip()=='no disponible' or estado.lower().strip()=='en reparacion':
        return True
    return False



def validar_herramienta_existente(nombre_herramienta):
    ARCHIVO="G_herramientas.json"
    G_herramientas=cargar(ARCHIVO)
    for elemento in G_herramientas:
        if nombre_herramienta.lower().strip()==elemento["nombre_herramienta"].lower():
            return True
    return False

def validar_cantidad_herramientas(cantidadp,herramientaS):
    ARCHIVO="G_herramientas.json"
    ARCHIVO3="G_logs.json"
    falso_contador=0
    resta_herramientas=0
    dia_hora=str(datetime.now())
    G_logs=cargar(ARCHIVO3)
    G_herramientas=cargar(ARCHIVO)
    for elemento in G_herramientas:
            if elemento["nombre_herramienta"]==herramientaS:
                resta_herramientas=int(elemento["cantidad"])-cantidadp
                if resta_herramientas<0:
                    falso_contador+=1
                    reporte_existencias={

                        "Fecha": str(dia_hora),
                        "Nombre del usuario": "Jaime Jaimes",
                        "operacion realizada" "Solcitud de mas herramientas de las que habia en existencia"
                        "tipo_de_reporte": "Reporte por bajas existencias_EXAMEN",
                        "herramienta": elemento["nombre_herramienta"],
                        "Numero de reporte": falso_contador
                    }
                    G_logs.append(reporte_existencias)
                    guardar(ARCHIVO3,G_logs)
                    print('Se ha generado un reporte por bajas existencias y solicitud mayor al inventario actual')
                    elemento["cantidad"]=resta_herramientas
                    guardar(ARCHIVO,G_herramientas)

                    print ('Lo sentimos no hay suficientes unidades de esta herramienta intentelo nuevamente')
                    return False
                if resta_herramientas<4:
                    falso_contador+=1
                    reporte_bajas_existencias={

                        "Fecha": dia_hora,
                        "tipo_de_reporte": "Reporte por baja cantidad de herramientas",
                        "herramienta": elemento["nombre_herramienta"],
                        "cantidad": resta_herramientas,
                        "Numero de reporte": falso_contador
                    }
                    G_logs.append(reporte_bajas_existencias)
                    guardar(ARCHIVO3,G_logs)
                    print('Se ha generado un reporte por poca cantidad de herramientas')
                elemento["cantidad"]=resta_herramientas
                guardar(ARCHIVO,G_herramientas)

                print('La cantidad se ha corroborado y hay suficientes existencias para llevar a cabo el prestamo')
                return True
            
    print("Herramienta no encontrada")
    return False

