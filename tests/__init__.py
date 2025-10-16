import os
import dotenv

dotenv.load_dotenv()

LOCAL_URL = os.getenv('LOCAL_URL')

PREFIX = './tests/fixtures'
ITEM_DATA_TO_CREATE_FILE_PATH = f'{PREFIX}/item_data_to_create.json'
ITEM_DATA_TO_UPDATE_FILE_PATH = f'{PREFIX}/item_data_to_update.json'
