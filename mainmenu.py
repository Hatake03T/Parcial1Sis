#Main menu phyton file

#importar desde crud
from crud import *
from functions import *
op =0

#menu started
while op!= 5:
    print("SV GROCERIES")
    print("**********************")
    print("1. Consultar productos")
    print("2. Consultar un producto en específico")
    print("3. Ingresar nuevo producto")
    print("4. Actualizar información de producto")
    print("5. Eliminar registro de producto")
    print("6. Salir")
    op = input("¿Qué desea hacer? ")
    print("**********************")
    #Consultar
    if op == "1":
            print("Menu de consulta")
            print("1. Ver todo los productos")
            print("2. Buscar por categoría")
            opcion = input("Qué desea hacer? ")
            print("**********************")
            if opcion == "1":
                read_product_info()
            elif opcion == "2":
                category = input("Ingrese Categoría: ")
                read_product_info(category)
    elif op == "2":
                name = input("Ingrese nombre de producto: ")
                read_product_info_producto(name)
    #Insertar
    elif op == "3":
        product_info = create_json_product_info()
        create_product_info(product_info)
    #Actualizar
    elif op == "4":
        id = int(input("Ingres el ID del producto a modificar: "))
        product_info = create_json_update()
        update_product_info(id, product_info)
    #Eliminar
    elif op == "5":
        id = int(input("Ingres el ID del producto a eliminar: "))
        delete_product_info(id)
        read_product_info()

    elif op == "6":
        print("Saliendo de programa. Bye")
        break





