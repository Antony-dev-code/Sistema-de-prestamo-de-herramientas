from GestionJson import cargar,guardar,generar_id
from validaciones import validar_entero, validar_nombre_espacios
from GestionSolicitudes_Admin import ver_solicitudes

ARCHIVO= "G_usuarios.json"

def agregar_persona():
    G_usuarios=cargar(ARCHIVO)

    nombre=input('Ingrese el primer nombre del nuevo usuario: ')
    while validar_nombre_espacios(nombre)==False:
        nombre=input('Ingrese un nombre valido: ')

    apellido=input('Ingrese el apellido del nuevo usuario: ')
    while validar_nombre_espacios(apellido)==False:
        apellido=input('Ingrese un apellido valido: ')

    telefono=validar_entero('Ingrese el número de telefono del nuevo usuario: ')
    while telefono==None:
        telefono=validar_entero('Ingrese el numero de telefono sin puntos ni letras')


    direccion=input('Ingrese la dirección del nuevo usuario: ')
    while validar_nombre_espacios(direccion)==False:
        direccion=input('Ingrese una direccion valida: ')


    nuevo_usuario={
        "id": generar_id(G_usuarios),
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion
    }

    G_usuarios.append(nuevo_usuario)
    guardar(ARCHIVO,G_usuarios)
    print('Nuevo usuario añadido con exito')



def ver_usuarios():
    G_usuarios=cargar(ARCHIVO)

    if not G_usuarios:
        print('No hay usuarios registrados de momento')
        return
    
    for elemento in G_usuarios:
        print(f'ID: {elemento["id"]}             ->      Telefono: {elemento["telefono"]}')
        print(f'Nombre: {elemento["nombre"]}     ->      Apellido: {elemento["apellido"]}')
        print(f'Direccion: {elemento["direccion"]}')
    print()


def bucar_usuarios():
    G_usuarios=cargar(ARCHIVO)

    ver_usuarios()

    id_temporal=int(input('Igrese el ID a consultar: '))

    #Esperando lista de solicitudes para continuar

def actualizar_usuarios():
    G_usuarios=cargar(ARCHIVO)
    
    ver_usuarios()
    id_persona=validar_entero('Escoja y digite el ID a actualizar ')
    while(id_persona==None):
        id_persona=validar_entero('Error, ID no valido, escoja y digite el ID a actualizar ')
    
    for elemento in G_usuarios:
        if id_persona==elemento["id"]:

            nombre=input('Ingrese el primer nombre a actualizar del usuario: ')
            while validar_nombre_espacios(nombre)==False:
                nombre=input('Ingrese un nombre valido: ')
                elemento["nombre"]=nombre

            apellido=input('Ingrese el apellido a actualizar del usuario: ')
            while validar_nombre_espacios(apellido)==False:
                apellido=input('Ingrese un apellido valido: ')
                elemento["apellido"]=apellido

            telefono=validar_entero('Ingrese el número de telefono a actualizar del usuario: ')
            while telefono==None:
                telefono=validar_entero('Ingrese el numero de telefono a actualizar sin puntos ni letras')
                elemento["telefono"]=telefono


            direccion=input('Ingrese la dirección a actualizar del usuario: ')
            while validar_nombre_espacios(direccion)==False:
                direccion=input('Ingrese una direccion valida: ')
                elemento["direccion"]=direccion

            
            guardar(ARCHIVO, G_usuarios)
            print('Usuario actualizado con exito!')
            return
    print("El ID no existe. \n")



def eliminar_usuarios():
    contador=0
    G_usuarios=cargar(ARCHIVO)

    ver_usuarios()

    id_usuario=validar_entero("Escoja y digite el ID a eliminar: ")
    while(id_usuario==None):
        id_usuario=validar_entero("Error, Escoja y digite el id a eliminar: ")
        

    for elemento in G_usuarios:
        if id_usuario==elemento["id"]:
            G_usuarios.pop(contador)
            guardar(ARCHIVO, G_usuarios)
            print('Usuario eleminado con éxito!')
            return
        contador+=1

    print("El ID no existe. \n")

def validar_contraseña():
    contraseña_correcta=12345
    
    while True:
        contraseña_ingresada=validar_entero("Ingrese la contraseña: ")
        if contraseña_ingresada==contraseña_correcta:
            print("Acceso concedido")
            return True
        else:
            print("Contraseña incorrecta")
            return False


def validar_usuario():
    ARCHIVO="G_usuarios.json"
    G_usuarios=cargar(ARCHIVO)

    if not G_usuarios:
        print("No hay usuarios registrados.")
        return False

    while True:
        ver_usuarios()  
        id_ingresado = validar_entero("Ingrese el ID del usuario: ")
        for usuario in G_usuarios:
            if usuario["id"]==id_ingresado:
                print("Usuario confirmado")
                return usuario  
        print("ID no encontrado, intente nuevamente.\n")




