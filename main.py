from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8095973158:AAFdkCrqjQ7jrul1nzC2qmC3Z2HVZR061ms"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Kino bot ishladi 🎬")

executor.start_polling(dp)