"""Run this file to start bot"""
from modules.bot import D, Il
from util import create_tables
import asyncio


# Place for your handlers:)


async def main() -> None:
    """starts bot"""
    create_tables()
    await D.start_polling(Il)


if __name__ == "__main__":
    asyncio.run(main())
