from aiogram import types
from modules.domain.processes import active_processes


class ProcessActivator:
    def __init__(self, message: types.Message):
        self.message: types.Message = message

    def __getattribute__(self, item):
        return active_processes[item](self.message)
