from aiogram import *
import asyncio
import asyncpg
from aiogram.fsm.state import *
from aiogram.fsm.context import *
from keyboards import start_inline_keyboard
from database.models import *
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import *
from aiogram.types import *

router = Router()
dp = Dispatcher()

HELP_COMMAND = '''
<b>/start</b> - <em>запустить бота</em>
<b>/help</b> - <em>список доступных команд</em>
'''

# ! инициализация таблицы
# async def init_db(pool: asyncpg.Pool):
# 	async with pool.acquire() as conn:
# 		await conn.execute(CREATE_TABLE)

@router.message(Command("start"))
async def start_cmd(message: Message):
	await message.answer(f"Здравствуйте, это бот для продажи <i>@UserName</i>\n\n⬇️ Выберите одну из команд ниже ⬇️", reply_markup= await start_inline_keyboard(), parse_mode="HTML")

@router.message(Command("help"))
async def help_cmd(message: Message):
	await message.answer(text=HELP_COMMAND, parse_mode="HTML")

