from modules.processes.BaseProcess import BaseHandler
from pyrogram import handlers, filters, types


class StartHandler(BaseHandler):
    __name__ = "Обработчик команды /start"
    HANDLER = handlers.MessageHandler
    FILTER = filters.command("start")

    async def func(self, _, message: types.Message):
        await message.reply(f"Hello, <b>{message.from_user.first_name.title()}</b>!")
