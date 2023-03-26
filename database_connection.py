import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["parcial1_sis"]
collection = db["product_info"]

#print(collection)