from GestionJson import cargar,guardar,generar_id
from validaciones import validar_entero, validar_nombre_espacios, validar_estado

ARCHIVO= "G_herramientas.json"

def agregar_herramienta():
    G_herramientas=cargar(ARCHIVO)

    nombre_herramienta=input('Ingrese el nombre de la herramienta: ')
    while validar_nombre_espacios(nombre_herramienta)==False:
        nombre_herramienta=input('Ingrese un nombre de herramienta valido: ')

    categoria=input('Ingrese la categoria de la herramienta: ')
    while validar_nombre_espacios(categoria)==False:
        categoria=input('Ingrese un nombre valido para la categoria de la herramienta: ')

    cantidad=validar_entero('Ingrese el número de herramientas totales: ')
    while cantidad==None:
        cantidad=validar_entero('Ingrese el numero de herramientas sin puntos ni letras: ')

    precio_unitario=validar_entero('Ingrese el precio individual de la herramienta: ')
    while precio_unitario==None:
        precio_unitario=validar_entero('Ingrese el precio individual de la herramienta sin puntos ni letras: ')


    estado_h=input('Ingrese el estado de la herramienta, sea disponible, no disponible o en reparación: ')
    while validar_nombre_espacios(estado_h)==False:
        estado_h=input('Ingrese el un estado para la herramienta válido, sea disponible, no disponible o en reparación: ')
    while validar_estado(estado_h)==False:
        estado_h=input('Ingrese el un estado para la herramienta válido, sea disponible, no disponible o en reparación: ')
    print('Estado de la herramienta añadido con exito')


    nueva_herramienta={
        "id": generar_id(G_herramientas),
        "nombre_herramienta": nombre_herramienta,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "estado_h": estado_h
    }

    G_herramientas.append(nueva_herramienta)
    guardar(ARCHIVO,G_herramientas)
    print('Nuevo herramienta añadida con exito')



def ver_herramienta():
    G_herramienta=cargar(ARCHIVO)
    if not G_herramienta:
        print('No hay ninguna herramienta registrada de momento')
        return
    
    for elemento in G_herramienta:
        print(f'ID: {elemento["id"]}                                     ->      cantidad: {elemento["cantidad"]}')
        print('')
        print(f'nombre_herramienta: {elemento["nombre_herramienta"]}               ->      categoria: {elemento["categoria"]}')
        print('')
        print(f'estado_h: {elemento["estado_h"]}                      ->      precio_unitario: {elemento["precio_unitario"]}')
        print('')
        print('')
    print()
    print('')


def bucar_herramienta():
    G_herramienta=cargar(ARCHIVO)

    ver_herramienta()

    id_temporal=int(input('Igrese el ID de la a consultar: '))

    #Esperando lista de solicitudes para continuar


def actualizar_herramienta():
    G_herramientas=cargar(ARCHIVO)
    
    ver_herramienta()
    id_herramienta=validar_entero('Escoja y digite el ID de la herramienta a actualizar: ')
    while(id_herramienta==None):
        id_herramienta=validar_entero('Error, ID no valido, escoja y digite el ID a actualizar: ')
    
    for elemento in G_herramientas:
        if id_herramienta==elemento["id"]:

            nombre_herramienta=input('Ingrese el  nombre a actualizar de la herramienta: ')
            while validar_nombre_espacios(nombre_herramienta)==False:
                nombre_herramienta=input('Ingrese un nombre valido: ')
                elemento["nombre_herramienta"]=nombre_herramienta

            categoria=input('Ingrese la categoria a actualizar de la herramienta: ')
            while validar_nombre_espacios(categoria)==False:
                categoria=input('Ingrese un apellido valido: ')
                elemento["categoria"]=categoria

            cantidad=validar_entero('Ingrese la nueva cantidad de herramientas: ')
            while cantidad==None:
                cantidad=validar_entero('Ingrese el numero de herramientas a actualizar sin puntos ni numeros')
                elemento["cantidad"]=cantidad


            estado_h=input('Ingrese el nuevo estado de la herramienta: ')
            while validar_nombre_espacios(estado_h)==False:
                estado_h=input('Ingrese un estado en el campo, no valen espacios: ')
            while validar_estado(estado_h)==False:
                    estado_h=input('Ingrese el un estado para la herramienta válido, sea disponible, no disponible o en reparación: ')
            elemento["estado_h"]=estado_h

            
            guardar(ARCHIVO, G_herramientas)
            print('Herramienta actualizada con exito!')
            return
    print("El ID no existe. \n")



def eliminar_herramienta():
    contador=0
    G_herramientas=cargar(ARCHIVO)

    ver_herramienta()

    id_herramienta=validar_entero("Escoja y digite el ID a eliminar: ")
    while(id_herramienta==None):
        id_herramienta=validar_entero("Error, Escoja y digite el id a eliminar: ")
        

    for elemento in G_herramientas:
        if id_herramienta==elemento["id"]:
            G_herramientas.pop(contador)
            guardar(ARCHIVO, G_herramientas)
            print('Herramienta eleminada con éxito!')
            return
        contador+=1
        
    print("El ID no existe. \n")


print('Coregido el bug que impedía la correcta devolución de herramientas')

