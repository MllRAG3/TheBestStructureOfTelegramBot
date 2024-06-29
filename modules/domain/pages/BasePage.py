from aiogram.types import Message, InlineKeyboardButton as IKBtn, InlineKeyboardMarkup as IKMkp
from typing import Any


class GeneratedPage:
    def __init__(
            self,
            data: Any,
            additional: dict,
            keyboard: list[list[IKBtn]],
            message: Message,
            type: str,
    ) -> None:
        self.type: str = type
        self.message: Message = message
        self.keyboard: list[list[IKBtn]] = keyboard
        self.additional: dict = additional
        self.data: Any = data

    def __iadd__(self, other: list[list[IKBtn]]):
        self.keyboard += other
        return self

    async def __call__(self):
        match self.type:
            case "reply":
                await self.message.reply(
                    self.data,
                    reply_markup=IKMkp(inline_keyboard=self.keyboard),
                    **self.additional
                )
            case "photo":
                await self.message.reply_photo(
                    self.data,
                    reply_markup=IKMkp(inline_keyboard=self.keyboard),
                    **self.additional
                )
            case "document":
                await self.message.reply_document(
                    self.data,
                    reply_markup=IKMkp(inline_keyboard=self.keyboard),
                    **self.additional
                )
            case "edit_media":
                await self.message.edit_media(self.data, **self.additional)
                await self.message.edit_reply_markup(reply_markup=IKMkp(inline_keyboard=self.keyboard))
            case "edit_text":
                await self.message.edit_text(self.data, **self.additional)
                await self.message.edit_reply_markup(reply_markup=IKMkp(inline_keyboard=self.keyboard))
            case _ as t:
                raise NotImplementedError(f"type {t} unsupported.")


class BasePage:
    """Базовая страница"""
    DATA: Any = ""
    KEYBOARD: list[list[IKBtn]] = []
    ADDITIONAL_PARS: dict = {}

    async def render(self, msg: Message, *args, **kwargs) -> GeneratedPage:
        """Загрузка страницы"""
        # some code
        # return generated page!
        raise NotImplementedError
