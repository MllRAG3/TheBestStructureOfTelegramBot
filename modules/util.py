from modules.database.models import models
from modules.database import db

import re


def create_tables() -> None:
    """Database models to tables"""
    if not models:
        print("No database models created.")
        return
    with db:
        db.create_tables(models)
    print(f"created models: {', '.join(map(lambda x: x.__name__, models))}")


def is_command(text: str) -> bool:
    if text is None: return False
    return text.startswith('/')


def extract_arguments(text: str) -> str or None:
    regexp = re.compile(r"/\w*(@\w*)*\s*([\s\S]*)", re.IGNORECASE)
    result = regexp.match(text)
    return result.group(2) if is_command(text) else None
