from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

main_kb=[
    [KeyboardButton(text='🔊 Tiflo Kitoblar'),KeyboardButton(text='🖥 Video Darslar')],
  
  

]

reply_main_kb=ReplyKeyboardMarkup(keyboard=main_kb,resize_keyboard=True)

literature_kb=[
    [KeyboardButton(text='📜 Badiiy Adabiyotlar')],
    [KeyboardButton(text='📒 Ilmiy Ommabop Adabiyotlar')],
        [KeyboardButton(text='⬅️ Ortga')],

]

reply_literature_kb=ReplyKeyboardMarkup(keyboard=literature_kb,resize_keyboard=True)

choose_video_kb=[
    [KeyboardButton(text='🎥 Fan video-maruzalari')],
    [KeyboardButton(text='📽 Ilmiy-ommabop roliklar')],
    [KeyboardButton(text='⬅️ Ortga')],

]

reply_choose_video_kb=ReplyKeyboardMarkup(keyboard=choose_video_kb,resize_keyboard=True)


choose_international_economics_kb=[
    [KeyboardButton(text='📈 Xalqaro iqtisodiyot')],
    [KeyboardButton(text='⬅️ Ortga')],
]


reply_choose_international_economics=ReplyKeyboardMarkup(keyboard=choose_international_economics_kb,resize_keyboard=True)


##################INLINE BUTTONS##################
enclusive_videos_inkb=[
    [InlineKeyboardButton(text='1',callback_data='1'),InlineKeyboardButton(text='2',callback_data='2'),InlineKeyboardButton(text='3',callback_data='3'),InlineKeyboardButton(text='4',callback_data='4')],
    [InlineKeyboardButton(text='🏠 Asosiy',callback_data="🏠 Asosiy")],
]


reply_enclusive_videos_inkb=InlineKeyboardMarkup(inline_keyboard=enclusive_videos_inkb)

scientific_inkb=[
    [InlineKeyboardButton(text='1',callback_data='1a'),InlineKeyboardButton(text='2',callback_data='2a'),InlineKeyboardButton(text='3',callback_data='3a'),InlineKeyboardButton(text='4',callback_data='4a'),
     InlineKeyboardButton(text='5',callback_data='5a')],[InlineKeyboardButton(text='6',callback_data='6a'),InlineKeyboardButton(text='7',callback_data='7a'),InlineKeyboardButton(text='8',callback_data='8a'),
 InlineKeyboardButton(text='9',callback_data='9a'),InlineKeyboardButton(text='10',callback_data='10a')],
  [InlineKeyboardButton(text='11',callback_data='11a'),InlineKeyboardButton(text='12',callback_data='12a'),
     InlineKeyboardButton(text='13',callback_data='13a'),InlineKeyboardButton(text='14',callback_data='14a'),InlineKeyboardButton(text='15',callback_data='15a')],[InlineKeyboardButton(text='16',callback_data='16a'),
     InlineKeyboardButton(text='17',callback_data='17a'),InlineKeyboardButton(text='18',callback_data='18a'),InlineKeyboardButton(text='19',callback_data='19a'),InlineKeyboardButton(text='20',callback_data='20a')],
    [InlineKeyboardButton(text='🏠 Asosiy',callback_data="🏠 Asosiy")],
]

reply_scientific_inkb=InlineKeyboardMarkup(inline_keyboard=scientific_inkb)
