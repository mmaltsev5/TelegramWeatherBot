from aiogram import Bot, Dispatcher, executor, types
import python_weather

# bot init
bot = Bot(token="5324281341:AAFqCLCplv9UTUvApsdCIFvH9Qb3FZZGLTQ")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")


# echo
@dp.message_handler()
async def echo(message: types.message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = "Введите город"

    resp_msg = weather.location_name + "\n"
    resp_msg += f"{celsius}° - текущая температура. \n"
    resp_msg += f"Состояние погоды: {weather.current.sky_text}"

    if celsius <= 15:
        resp_msg += "\n\n Прохладно! Одевайтесь теплее."
    else:
        resp_msg += "\n\n На улице тепло. Одевайтесь полегче."

    await message.answer(resp_msg)


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)