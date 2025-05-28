import asyncio
from aiogram import Bot, Dispatcher
import logging 
from config import TOKEN_API
import asyncpg
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router

bot = Bot(TOKEN_API)
dp = Dispatcher()

async def main():
	dp.include_router(router)
	
	try: 
		await bot.delete_webhook(drop_pending_updates=True)
		await dp.start_polling(bot)
	finally:
		await bot.session.close()

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("Exit")