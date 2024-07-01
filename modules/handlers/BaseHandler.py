from pyrogram.filters import Filter
from pyrogram.handlers.handler import Handler


class BaseHandler:
    __name__ = "Базовый обработчик"
    HANDLER: Handler = Handler
    FILTER: Filter | None = None

    def __call__(self, *args, **kwargs):
        pass

    @property
    def pyrogram_handler(self):
        return self.HANDLER(self, self.FILTER)
