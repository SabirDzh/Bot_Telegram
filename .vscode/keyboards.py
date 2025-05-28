from aiogram.utils.keyboard import (InlineKeyboardBuilder, ReplyKeyboardBuilder, KeyboardBuilder)

async def start_inline_keyboard():
	builder = InlineKeyboardBuilder()
	builder.button(text="Продать userName", callback_data="sell_user_name")
	builder.button(text="Купить userName", callback_data="buy_user_name")
	return builder.adjust(2).as_markup()
