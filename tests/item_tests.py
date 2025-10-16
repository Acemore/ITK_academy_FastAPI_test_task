import requests

from app.models.item import ItemCreate, ItemUpdate
from tests import LOCAL_URL

item_id = None


def test_read_empty_items_list() -> None:
    empty_items_list_resp = requests.get(LOCAL_URL)

    assert empty_items_list_resp.status_code == 200
    assert empty_items_list_resp.json() == []


def test_create_item(item_data_to_create: ItemCreate) -> None:
    created_item_resp = requests.post(LOCAL_URL, json=item_data_to_create)
    created_item = created_item_resp.json()

    global item_id
    item_id = created_item['id']

    assert created_item_resp.status_code == 201
    assert created_item == {
        'id': item_id,
        **item_data_to_create,
    }


def test_read_items_list(item_data_to_create: ItemCreate) -> None:
    items_list_resp = requests.get(LOCAL_URL)

    assert items_list_resp.status_code == 200
    assert items_list_resp.json() == [
        {
            'id': item_id,
            **item_data_to_create,
        }
    ]


def test_read_items_list_with_skipping_item() -> None:
    items_list_resp = requests.get(f'{LOCAL_URL}?skip=1')

    assert items_list_resp.status_code == 200
    assert items_list_resp.json() == []


def test_read_items_list_with_limit() -> None:
    items_list_resp = requests.get(f'{LOCAL_URL}?limit=0')

    assert items_list_resp.status_code == 200
    assert items_list_resp.json() == []


def test_read_item(item_data_to_create: ItemCreate) -> None:
    item_resp = requests.get(f'{LOCAL_URL}/{item_id}')
    item = item_resp.json()

    assert item_resp.status_code == 200
    assert item == {
        'id': item_id,
        **item_data_to_create,
    }


def test_update_item(
    item_data_to_create: ItemCreate,
    item_data_to_update: ItemUpdate,
) -> None:
    old_item_resp = requests.get(f'{LOCAL_URL}/{item_id}')
    old_item = old_item_resp.json()

    assert old_item_resp.status_code == 200
    assert old_item == {'id': item_id, **item_data_to_create}

    updated_item_resp = requests.put(
        f'{LOCAL_URL}/{item_id}',
        json=item_data_to_update,
    )
    updated_item = updated_item_resp.json()

    assert updated_item_resp.status_code == 200
    assert updated_item == {'id': item_id, **item_data_to_update}


def test_update_item_not_found(item_data_to_update: ItemUpdate) -> None:
    resp = requests.put(f'{LOCAL_URL}/10', json=item_data_to_update)

    assert resp.status_code == 404
    assert resp.json() == {'detail': 'Item not found'}


def test_read_updated_item(item_data_to_update: ItemUpdate) -> None:
    updated_item_resp = requests.get(f'{LOCAL_URL}/{item_id}')
    updated_item = updated_item_resp.json()

    assert updated_item_resp.status_code == 200
    assert updated_item == {'id': item_id, **item_data_to_update}


def test_delete_item() -> None:
    resp = requests.delete(f'{LOCAL_URL}/{item_id}')

    assert resp.status_code == 200
    assert resp.json() == {"message": "Item deleted successfully"}


def test_read_items_list_after_deleting() -> None:
    items_list_resp = requests.get(LOCAL_URL)

    assert items_list_resp.status_code == 200
    assert items_list_resp.json() == []


def test_read_deleted_item() -> None:
    resp = requests.get(f'{LOCAL_URL}/{item_id}')

    assert resp.status_code == 404
    assert resp.json() == {'detail': 'Item not found'}
