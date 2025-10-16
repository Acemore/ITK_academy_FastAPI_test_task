import pytest

from app.models.item import ItemCreate, ItemUpdate
from tests import ITEM_DATA_TO_CREATE_FILE_PATH, ITEM_DATA_TO_UPDATE_FILE_PATH
from tests.file_parser import get_file_content, parse_json


@pytest.fixture(scope='package')
def item_data_to_create() -> ItemCreate:
    return parse_json(get_file_content(ITEM_DATA_TO_CREATE_FILE_PATH))


@pytest.fixture(scope='package')
def item_data_to_update() -> ItemUpdate:
    return parse_json(get_file_content(ITEM_DATA_TO_UPDATE_FILE_PATH))
