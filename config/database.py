from pymongo import MongoClient
client = MongoClient("mongodb+srv://Gaurav33:Gaurav99@cluster0.ajisikx.mongodb.net/?retryWrites=true&w=majority")

db = client.book_db

collection_name = db["books"]