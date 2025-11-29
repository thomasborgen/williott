from typing import Annotated
from fastapi import Query


def get_characters(characters: Annotated[list[str], Query()]) -> list[str]:
    all_chars = []
    [all_chars.extend(chars.split(",")) for chars in characters]
    return all_chars
