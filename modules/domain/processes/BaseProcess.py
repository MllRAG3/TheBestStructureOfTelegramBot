from aiogram.types import Message as M, InlineKeyboardButton as IKBtn, InlineKeyboardMarkup as IKMkp, InputFile
import time


class DataEvent:
    type: str = ""
    pars: dict[str, str | InputFile | list[list[IKBtn]] | IKMkp] = {}

    @staticmethod
    async def code(message: M, *args, **kwargs):
        raise NotImplementedError

    def __iadd__(self, row: list[IKBtn]):
        try:
            if isinstance(self.pars["reply_markup"], IKMkp): raise KeyError
            self.pars["reply_markup"] += row
        except KeyError:
            pass

        return self

    @property
    def for_send(self):
        data = self.pars
        try:
            data["reply_markup"] = IKMkp(inline_keyboard=data["reply_markup"])
        except KeyError:
            pass
        return {'type': self.type, **data}


class BaseProcess:
    """Базовый процесс"""
    events: dict[int, DataEvent] = {
        #  Your events
    }

    def __getitem__(self, item: int):
        try:
            return self.events[item]
        except KeyError:
            return None

    async def __call__(self, msg: M, sleep_time=0.2):
        keys = self.events.keys()
        for i in range(min(keys), max(keys)):
            if self[i] is None: continue
            await self[i].code(msg)
            await self.answer(message=msg, **self[i].for_send)
            time.sleep(sleep_time)

    async def answer(self, message, type: str, **kwargs):
        match type:
            case "reply":
                await message.reply(**kwargs)
            case "photo":
                await message.reply_photo(**kwargs)
            case "document":
                await message.reply_document(**kwargs)
            case "edit_media":
                try:
                    await message.edit_reply_markup(reply_markup=kwargs["reply_markup"])
                    del kwargs["reply_markup"]
                except KeyError:
                    pass
                await message.edit_media(**kwargs)
            case "edit_text":
                try:
                    await message.edit_reply_markup(reply_markup=kwargs["reply_markup"])
                    del kwargs["reply_markup"]
                except KeyError:
                    pass
                await message.edit_text(**kwargs)
            case _ as t:
                raise NotImplementedError(f"type {t} unsupported yet.")
