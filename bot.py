import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import StateFilter
import os 
from dotenv import load_dotenv
from aiogram import F,Router
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import default_state
from aiogram.utils.formatting import Bold, Text,Url
from aiogram.enums.parse_mode import ParseMode
from state import Tiflo,Video
from buttons import reply_main_kb,reply_choose_video_kb,reply_literature_kb,\
                    reply_choose_international_economics,reply_enclusive_videos_inkb,reply_scientific_inkb



load_dotenv()

logging.basicConfig(level=logging.INFO)
router=Router()

videos=["https://youtube.com/shorts/LaZ_-qMcBBU?si=yi4VJhGDQU-nJ9Xy","https://youtube.com/shorts/zzA4VhDzAyI?si=MfMbsTzsd7nKHgGX","https://youtube.com/shorts/0AVKWrXAm6A?si=enh-oC8lj4kE5eB0","https://youtube.com/shorts/_A_4MdkqB2o?si=E2vkFq63C3eXdAGN"]
# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text="Xush kelibsiz, ilmsevar, o'zingizni qiziqtirgan ma'lumotlarni olishga sizda imkon bor, hozir!",reply_markup=reply_main_kb)



    # await message.answer(text="Xush kelibsiz, ilimsevar, o'zingizni qiziqtirgan ma'lumotlarni olishga sizda imkon bor, hozir!",reply_markup=reply_main_kb)

@router.message(F.text.lower() == "🏠 asosiy")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Xush kelibsiz, ilmsevar, o'zingizni qiziqtirgan ma'lumotlarni olishga sizda imkon bor, hozir!",reply_markup=reply_main_kb)

@router.message(F.text.lower()=="🔊 tiflo kitoblar")
async def choose_literature_books(message:types.Message,state:FSMContext):
    await message.answer('Biz sizga turli xildagi adabiyotlarni taklif qilmoqdamiz, istaganingizni tanlang!',reply_markup=reply_literature_kb)
    await state.set_state(Tiflo.choose_literature_type)

@router.message(Tiflo.choose_literature_type)
async def choose_literature(message:types.Message,state:FSMContext):

    if message.text.lower()=="📜 badiiy adabiyotlar":
        await message.answer("Hozirda bu qism ma'lumotlari to'ldirilmoqda")

    elif message.text.lower()=="📒 ilmiy ommabop adabiyotlar":
            link_text='-- Havola --'
            message_text = f"<b>Audio Kitob: Iqtisodiyot osmonida yulduzga aylanganlar</b>\n\
        1.Kirish.<a href='https://www.youtube.com/watch?v=07lfGxMukGI&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=1&pp=iAQB'>{link_text}</a>\n\
        2.Vasiliy Vasilovich Leontev <a href='https://www.youtube.com/watch?v=lxIcEUXW3ec&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=2&pp=iAQB'>{link_text}</a>\n\
        3.Pol Entoni Samuelson  <a href='https://www.youtube.com/watch?v=57gwxnYP33Q&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=3&pp=iAQB'>{link_text}</a>\n\
        4.Milton Fridman (1 qism) <a href='https://www.youtube.com/watch?v=n3LrC1vC8FY&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=4&pp=iAQB'>{link_text}</a>\n\
        5.Milton Fridman (2 qism) <a href='https://www.youtube.com/watch?v=FXcuJYrwrQQ&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=5&pp=iAQB'>{link_text}</a>\n\
        6.Jeyms Tobin <a href='https://www.youtube.com/watch?v=LsUzKVjLxZI&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=6&pp=iAQB'>{link_text}</a>\n\
        7.Robert Shiller <a href='https://www.youtube.com/watch?v=-vzUkBtKmJQ&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=7&pp=iAQB'>{link_text}</a>\n\
        8.Kichik Robert Lukas  <a href='https://www.youtube.com/watch?v=T1PlyCkLemE&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=8&pp=iAQB'>{link_text}</a>\n\
        9.Robert Jon Auman (1 qism) <a href='https://www.youtube.com/watch?v=UPRMRTffWtU&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=9&pp=iAQB'>{link_text}</a>\n\
        10.Robert Jon Auman (2 qism)<a href='https://www.youtube.com/watch?v=fCi_UU_1els&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=10&pp=iAQB'>{link_text}</a>\n\
        11.Tomas Jon Serjant <a href='https://www.youtube.com/watch?v=T0BB-JEZ7ec&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=11&pp=iAQB'>{link_text}</a>\n\
        12.Kirstofer Albert Sims <a href='https://www.youtube.com/watch?v=a4AFj-c0lCs&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=12&pp=iAQB'>{link_text}</a>\n\
        13.Pol Volker (1 qism) <a href='https://www.youtube.com/watch?v=57gwxnYP33Q&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=3&pp=iAQB'>{link_text}</a>\n\
        14.Pol Volker (2 qism) <a href='https://www.youtube.com/watch?v=dn4NByOmJzM&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=14&pp=iAQB'>{link_text}</a>\n\
        15.Stenli Fisher(1 qism)<a href='https://www.youtube.com/watch?v=96mdG7Fp4XI&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=15&pp=iAQB'>{link_text}</a>\n\
        16.Stenli Fisher(2 qism) <a href='https://www.youtube.com/watch?v=rHRBc8uHEbw&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=16&pp=iAQB'>{link_text}</a>\n\
        17.Devid Kass(1 qism) <a href='https://www.youtube.com/watch?v=-_Zkyuz4aDc&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=17&pp=iAQB'>{link_text}</a>\n\
        18.Devid Kass (2 qism) <a href='https://www.youtube.com/watch?v=tqUuZDJiwPE&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=18&pp=iAQB'>{link_text}</a>\n\
        19.Jek Drez (1 qism) <a href='https://www.youtube.com/watch?v=fon08HBBNv8&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=19&pp=iAQB'>{link_text}</a>\n\
        20.Jek Drez (2 qism) <a href='https://www.youtube.com/watch?v=DLg4qNw8Iww&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=20&pp=iAQB'>{link_text}</a>" 


            await message.answer(message_text,reply_markup=reply_scientific_inkb, parse_mode=ParseMode.HTML)

    elif message.text.lower()=="⬅️ ortga":
        await state.clear()
        await cmd_start(message)

@router.message(F.text.lower()=="🖥 video darslar")
async def choose_literature_books(message:types.Message,state:FSMContext):
    await message.answer('Biz sizga turli xildagi videolarni taklif qilmoqdamiz, istaganingizni tanlang!',reply_markup=reply_choose_video_kb)
    await state.set_state(Video.choose_video_type)

# @router.message(Video.choose_video_type,F.text.lower()=="🎥 fan video-maruzalari")
# async def choose_video_type(message:types.Message,state:FSMContext):
   
#     await state.clear()
#     await message.answer("Siz quyidagi video maruza va roliklarimizni tomosha qilishingiz mumkin.",reply_markup=reply_main_kb)
#     for video in videos:
#         await message.answer(video)

@router.message(Video.choose_video_type)
async def choose_video_type(message:types.Message,state:FSMContext):
    if message.text.lower()=="📽 ilmiy-ommabop roliklar":
        
        await state.set_state(Video.choose_economics)

        await message.answer("Siz quyidagi yo'nalishlardagi video roliklarimizni tomosha qilishingiz mumkin.",reply_markup=reply_choose_international_economics)

    elif message.text.lower()=="🎥 fan video-maruzalari":
        await state.set_state(Video.choose_video_type)
        await message.answer("Siz quyidagi video maruza va roliklarimizni tomosha qilishingiz mumkin.",reply_markup=reply_choose_video_kb)
        for video in videos:
            await message.answer(video)

    elif message.text.lower()=='⬅️ ortga':

        await state.clear()
       
        await cmd_start(message)




@router.message(Video.choose_economics)
async def choose_international_economic(message:types.Message,state:FSMContext):
  
    if message.text.lower()=="📈 xalqaro iqtisodiyot":
             
        # content = Text("Inklusiv video darslar\n",Bold("1."), "Xalqaro xizmatlar bozori\n","Havola: ",Url("https://youtu.be/W5tqBwEB_Ok?si=4hOP13oWgn78ac84"))
        link_text = "-- Havola --"
        message_text = f"<b>Inklusiv video darslar</b>\n 1.Xalqaro xizmatlar bozori.\n\
            Maruzachi:<b>Qobiljon Isayev</b> <a href='https://youtu.be/W5tqBwEB_Ok?si=4hOP13oWgn78ac84'>{link_text}</a>\n 2.Xalqaro iqtisodiy munosabatlar.\n \
            Maruzachi:<b>Qobiljon Isayev</b> <a href='https://youtu.be/_8YcOQW91Ug?si=O9x4ILlrqKtY4nKi'>{link_text}</a>\n 3.Oltin valyuta zaxiralari.\n\
            Maruzachi:<b>Qobiljon Isayev</b> <a href='https://youtu.be/9Qintfi_w2s?si=9vSe4LmYSQcoF9q-'>{link_text}</a>\n 4.Xalqaro valyuta munosabatlari.\n \
            Maruzachi:<b>Qobiljon Isayev</b> <a href='https://youtu.be/j6gsWOTzLzs?si=Mz_eejPssZTvNnOr'>{link_text}</a>"

        await message.answer( text=message_text,
            reply_markup=reply_enclusive_videos_inkb,
            parse_mode=ParseMode.HTML,disable_web_page_preview=True)
        
    elif message.text.lower()=='⬅️ ortga':

        await state.clear()
       
        await choose_literature_books(message,state)

    
@router.callback_query(F.data == "1a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=07lfGxMukGI&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=1&pp=iAQB")

@router.callback_query(F.data == "2a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=lxIcEUXW3ec&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=2&pp=iAQB")
@router.callback_query(F.data == "3a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=57gwxnYP33Q&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=3&pp=iAQB")
@router.callback_query(F.data == "4a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=n3LrC1vC8FY&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=4&pp=iAQB")

@router.callback_query(F.data == "5a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=FXcuJYrwrQQ&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=5&pp=iAQB")

@router.callback_query(F.data == "6a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=LsUzKVjLxZI&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=6&pp=iAQB")
@router.callback_query(F.data == "7a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=-vzUkBtKmJQ&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=7&pp=iAQB")
@router.callback_query(F.data == "8a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=T1PlyCkLemE&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=8&pp=iAQB")

@router.callback_query(F.data == "9a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=UPRMRTffWtU&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=9&pp=iAQB")

@router.callback_query(F.data == "10a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=fCi_UU_1els&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=10&pp=iAQB")
@router.callback_query(F.data == "11a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=T0BB-JEZ7ec&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=11&pp=iAQB")
@router.callback_query(F.data == "12a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=a4AFj-c0lCs&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=12&pp=iAQB")

@router.callback_query(F.data == "13a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://youtu.be/W5tqBwEB_Ok?si=4hOP13oWgn78ac84")

@router.callback_query(F.data == "14a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=dn4NByOmJzM&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=14&pp=iAQB")
@router.callback_query(F.data == "15a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=96mdG7Fp4XI&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=15&pp=iAQB")
@router.callback_query(F.data == "16a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=rHRBc8uHEbw&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=16&pp=iAQB")

@router.callback_query(F.data == "17a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=-_Zkyuz4aDc&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=17&pp=iAQB")

@router.callback_query(F.data == "18a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=tqUuZDJiwPE&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=18&pp=iAQB")
@router.callback_query(F.data == "19a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=fon08HBBNv8&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=19&pp=iAQB")
@router.callback_query(F.data == "20a")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://www.youtube.com/watch?v=DLg4qNw8Iww&list=PLWnln1h-GrAgM-01kCqhr8cwXDVkam9XX&index=20&pp=iAQB")
@router.callback_query(F.data.lower() == "🏠 asosiy")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text="Xush kelibsiz, ilmsevar, o'zingizni qiziqtirgan ma'lumotlarni olishga sizda imkon bor, hozir!",reply_markup=reply_main_kb)
     

@router.callback_query(F.data == "1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://youtu.be/W5tqBwEB_Ok?si=4hOP13oWgn78ac84")

@router.callback_query(F.data == "2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://youtu.be/_8YcOQW91Ug?si=O9x4ILlrqKtY4nKi")
@router.callback_query(F.data == "3")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://youtu.be/9Qintfi_w2s?si=9vSe4LmYSQcoF9q-")
@router.callback_query(F.data == "4")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer( text="https://youtu.be/j6gsWOTzLzs?si=Mz_eejPssZTvNnOr")
@router.callback_query(F.data.lower() == "🏠 asosiy")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text="Xush kelibsiz, ilmsevar, o'zingizni qiziqtirgan ma'lumotlarni olishga sizda imkon bor, hozir!",reply_markup=reply_main_kb)

@router.message(F.media)
async def handle_group_video(message: types.Message):
    video_file_id = message.video.file_id
    print('thiss ---------------------')
    # Now you have the file ID of the video
    print(f"Video File ID: {video_file_id}")



# Запуск процесса поллинга новых апдейтов
async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
   

if __name__ == "__main__":
    asyncio.run(main())