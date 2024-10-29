print("========================================================")
print("========== $ TIENDA VIRTUAL SOLO VERDE $ ===============")
print("========================================================\n")

producto = {}

def agregar_producto( ):
    nombre = input("nombre del producto: ")
    ID = input("ID del producto: ")
    contenido = input(f"contenido del producto es: ")
    fecha_inicio = (input("fecha de fabricacion : "))
    fecha_vencimiento = (input("fecha de vencimiento: "))
    dic_producto = {"nombre":nombre, "ID de registro":ID, "contenido":contenido, "fecha de inicio":fecha_inicio, "fecha de vencimiento":fecha_vencimiento}
    producto[ID] = dic_producto
    print("¡el prodcuto ha sido agregado! ")

def buscar_producto( ):
    id_producto = input("ingrese el ID del producto: \n")
    if id_producto in producto:
        print("Producto encontrado:")
        print(producto[id_producto]) 
    else:
        print("Producto no encontrado.")
    
def modificar_producto( ):
    id_producto = input("Ingrese el ID del producto a modificar: ")
    if id_producto in producto:
        print("Producto encontrado. Ingrese los nuevos datos (deje vacío si no desea cambiar):")
        nombre = input("Nuevo nombre del producto: ") or producto[id_producto]["nombre"]
        contenido = input("Nuevo contenido del producto: ") or producto[id_producto]["contenido"]
        fecha_inicio = input("Nueva fecha de fabricación: ") or producto[id_producto]["fecha de inicio"]
        fecha_vencimiento = input("Nueva fecha de vencimiento: ") or producto[id_producto]["fecha de vencimiento"]

        producto[id_producto].update({
            "nombre": nombre,
            "contenido": contenido,
            "fecha de inicio": fecha_inicio,
            "fecha de vencimiento": fecha_vencimiento})
        print("¡El producto ha sido modificado!")
    else:
        print("Producto no encontrado.")

def eliminar_producto( ):
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    if id_producto in producto:
        del producto[id_producto]
        print("¡El producto ha sido eliminado!")
    else:
        print("Producto no encontrado.")


while True:
    print("\n|| MENU PRINCIPAL ||: \n")
    opciones = int(input ("\n 1. AGREGAR PRODUCTO \n 2. BUSCAR PRODUCTO \n 3. MODIFICAR PRODUCTO \n 4. ELIMINAR PRODUCTO \n 5. SALIR \ningrese la opcion deseada: "))
    if opciones < 1 or opciones > 5:
        print("opcion invalida , ingrese nuevamente ")
    
    elif opciones == 1:
        while True:
            print("\n|| MENU DE REGISTRO ||\n")
            menu_agregar = int(input("\n 1.AÑADIR PRODUCTO \n 2.VOLVER \n"))
            if menu_agregar < 1 or menu_agregar > 2:
                print("opcio invalida, intente nuevamente")
            elif menu_agregar == 1:
                print("ingrese los siguentes datos:\n ")
                agregar_producto()
            else:
                print("Has vuelto al menú principal.")
                break
            
    elif opciones == 2:
        while True:
            print("\n|| MENU DE BUSQUEDA ||\n")
            buscador = int(input("\n 1. BUSCAR PRODUCTO\n 2. VOLVER \n"))
            if buscador < 1 or buscador > 2:
                print("opcio invalida, intente nuevamente")
            elif buscador == 1:
                buscar_producto() 
            else:
                print("Has vuelto al menú principal.")
                break
    
    elif opciones == 3:
            while True:
                print("\n|| MENU DE MODIFICACION ||\n")
                buscador = int(input("\n 1. MODIFICAR PRODUCTO\n 2. VOLVER \n"))
                if buscador < 1 or buscador > 2:
                    print("opcio invalida, intente nuevamente")
                elif buscador == 1:
                    modificar_producto() 
                else:
                    print("Has vuelto al menú principal.")
                    break
    
    elif opciones == 4:
            while True:
                print("\n|| MENU DE ELIMINACION ||\n")
                buscador = int(input("\n 1. ELIMINAR PRODUCTO\n 2. VOLVER \n"))
                if buscador < 1 or buscador > 2:
                    print("opcio invalida, intente nuevamente")
                elif buscador == 1:
                    eliminar_producto() 
                else:
                    print("Has vuelto al menú principal.")
                    break
    
    else:
        print("has finalizado , !hasta luego¡ ")
        break

        
















