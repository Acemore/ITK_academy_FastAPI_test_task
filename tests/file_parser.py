import json
from typing import Any


def get_file_content(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def parse_json(file_content: str) -> Any:
    return json.loads(file_content)
