from aiogram.types import Message as M
from modules.domain.pages.BasePage import BasePage


class BaseProcess:
    __name__ = "base process"
    page_array: dict[int, BasePage] = {}

    def __getitem__(self, item: int):
        try:
            return self.page_array[item]
        except KeyError:
            return None

    def __setitem__(self, key: int, value: BasePage):
        self.page_array[key] = value

    async def __call__(self, message: M):
        for i in range(min(self.page_array.keys()), max(self.page_array.keys()) + 1):
            if self.page_array[i] is None: continue
            page = await self.page_array[i].render(message)
            await page()
