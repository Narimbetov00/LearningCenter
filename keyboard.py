from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton
#user
inlinemarkup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📝Oqiw ushin registratsiya📝",callback_data="1")
    ],
    [
        InlineKeyboardButton(text="📚Sabaqlar haqqinda mag'liwmat📚",callback_data="3")
    ],
    [
        InlineKeyboardButton(text="👩‍💻🧑‍💻Mentorlar Haqqinda🧑‍💻👩‍💻",callback_data="5")
    ],
    [
        InlineKeyboardButton(text="🗳Usinis kiritiw🗳",callback_data="2")
    ],
    [
        InlineKeyboardButton(text="📌Biz haqimizda📌",callback_data="6")
    ],
])
sabaqliqlar = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🌟Scratch",callback_data="scratch")
    ],
    [
        InlineKeyboardButton(text="🌟Python Basic",callback_data="pythonBasic")
    ],
    [
        InlineKeyboardButton(text="🌟Python Development",callback_data="pythonDev")
    ],
    [
        InlineKeyboardButton(text="🌟Telegram Bot ",callback_data="teleBot")
    ],
    [
        InlineKeyboardButton(text="🌟Android Development",callback_data="androidDev")
    ],
        [
        InlineKeyboardButton(text="🌟Front-end",callback_data="frontEnd")
    ],
    [
        InlineKeyboardButton(text="🌟Back-End",callback_data="backEnd")
    ],
    [
        InlineKeyboardButton(text="🌟Kompyuter sawatxanlıǵı",callback_data="kompyuter")
    ],
    [
        InlineKeyboardButton(text="🌟Photoshop ",callback_data="photoshop")
    ],
    [
        InlineKeyboardButton(text="🌟Corel Draw",callback_data="corelDraw")
    ],
            [
        InlineKeyboardButton(text="🌟AutoCad 3DS MAX",callback_data="autocad")
    ],
    [
        InlineKeyboardButton(text="🌟Mobilografiya",callback_data="mobiloGr")
    ],
    [
        InlineKeyboardButton(text="🌟Rus tili",callback_data="rustil")
    ],
    [
        InlineKeyboardButton(text="🌟Media jurnalistika ",callback_data="media")
    ],
    [
        InlineKeyboardButton(text="🔙Artqa qaytiw🔙",callback_data="quit")
    ],
])
mentorsbtn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Python Development Mentor",callback_data="pyDevMentor")
    ],
    [
        InlineKeyboardButton(text="Corel draw Mentor",callback_data="coreldrawmentor")
    ],
    [
        InlineKeyboardButton(text="AutoCad 3DSMAX Mentori",callback_data="autoaadmentori")
    ],
    [
        InlineKeyboardButton(text="Photoshop Mentor",callback_data="photoshopmentor")
    ],
    # [
    #     InlineKeyboardButton(text="Android Development",callback_data="androidMentor")
    # ],
    # [
    #     InlineKeyboardButton(text="Front-end",callback_data="frontEndMentor")
    # ],
    # [
    #     InlineKeyboardButton(text="Back-End",callback_data="backEndMentor")
    # ],
        [
        InlineKeyboardButton(text="Kompyuter sawatxanlıǵı ",callback_data="komMentor")
    ],
        [
        InlineKeyboardButton(text="🔙Artqa qaytiw🔙",callback_data="quit")
    ],

])

feedback = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅Álbette✅",callback_data="albette"),
        InlineKeyboardButton(text="❌Házir Emes❌",callback_data="haziremes")
    ]
])
saylan = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Ayapov Aydos")
    ],
        [
        KeyboardButton(text="Emluratova Feruza")
    ],
        [
        KeyboardButton(text="Bazarbaev Begdiyar")
    ],
        [
        KeyboardButton(text="Abdikerimov Rasul")
    ],
        [
        KeyboardButton(text="Baltabaev Uluǵbek")
    ],
        [
        KeyboardButton(text="Ramatullaev Ruslan")
    ],
        [
        KeyboardButton(text="Bektemirov Asadbek")
    ],
        [
        KeyboardButton(text="Bukenova Asemay")
    ],
        [
        KeyboardButton(text="Nawrızbaev Aydos")
    ],
        [
        KeyboardButton(text="Erlepesova Maxida")
    ]
],resize_keyboard=True,one_time_keyboard=True)
ball =  ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="1 ball😔"),
        KeyboardButton(text="2 ball☹️"),
        KeyboardButton(text="3 ball🙁"),
        KeyboardButton(text="4 ball😕"),
        KeyboardButton(text="5 ball👍🏻")   
    ],
    [
        KeyboardButton(text="6 ball☺️"),
        KeyboardButton(text="7 ball😊"),
        KeyboardButton(text="8 ball😇"),
        KeyboardButton(text="9 ball🤩"),
        KeyboardButton(text="10 ball🥳")   
    ]
],resize_keyboard=True,one_time_keyboard=True)
sbprinsp = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🤩Awa🤩")
    ],
    [
        KeyboardButton(text="🙂Ortasha🙂")
    ],
    [
        KeyboardButton(text="😔Yaq😔")
    ]
],resize_keyboard=True,one_time_keyboard=True)
takrarlaw = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🤩Toliq jaratilgan🤩")
    ],
    [
        KeyboardButton(text="🙂Toliq emes🙂")
    ],
    [
        KeyboardButton(text="😔Jaratilmagan😔")
    ]
],resize_keyboard=True,one_time_keyboard=True)
adwork = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🤩Unaydi🤩")
    ],
    [
        KeyboardButton(text="🙂Ortasha🙂")
    ],
    [
        KeyboardButton(text="💭Pikir qaldiriw💭")
    ]
],resize_keyboard=True,one_time_keyboard=True)
qosimsha = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🤩Awa🤩")
    ],
    [
        KeyboardButton(text="😉Yaq😉")
    ]
],resize_keyboard=True,one_time_keyboard=True)

yesorno = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="✅Duris✅"),
        KeyboardButton(text="❌Qa'te❌")
    ]
],resize_keyboard=True,one_time_keyboard=True)
#admin
admininlinemark = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📝Taza arzalar📝",callback_data="7")
    ],
    [
        InlineKeyboardButton(text="📝Usinislar📝",callback_data="8")
    ],
    # [
    #     InlineKeyboardButton(text="🔑Gilt sozdi ozgertiw🔑",callback_data="12")
    # ],
    [
        InlineKeyboardButton(text="🧑‍💻Taza admin kiritiw👩‍💻",callback_data="9")
    ],
    [
        InlineKeyboardButton(text="📢Reklama jiberiw📢",callback_data="10")
    ],
    [
        InlineKeyboardButton(text="🗑Adminlerdi o'shiriw🗑",callback_data="11")
    ],

])
#reklama
sendreklama = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎥Videoli Mag'liwmat🎥",callback_data="video")
    ],
    [
        InlineKeyboardButton(text="🖼Suwretli Mag'liwmat🖼",callback_data="suwret")
    ],
    [
        InlineKeyboardButton(text="🔙Artqa qaytiw🔙",callback_data="quit2")
    ],
])

artqa = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔑Gilt sozdi o'zgertiw🔑",callback_data="ozgert")
    ],
    [
        InlineKeyboardButton(text="🔙Artqa qaytiw🔙",callback_data="quit3")
    ]
])