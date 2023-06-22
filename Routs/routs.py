from fastapi import APIRouter
from models.books import Book
from config.database import collection_name
from Schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

#Get Request Method
@router.get("/")
async def get_books():
    books = list_serial(collection_name.find())
    return books

#Post Request Method
@router.post("/")
async def post_book(book: Book):
    collection_name.insert_one(dict(book))

#put Request Method
@router.put("/{id}")
async def put_book(id: str, book: Book):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(book)})

#Delete Request Method
@router.delete("/{id}")
async def delete_book(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})