import asyncio
from aiogram import Bot, Dispatcher, types
from deep_translator import GoogleTranslator
from gtts import gTTS
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def translate(msg: types.Message):
    text = msg.text.strip()

    # Tilni aniqlash
    if any(ch in "äöüß" for ch in text.lower()):
        source = "de"
        target = "uz"
    else:
        source = "uz"
        target = "de"

    translated = GoogleTranslator(source=source, target=target).translate(text)

    await msg.answer(f"Tarjima:\n\n{translated}")

    # Agar tarjima nemischa bo‘lsa — ovoz chiqaramiz
    if target == "de":
        tts = gTTS(translated, lang="de")
        file = "tts/audio.mp3"
        tts.save(file)
        await msg.answer_voice(types.FSInputFile(file))


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
