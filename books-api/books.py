from fastapi import FastAPI
from enum import Enum
app = FastAPI()

BOOKS = {
  'book_1': {'title': 'Title One', 'author': 'Author One'},
  'book_2': {'title': 'Title Two', 'author': 'Author Two'},
  'book_3': {'title': 'Title Three', 'author': 'Author Three'},
  'book_4': {'title': 'Title Four', 'author': 'Author Four'},
  'book_5': {'title': 'Title Five', 'author': 'Author Five'}
}

class DirectionName(str, Enum):
  north = "North"
  east = "East"
  south = "South"
  west = "West"
  
@app.get("/")
async def get_all_books():
  return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: int):
  return {"book_title": book_id}

@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
  if direction_name == DirectionName.north:
    return {"Direction": direction_name, 'orientation': 'Up'}
  if direction_name == DirectionName.east:
    return {"Direction": direction_name, 'orientation': 'Right'}
  if direction_name == DirectionName.south:
    return {"Direction": direction_name, 'orientation': 'Down'}
  return {"Direction": direction_name, 'orientation': 'Left'}
  