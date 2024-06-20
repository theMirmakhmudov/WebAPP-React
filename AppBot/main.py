import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config import TOKEN
from aiogram import Bot
from inline_buttons import button_web_app
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}</b>")
    await message.answer(f"<b>Open Web App</b>", reply_markup=button_web_app)


async def main() -> None:
    default_bot_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(TOKEN, default=default_bot_properties)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
