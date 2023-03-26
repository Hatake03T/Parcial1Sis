from database_connection import  collection
import  json

#definicion de lectura de datos
def read_product_info(category=None):
    if category is not None:
        query = {"category": category}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)

def read_product_info_producto(name:None):
    if name is not None:
        query = {"name": name}
        document = collection.find_one(query)
        print(document)
    else:
        print("Producto no existe")

#Creacion de documento
def create_product_info(json_product_info):
    result = collection.insert_one(json_product_info)
    print(result.inserted_id)


#Actualizacion de producto/document
def update_product_info(id, json_product_info_update):
    query = {"_id": id}
    new_values = {"$set": json_product_info_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)


#Eliminar un documento
def delete_product_info(id=None):
        query = {"_id": id}
        document = collection.delete_many(query)


