
def create_json_product_info():
    _id = int(input("Id de producto: "))
    pcode = input("Código de producto: ")
    name = input("Nombre de producto: ")
    price = float(input("Precio: "))
    in_stock = int(input("Unidades disponibles: "))
    category = input("Categoría: ")


    product_info = {
        "_id" : _id,
        "pcode": pcode,
        "name" : name,
        "price": price,
        "in_stock": in_stock,
        "category": category
    }
    return product_info

def create_json_update():
    print("Menu de opciones")
    print("1. Modificar todos los datos del producto")
    print("2. Modificar un elemento del producto")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        pcode = input("Código de producto: ")
        name = input("Nombre de producto: ")
        price = float(input("Precio: "))
        in_stock = int(input("Unidades disponibles: "))
        category = input("Categoría: ")

        product_info = {
            "pcode": pcode,
            "name": name,
            "price": price,
            "in_stock": in_stock,
            "category": category
        }
        return product_info

    elif opcion == "2":
        indice = input("Ingrese el dato a modificar, ejemplo pcode")
        valor = input("Ingrese el valor a modificar")
        product_info = {indice: valor}
        return product_info
    else:
        print("Dato ingresado no valido")


