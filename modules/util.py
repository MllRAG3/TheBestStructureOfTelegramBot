from modules.database.models import models
from modules.database import db


def create_tables() -> None:
    if not models: return
    with db:
        db.create_tables([*models])
    print(f"created models: {', '.join(models)}")
