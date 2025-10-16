from fastapi import FastAPI, HTTPException
from typing import Dict, List

from app.models.item import Item, ItemCreate, ItemUpdate

app: FastAPI = FastAPI()
items_db: Dict[int, Item] = {}


@app.post('/items', response_model=Item, status_code=201)
def create_item(item: ItemCreate) -> Item:
    item_id = len(items_db) + 1
    item_with_id = Item(id=item_id, **item.model_dump())
    items_db[item_id] = item_with_id
    return item_with_id


@app.get('/items', response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10) -> List[Item]:
    items = list(items_db.values())
    return items[skip:skip + limit]


@app.get('/items/{item_id}', response_model=Item)
def read_item(item_id: int) -> Item:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail='Item not found')

    return items_db[item_id]


@app.put('/items/{item_id}', response_model=Item)
def update_item(item_id: int, item: ItemUpdate) -> Item:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail='Item not found')

    item_with_id = Item(id=item_id, **item.model_dump())
    items_db[item_id] = item_with_id
    return item_with_id


@app.delete('/items/{item_id}')
def delete_item(item_id: int) -> Dict[str, str]:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail='Item not found')

    del items_db[item_id]
    return {"message": "Item deleted successfully"}
