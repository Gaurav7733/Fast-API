def individual_serial(book) -> dict:
    return {
        "id": str(book["_id"]),
        "name": book["name"],
        "img": book["img"],
        "summary": book["summary"]
    }

def list_serial(books) -> list:
    return[individual_serial(book) for book in books]