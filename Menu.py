from validaciones import validar_menu
from GestionUsuarios_Admin import validar_contraseña, validar_usuario, agregar_persona, ver_usuarios, bucar_usuarios, actualizar_usuarios, eliminar_usuarios
from GestioHerramientas_Admin import agregar_herramienta, ver_herramienta, bucar_herramienta, actualizar_herramienta, eliminar_herramienta
from GestionSolicitudes_Admin import agregar_solicitud,bajo_stock, prestamos_on, prestamos_off, historial_prestamos, top_herramientas, top_usuarios,disponibilidad_herramientas_y_fechas,devolver_herramientas, ver_logs


#Menu general

def menu1():
    while True:
        op1=validar_menu('''
                            Bienvenido al prestamo de herramientas local
                            Escoja el tipo de usuario que vaya a ingresar al sistema
                            (Recuerde que si no está registrador
                            debe pedir a un administrador que lo registre)
                        
                        1.Administrador

                        2.Usuario

                        3.Salir


                        ''',1,3)
        while op1==None:
            op1=validar_menu('Error, opcion no valida en el menu. Vuelva a seleccionar una opción: ',1,3)
        match op1:
            case 1:
                #PONER CLAVE AL ADMIN
                print('recordar que la contraseña del admin es 12345')
                validar_contraseña()
                menu2()
            case 2:
                #Listar usuarios y pedir ID del usuario para poder entrar
                validar_usuario()
                menu3()
            case 3:
                print('Gracias por usar el sistema de herramientas comunal')

        if op1==3:
            break


#Menu's admin
 
def menu2():
    while True:
        op2=validar_menu('''
                            Bienvenido señor administrador,
                            ¿Qué desea hacer el día de hoy?
                         
                         1.Gestionar usuarios (Agregar usuarios, ver usuarios, buscar usuarios,
                                                actualizar usuarios y eliminar usuarios)

                         2.Gestionar herramientas (Agregar herramientas, ver herramientas, 
                                                    buscar herramientas, actualizar herramientas y 
                                                    eliminar herramientas)

                         3.Consultar solicitudes, datos y reportes

                         4.Salir de la interfaz de administrador

                        ''',1,4)
        while op2==None:
            op2=validar_menu('Error, opcion no valida en el menu. Vuelva a seleccionar una opción: ',1,4)
        match op2:
            case 1:
                menu2_1()
            case 2:
                menu2_2()
            case 3:
                menu2_3()
            case 4:
                print('Feliz día administrador, vuelva pronto')

        if op2==4:
            break

#Menu gestionar usuarios

def menu2_1():
    while True:
        op3=validar_menu('''
                            Bienvenido señor administrador,
                            
                         
                         1.Agregar usuarios

                         2.Ver usuarios

                         3.Buscar usuarios

                         4.Actualizar usuarios

                         5.Eliminar usuarios

                         6.Salir de la interfaz de administrador

                        ''',1,6)
        while op3==None:
            op3=validar_menu('Error, opcion no valida en el menu. Vuelva a seleccionar una opción: ',1,6)
        match op3:
            case 1:
                agregar_persona()
            case 2:
                ver_usuarios()
            case 3:
                bucar_usuarios()
            case 4:
                actualizar_usuarios()
            case 5:
                eliminar_usuarios()
            case 6:
                print('Feliz día administrador, vuelva pronto')

        if op3==6:
            break
    
#Menu gestionar herramientas

def menu2_2():
    while True:
        op4=validar_menu('''
                            Bienvenido señor administrador,
                            
                         
                         1.Agregar Herramientas

                         2.Ver Herramientas

                         3.Buscar Herramientas

                         4.Actualizar Herramientas

                         5.Eliminar Herramientas

                         6.Salir de la interfaz de administrador

                        ''',1,6)
        while op4==None:
            op4=validar_menu('Error, opcion no valida en el menu. Vuelva a seleccionar una opción: ',1,6)
        match op4:
            case 1:
                agregar_herramienta()
            case 2:
                ver_herramienta()
            case 3:
                bucar_herramienta()
            case 4:
                actualizar_herramienta()
            case 5:
                eliminar_herramienta()

            case 6:
                print('Feliz día administrador, vuelva pronto')

        if op4==6:
            break

#Menu Solicitudes y gestión de prestamo de herramientas

def menu2_3():
    while True:
        op5=validar_menu('''
                            Bienvenido señor administrador,
                            aquí encontrará todos los datos sobre:
                            
                         1.Herramientas con bajo stock

                         2.Lista de prestamos activos

                         3.Lista de prestamos vencidos

                         4.Consultar historial de prestamos de un usuario

                         5.Listado de herramientas más utilizadas

                         6.Usuarios que más herramientas han solicitado

                         7.Reportes/Logs

                         8.Salir de la interfaz de administrador

                        ''',1,8)
        while op5==None:
            op5=validar_menu('Error, opcion no valida en el menu. Vuelva a seleccionar una opción: ',1,7)
        match op5:
            case 1:
                bajo_stock()
            case 2:
                prestamos_on()
            case 3:
               prestamos_off()
            case 4:
                historial_prestamos()
            case 5:
                top_herramientas()
            case 6:
                top_usuarios()
            case 7:
                #pendiente poner reportes log
                ver_logs()

                print("")
            case 8:
                print('Feliz día administrador, vuelva pronto')
        if op5==7:
            break

#Hasta aquí el menu del admin

#Menu de usuario 

def menu3():
    while True:
        op6=validar_menu('''
                            Bienvenido usuario,
                            ¿Qué desea hacer el día de hoy?
                         
                         1.Disponibilidad de las herramientas y fechas de entrega 

                         2.Crear solicitud de prestamo de herramienta 

                         3.Devolver herramientas

                         4.Salir menu usuarios

                        ''',1,4)
        while op6==None:
            op6=validar_menu('Error, opcion no valida en el menu. Vuelva a seleccionar una opción: ',1,4)
        match op6:
            case 1:
                disponibilidad_herramientas_y_fechas()
            case 2:
                agregar_solicitud()
            case 3:
                devolver_herramientas()
            case 4:
                print('Feliz día usuario, vuelva pronto')

        if op6==4:
            break

