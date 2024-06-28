from aiogram import Bot
from os import environ
from typing import Final
from dotenv import load_dotenv

load_dotenv()

Il: Final[Bot] = Bot(token=environ["API_TOKEN"])
