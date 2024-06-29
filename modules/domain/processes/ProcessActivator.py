from aiogram.types import Message as M
from modules.errors.MessageIsInvalid import MessageIsInvalid


class ProcessActivator:
    def __init__(self, message=None):
        self.MESSAGE: M | None = message

        # self.<command_1> = None
        # self.<command_2> = None
        # ...
        # self.<command_n> = None

    def __getattribute__(self, item: str):
        if self.MESSAGE is None: raise MessageIsInvalid
        self.__dict__[item](self.MESSAGE)

    @classmethod
    def update(cls, new: M):
        return cls(new)
