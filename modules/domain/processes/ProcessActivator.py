from aiogram.types import Message as M
from modules.domain.processes import *


class ProcessActivator:
    def __init__(self, msg: M | None = None):
        self.msg = msg

        # self.<command_1> = None
        # self.<command_2> = None
        # ...
        # self.<command_n> = None

    async def execute(self, item: str) -> bool:
        if self.msg is None: return False
        await self.__dict__[item](self.msg)
        return True

    def update(self, new: M):
        self.msg = new
