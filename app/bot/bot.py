from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup
from httpx import AsyncClient
from config import settings


bot = Bot(token=settings.TG_TOKEN)


dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add('Начать сбор')


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer('Чтобы начать, нажмите кнопку "Начать сбор"', reply_markup=menu)

@dp.message_handler()
async def pik_parser(message: types.Message):
    if message.text == 'Начать сбор':
        async with AsyncClient() as client:
            response = await client.get("http://pik-api:8000/pik/get_data")
            
            for item in response.json().get("data")["items"]:
                    await bot.send_message(message.chat.id, f"""Площадь {item.get('area')}\nЭтаж {item.get('floor')}\nЦена {item.get('price')} руб.\n{item.get('bulkName')}\nВсего этажей {item.get('maxFloor')}\nДата сдачи: {item.get('settlementDate')}\nhttps://www.pik.ru/flat/{item.get('id')}?benefitId=114415""")
 

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)