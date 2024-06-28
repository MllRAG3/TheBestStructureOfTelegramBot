from modules.bot import D, Il
import asyncio


# Place for your handlers:)


async def main() -> None:
    await D.start_polling(Il)


if __name__ == "__main__":
    asyncio.run(main())
