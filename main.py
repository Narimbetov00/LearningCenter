from aiogram import Bot,Dispatcher,types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import BotCommand
from keyboard import inlinemarkup,feedback,saylan,ball,sbprinsp,takrarlaw,adwork,qosimsha,admininlinemark,sabaqliqlar,mentorsbtn,sendreklama,artqa,yesorno
from data import add_datas,user_add_datas,arzalar_add_datas,add_feedback,get_admin_data,get_admin_us_data,get_users_id,get_users_id_name,get_users_Arza,get_users_feedback,delete_admin
import time


bot = Bot(open('config.txt','r').read())
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

class Admins(StatesGroup):
    chat_id = State()
    name = State()
    number = State()
    deleteAdmin = State()
class newArza(StatesGroup):
    name = State()
    phone = State()
    magliwmat = State()
class usinislar(StatesGroup):
    
    sayla = State()
    sistmball = State()
    sbprins = State()
    tarrar = State()
    adw = State()
    txt = State()
class Reklamavidio(StatesGroup):
    reklameVideo = State() 
    reklamaPhoto = State()

#                                                   COMMANDS 

#               START COMMAND     
@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    adminID = get_admin_data()
    getUser = get_users_id_name()
    if user_id in adminID:
        await message.answer(text=f"Assalawma áleykim {message.from_user.full_name}",reply_markup=admininlinemark)
    else:
        await message.answer(text=f"Assalawma áleykim {message.from_user.full_name}\nTEXNOPOST IT ACADEMY botina xosh keldińiz\nSiz bul bot arqali TexnoPOS kompaniyası jańalıqlarınan xabardar bolıp barasız.\nMánzilimiz : Ğáresizlik kóshesi 80/4.\nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.\nTelegram kanalimiz: https://t.me/texnopos",reply_markup=inlinemarkup)
        if user_id not in getUser :
            user_add_datas(user_id,user_name)
    await bot.set_my_commands(commands=[
        BotCommand(command="/start",description="Botti iske túsiriw"),
        BotCommand(command="/stop",description="Jazilip atrģan arzani toqtatiw"),
        BotCommand(command="/help",description="Járdem")
    ])

#               STOP COMMAND

@dp.message_handler(commands=['stop'],state=newArza)
async def stop_command(msg:types.Message,state:FSMContext):
    this_state = await state.get_state()
    if this_state == None:
        print(this_state)
        await msg.answer("Biykar qiliw ushin arza tabilmadi!")    
    else:
        await state.finish()
        await msg.answer("Jazip atrgan arza toqtatildi!")                    

#               HELP COMMAND

@dp.message_handler(commands=['help'])
async def help_command(msg:types.Message):
    await msg.answer(f"""Siz botdan qalay paydalaniw kerek
            /start    -    Botti qayta ju'kleydi
            /stop     -    Jazip atrg'an arzani biykar etiw
            /help     -    Ja'rdem
                     """)

#               CALLBACK 
@dp.callback_query_handler()
async def start_to_registrate(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    if data == "1":
        await bot.send_message(chat_id=call.from_user.id,text="TEXNOPOST IT ACADEMYsinda oqiw ushin ARZA jiberip atırsiz‼️\nBizge Atinizdi jiberin.")
        await newArza.name.set()
    if data == "2":
        await bot.send_message(chat_id=call.from_user.id,text="Dawam etiwge tayinsizba?",reply_markup=feedback)   
    if data == 'albette':
        await bot.send_message(chat_id=call.from_user.id,text="Mentorinizdi saylań",reply_markup=saylan)
        await usinislar.sayla.set() 
    if data == 'haziremes':
        await bot.send_message(chat_id=call.from_user.id,text="Waqtińiz bolģanda usinisinizdi bildiriń.Biz sizdiń usinisinizdi albette kórip shiģamiz ",reply_markup=inlinemarkup)
    if data == "3":       
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,
                                            reply_markup=sabaqliqlar)      
    if data == "5":       
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,
                                            reply_markup=mentorsbtn) 
    if data == "6":
        await bot.send_message(chat_id=call.from_user.id,text="TEXNOPOS IT ACADEMY 2020 - jili fevral ayinda tiykar salindi.\nEń dáslep Kotlin && Android kurslari menen óz jumisin basladi;\n2020 - jili 20-fevral Kotlin kursi baslandi,12 student;\n2020 - jili 21-fevral Android kursi baslandi,15 student;\nTEXNOPOS IT MEKTEBI TIYKARSHILARI:\nKalabaev Sharapat ha'm Embergenov Álibek\n2020-jil 20-oktyabrde TexnoPOS IT Mektebi brand ati menen rásmiy mámleket diziminen ótkerildi.Kamandaniń 3 aģzasi bar edi.TexnoPOS IT Mektebi házirgi waqitta 15 ge jaqin ha'r tu'rli salada bilim úlesip kelmekte.")     
    if data == "7":
        arza = get_users_Arza()
        await bot.send_message(chat_id=call.from_user.id,text=arza)     
    if data == "8":
        feedback1 = get_users_feedback()
        await bot.send_message(chat_id=call.from_user.id,text=feedback1)   
    if data == '9':
        await bot.send_message(chat_id=call.from_user.id, text="Taza admin qosiw bólimi.\nQosilatuģin adminniń ID nomerin jiberiń!..")
        await Admins.chat_id.set()
    if data == '10':
        await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                            message_id=call.message.message_id,
                                            reply_markup=sendreklama)
    if data == "11":    
        await bot.send_message(chat_id=call.from_user.id, text="Óshiriw kerek bolģan adminniń Telegram id nomerin kiritiń.")
        await Admins.deleteAdmin.set()
    if data== "pyDevMentor":
        await bot.send_message(chat_id=call.from_user.id,text="""Maģliwmat 2024-jil basinda alinģan‼️\n\n1.Rasul Abdikerimov\n2. 2 jildan artiq tajriybege iye,\n3. scratch,python basic, telegram bot, python development kurslari mentori,\n4.Nátiyjeleri:Telegram bot kursin pitirip házirde 30-35 % ti óz telegram botlarin jaratip kelmekte.\n5.Oqiwshilar sani 300 den aslam """)
    if data=="coreldrawmentor":
        await bot.send_message(chat_id=call.from_user.id,text="""Maģliwmat 2024-jil basinda alinģan‼️\n\nBektemirov Asadbek\n2-jilliq tájriybege iye\nNátiyjeleri:Birinshi gruppadan 2 adam, Ekinshi gruppadan bolsa 4 adam jumisli bolģan\nOqiwshilar sani:13 """)
    if data=="autoaadmentori":
        await bot.send_message(chat_id=call.from_user.id,text="""Maģliwmat 2024-jil basinda alinģan‼️\n\nAydos Ayapov\n2 jil is tájriybege iye\nNátiyje:Interer diyzayn boyinsha 8\nNátiyje:Eksteriyer boyinsha 6 Hám animaciya boyinsha 5 real proektler menen islesken  1.5 jil ishinde 40 tan aslam
                                                    """)
    if data=="photoshopmentor":
        await bot.send_message(chat_id=call.from_user.id,text="""Maģliwmat 2024-jil basinda alinģan‼️\n\nBegdiyar Bazarbaev\n4 jilǵa jaqın tájriybege iye\nÓzbekistanda islesip kórgen proektleri:TexnoPOS, Forest, Tiffanı, Alpamıs Stomed,\nPlatoBooks, Rivoj Yulduz, Socially uz, Karsoft,\nIntuza , Camelot Academy, RedFox, ITUnity h.t.b.\nbrendlerge grafik dizayn xizmetleri menen islesip kórgen.\nOqiwshilar sani: 30 dan ziyad""")
    if data=="komMentor":
        await bot.send_message(chat_id=call.from_user.id,text="""Maģliwmat 2024-jil basinda alinģan‼️\n\nElmuratova Feruza\n1,5jil tájriybege iya\nNátiyjeler:Jumisqa kirgenleri sani 50 bilgenleri\nOqiwshilar sani:400""")
    if data == "quit":    
        await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                            message_id=call.message.message_id,
                                            reply_markup=inlinemarkup)
    if data == "quit2":    
        await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                            message_id=call.message.message_id,
                                            reply_markup=admininlinemark)
    if data == "quit3":    
        await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                            message_id=call.message.message_id,
                                            reply_markup=admininlinemark)
    if data == 'video':
        await bot.send_message(chat_id=call.from_user.id, text="🎥Vidioli Reklama🎥\n✅Videoni astinda maģliwmati menen jiberseńiz boladi✅")
        await Reklamavidio.reklameVideo.set()
    if data == 'suwret':
        await bot.send_message(chat_id=call.from_user.id, text="🖼Suwretli Reklama🖼\n✅Suwretti astinda maģliwmati menen jiberseńiz boladi✅")
        await Reklamavidio.reklamaPhoto.set()
    if data == 'scratch':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Scratch \n3-6-klass oqiwshilari ushin arnalg'an Scratch kursimizda oqiģan ballar ózleri bilmegen halda IT tarawina dáslepki qa'demin taslaydi.Yaģiniy programmalastiriw algaritimlerin úyrenedi ha'm logikasin jaqsilaydi.\nKurs:⏳3 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bólimin saylań\nElede toliq maģliwmatģa iye boliwdi qaleseńiz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")
    if data == 'pythonBasic':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Python Basic \nÁpiwayilastirilģan sintaksis ha'm quramali bolmag'an ko'p paydalanilatug'i tillerdin' biri.U'yreniw ha'm paydalaniwdin' an'sat ekenligi sebepli python kodlari basqa programmalastiriw tillerinen an'sat jaziladi ha'm tezlew a'melge asiriladi.\nKurs:⏳3 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")
    if data == 'pythonDev':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Python Development \nKursda web-sayt jaratiw ha'm API arqali Front-End,Android penen baylanisiw u'yretiledi.Basqalardan o'zgeshe tu'rde ajralip turatug'in shirayli web-betlerin jaratiwdi HTML ha'm CSS da u'yrenesiz.Operativ ha'm natiyjeli web-qosimshalardi islep shig'ariw tiykari bolg'an Django menen islewdi u'yreniw mu'mkinshiligine iyesiz.\nKurs:⏳4 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")
    if data == 'teleBot':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Telegram Bot \nBotlar kerekli mag'liwmatlardi tabiw ushin adamlarg'a jaqin jardemshi bolip belmekte.Bul kursda siz hawa rayi,moderator,valyuta ha'm biznes ushin botlar jaratiwdi u'yrenesiz.\nKurs:⏳1 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")
    if data == 'androidDev':
        await bot.send_message(chat_id=call.from_user.id,text="""🌟Android Development \nAndroid Studio arqali Kotlin ya'ki Java tillerinde jazilg'an kodlardi Android programmag'a aylandiriw mu'mkin.Ha'm sol programmalardi "GOOGLE PLAY MARKET"platformasina ju'klew mu'mkin\nKurs:⏳8 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.""")
    if data == 'frontEnd':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Front-end \nBul ha'r tu'rli web-saytlar,web-programmalardin' bizge ko'rinip turg'an ta'repi esaplanadi.Siz ko'rgen ba'rshe saytlardag'i ha'r tu'rli animaciyalar,tu'ymeler,jaziwlar,su'wretler ha'm basqa ba'rshe bizge ko'rinip turg'an ta'repi Front-End bolip esaplanadi.\nKurs:⏳6 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")    
    if data == 'backEnd':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Back-End \nBasqa kompyuterlerdin xabarlarina juwap beretug'in tarmaqqa (Internetka) jalg'ang'an kompyuterlerde isleydi.Apparat ha'm programmaliq ta'minat toplami bolip,onin' ja'rdeminde sayttin' islew logikasi a'melge asiriladi.Yag'niy paydalaniwshig'a ko'rinbes ta'repi.\nKurs:⏳6 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")      
    if data == 'kompyuter':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Kompyuter sawatxanlıǵı  \nKurs dawaminda kompyuterden duris paydalaniw,microsoft word,excel,power point siyaqli ofis programmalari menen islesiw internet tarmaqlarinan paydalaniwdi uyrenip barasiz.\nKurs:⏳1 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")
    if data == 'photoshop':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Photoshop \nBul grafik dizaynerlerdin' en' tiykarg'i is qurallarinin' biri bolip esaplanadi.Photoshop programmasi arqali su'wretlerdi qayta islew redaktorlaw ha'm ha'r tu'rli elementler ja'rdeminde dizaynlar jaratiw mu'mkin.\nKurs:⏳2 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")       
    if data == 'corelDraw':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Corel Draw \nBul grafik dizaynerler ushin arnalg'an,vektorli grafika menen islewshi kompyuter programmasi bolip esaplanadi.Corel Draw ja'rdeminde u'lken o'lshemde basip shig'arilatug'in o'nimler ushin dizayn jaratiw mu'mkin.\nKurs:⏳1 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")
    if data == 'autocad':
        await bot.send_message(chat_id=call.from_user.id,text="🌟AutoCad 3DS MAX \n2 ha'm 3 o'lshemli grafika menen islewshi,imaratlardin 3D ko'rinisin jaratiwmushin qollaniladi.3DS MAX programmasi menen birgelikte interior dizayn jaratiw mu'mkin.\nKurs:⏳4 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")        
    if data == 'mobiloGr':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Mobilografiya \nBul smartfon kamerasi ja'rdeminde professional da'rejede video kontend tu'siriw.Jaqin waqit ishinde mobilografiya tarawi en' aktual ka'siplerdin biri boliwi ku'tilmekte.\nKurs:⏳1 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")      
    if data == 'rustil':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Rus tili \nBul kursda siz birinshi bolip Rus-tili gramatikasin u'yrenesiz ha'm onnan kiyin Rus-tilin duris so'ylewdi u'yrenesiz.Kurstin son'g'i 2 ayinda Rus-tilinde so'ylew,pikir ju'ritiwdi u'yrenip barasiz.\nKurs:⏳4 Ay dawam etedi.\nSabaqlar:Offline boladi.\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")      
    if data == 'media':
        await bot.send_message(chat_id=call.from_user.id,text="🌟Media jurnalistika .\nKurisqa jaziliw ushin:📝Oqiw ushin registratsiya📝 bo'limin saylan'\nElede toliq mag'liwmatg'a iye boliwdi qalesen'iz✅ \nBaylanıs ushın:  +998 90 592 71 17 \nAdminimiz: @texnopos_admin.")       



#                                       FSMCONTEXT  BO'LIMI
        
#                                       ADMINLER BO'LIMI
#ADMIN QOSIW BO'LIMI           

@dp.message_handler(state=Admins.chat_id)
async def send_id(message: types.Message, state: FSMContext):
    if message.text == "/start" or message.text== "/stop":
        await message.answer(text=f"Assalawma a'leykim {message.from_user.full_name}",reply_markup=admininlinemark)
        await state.finish()
    elif message.text.isdigit():
        async with state.proxy() as data:
            data['chat_id'] = message.text
        await message.answer(text="Qosilatug'in adminnin' Atin jazip jiberin!..")
        await Admins.next()
    else:
        await message.answer(text="ID tek gana san boliwi kerek‼️")
@dp.message_handler(state=Admins.name)
async def send_name(message: types.Message, state: FSMContext):
    if message.text== "/start" or message.text== "/stop":
        await message.answer(text=f"Assalawma a'leykim {message.from_user.full_name}",reply_markup=admininlinemark)
        await state.finish() 
    elif len(message.text.split())==1: #2 soz ekenin tekseredi
        if not ("0" in message.text or 
            "1" in message.text or 
            "2" in message.text or 
            "3" in message.text or 
            "4" in message.text or 
            "5" in message.text or 
            "6" in message.text or 
            "7" in message.text or 
            "8" in message.text or 
            "9" in message.text ):
            async with state.proxy() as data:
                data['name'] = message.text
            await message.answer(text="Qosilatug'in adminnin' Telefon nomerin jiberin!..")
            await Admins.next()  
    else:
        await message.answer(text="Siz qa'te mag'liwmat kiritip atrsiz")        
@dp.message_handler(state=Admins.number)
async def send_nomer(message: types.Message, state: FSMContext):
    if message.text== "/start" or message.text== "/stop":
        await message.answer(text=f"Assalawma a'leykim {message.from_user.full_name}",reply_markup=admininlinemark)
        await state.finish()
    elif len(message.text)<12 or not message.text.startswith("+998") or not message.text[4:].isdigit():
        await message.answer("Siz nomerinizde qa'telik bar.Iltimas nomerinizdi duris kiritin‼️") 
    else:
        async with state.proxy() as data:
            data['number'] = message.text
            await message.answer(text=f'''Admin qosiw juwmaqlandi!
            Admin id nomer:{data['chat_id']},
            Admin Ati:{data['name']},
            Admin Telefon nomeri:{data['number']},
            ''')    
            await state.finish()
            add_datas(data['chat_id'],data['name'],data['number'])
@dp.message_handler(state=Admins.deleteAdmin)
async def del_admin(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['deleteAdmin'] = message.text
        await message.answer(text="Siz kiritken id nomer iyesi Adminlik huquqinan ayrildi‼️")
        delete_admin(data["deleteAdmin"])
        await state.finish()
    else:
        await bot.send_message(chat_id=message.from_user.id,text="Siz kiritken id nomerde qa'telik bar❌")
    await state.finish()

#REKLAMA JIBERIW BOLIMI 

@dp.message_handler(content_types=types.ContentType.VIDEO,state=Reklamavidio.reklameVideo)
async def send_vid(msg:types.Message,state:FSMContext):
    caption = msg.caption
    async with state.proxy() as data:
        data['reklamaVidio']= msg.video.file_id
        users = get_users_id()
        for i in users:
            try:
                await bot.send_video(chat_id=i,video=msg.video.file_id,caption=caption)
            except:
                print("sizdin botinizdi bloklagani sebepli ayrim adamlarga video barmadi")    
    await state.finish()
@dp.message_handler(content_types=types.ContentType.PHOTO,state=Reklamavidio.reklamaPhoto)
async def send_pt(msg:types.Message,state:FSMContext):
    caption = msg.caption
    async with state.proxy() as data:
        ph = data['reklamaPhoto']=msg.photo[0]['file_id']
        users = get_users_id()
        for i in users:
            try:
                await bot.send_photo(chat_id=i,photo=ph,caption=caption)
            except:
                print("sizdin botinizdi bloklagani sebepli ayrim adamlarga Photo barmadi")   
    await state.finish()
 

 
#                               USERLER MENEN ISLESIW BOLIMI
# OQIW USHIN KIRITILGEN Feedback

@dp.message_handler(state=usinislar.sayla)
async def sayla_answer(msg:types.Message,state:FSMContext):
    if len(msg.text.split())==2: #2 soz ekenin tekseredi
        if not ("0" in msg.text or 
            "1" in msg.text or 
            "2" in msg.text or 
            "3" in msg.text or 
            "4" in msg.text or 
            "5" in msg.text or 
            "6" in msg.text or 
            "7" in msg.text or 
            "8" in msg.text or 
            "9" in msg.text ): # san joq ekenligin tekseredi 
                surname, name = msg.text.split(maxsplit=1)
                if surname.lower().endswith(("ov","ova","ev","eva")):
                    if name.isalpha() and name.strip():
                        async with state.proxy() as data:
                            data['sayla'] = msg.text
                        await msg.answer("Oqıtıp atırǵan mentorıńızdı 1 balldan 10 ballǵa shekem bahalań.",reply_markup=ball)
                        await usinislar.next()
                else:
                    await msg.answer("Tómendegi Mentorlardan ózininizge tiyislisin saylan.")        
        else: await msg.answer("Tómendegi Mentorlardan ózininizge tiyislisin saylan.") 
    else: await msg.answer("Tómendegi Mentorlardan ózininizge tiyislisin saylan.") 
@dp.message_handler(state=usinislar.sistmball)
async def ball_answer(msg:types.Message,state:FSMContext):
    if msg.text=="1 ball😔" or msg.text=="2 ball☹️" or msg.text=="3 ball🙁" or msg.text=="4 ball😕" or msg.text=="5 ball👍🏻" or msg.text=="6 ball☺️" or msg.text=="7 ball😊" or msg.text=="8 ball😇" or msg.text=="9 ball🤩" or msg.text=="10 ball🥳":
        async with state.proxy() as data:
            data['sistmball'] = msg.text
        await msg.answer("Mentordıń pedogogikalıq sheberligi unaydı ma?",reply_markup=sbprinsp)
        await usinislar.next()
    else:
        await msg.answer("Iltimas tómendegi balldiń birin saylań‼️",reply_markup=ball)
@dp.message_handler(state=usinislar.sbprins)
async def prinsip_answer(msg:types.Message,state:FSMContext):
    if msg.text=="🤩Awa🤩" or msg.text=="🙂Ortasha🙂" or msg.text=="😔Yaq😔":
        async with state.proxy() as data:
            data['sbprins'] = msg.text
        await msg.answer("Ótilgen temanı úyde tákirarlaw imkaniyatı jaratılǵan ba? Youtube yáki Videojazıw",reply_markup=takrarlaw)
        await usinislar.next()
    else:
        await msg.answer("Iltimas tómendegi birin saylań‼️",reply_markup=sbprinsp)
@dp.message_handler(state=usinislar.tarrar)
async def takrarlaw_answer(msg:types.Message,state:FSMContext):
    if msg.text=="🤩Toliq jaratilgan🤩" or msg.text=="🙂Toliq emes🙂" or msg.text=="😔Jaratilmagan😔":
        async with state.proxy() as data:
            data['tarrar'] = msg.text
        await msg.answer("Sizge administraciyanıń xızmet kórsetiwi unaydı ma?",reply_markup=adwork)
        await usinislar.next()
    else:
        await msg.answer("Iltimas tómendegi birin saylań‼️",reply_markup=takrarlaw)
@dp.message_handler(state=usinislar.adw)
async def adw_answer(msg:types.Message,state:FSMContext):
    if msg.text == "🤩Unaydi🤩" or msg.text == "🙂Ortasha🙂":
        async with state.proxy() as data:
            data['adw'] = msg.text
        await msg.answer("Qosımsha pikir hám usınıslarıńız bar ma? Bar bolsa jazıp qaldırsańız esitiwden quwanamız!🙌",reply_markup=qosimsha)
        await usinislar.next()
    else:
        await msg.answer("Jazip qaldirin': ")
        if msg.text != "💭Pikir qaldiriw💭":
            async with state.proxy() as data:
                data['adw'] = msg.text
                await msg.answer("Qosımsha pikir hám usınıslarıńız bar ma? Bar bolsa jazıp qaldırsańız esitiwden quwanamız!🙌",reply_markup=qosimsha)
                await usinislar.next() 
@dp.message_handler(state=usinislar.txt)
async def txt_answer(msg:types.Message,state:FSMContext):
    if msg.text == "😉Yaq😉":
        async with state.proxy() as data:
            data["txt"] = "Joq"
        await msg.answer(f"🎉🎉Raxmet. Siziń pikir hám usınıslarıńızdı inabatqa alamız hám keleshekte olardı tuwırlawǵa háreket etemiz‼️\n\nSizdin Mentoriniz:{data['sayla']}\n\nQoygan Balliniz: {data['sistmball']}\n\nSabaq o'tiw prinsipi: {data['sbprins']}\n\nTakrarlaw Imkanyatiniz: {data['tarrar']}\n\nAdminstraciya Jumisi: {data['adw']}\n\nQosimsha pikiriniz: {data['txt']}")
        add_feedback(msg.from_user.id,msg.from_user.username,data['sayla'],data['sistmball'],data['sbprins'],data['tarrar'],data['adw'],data['txt'])
        ad = get_admin_us_data()
        for i in ad:
            await bot.send_message(chat_id=i,text=f"Usinis kiritiwshi:@{msg.from_user.username}\n\nSizdin Mentoriniz:{data['sayla']}\n\nQoygan Balliniz: {data['sistmball']}\n\nSabaq o'tiw prinsipi: {data['sbprins']}\n\nTakrarlaw Imkanyatiniz: {data['tarrar']}\n\nAdminstraciya Jumisi: {data['adw']}\n\nQosimsha pikiriniz: {data['txt']}",parse_mode="HTML")
                
        await state.finish()   
    else:
        await msg.answer("Jazip qaldirin': ")
        if msg.text != "🤩Awa🤩":
            async with state.proxy() as data:
                data['txt'] = msg.text
                await msg.answer(f"🎉🎉Raxmet. Siziń pikir hám usınıslarıńızdı inabatqa alamız hám keleshekte olardı tuwırlawǵa háreket etemiz‼️\n\nSizdin Mentoriniz:{data['sayla']}\n\nQoygan Balliniz: {data['sistmball']}\n\nSabaq o'tiw prinsipi: {data['sbprins']}\n\nTakrarlaw Imkanyatiniz: {data['tarrar']}\n\nAdminstraciya Jumisi: {data['adw']}\n\nQosimsha pikiriniz: {data['txt']}")
                add_feedback(msg.from_user.id,msg.from_user.username,data['sayla'],data['sistmball'],data['sbprins'],data['tarrar'],data['adw'],data['txt'])
                ad = get_admin_us_data()
                for i in ad:
                    await bot.send_message(chat_id=i,text=f"Usinis kiritiwshi:@{msg.from_user.username}\n\nSizdin Mentoriniz:{data['sayla']}\n\nQoygan Balliniz: {data['sistmball']}\n\nSabaq o'tiw prinsipi: {data['sbprins']}\n\nTakrarlaw Imkanyatiniz: {data['tarrar']}\n\nAdminstraciya Jumisi: {data['adw']}\n\nQosimsha pikiriniz: {data['txt']}")
                await state.finish()     

#   OQIW USHIN KIRITILGEN ARZALAR BO'LIMI
@dp.message_handler(state=newArza.name)
async def newArza_name_answer(msg:types.Message,state:FSMContext):
    if len(msg.text.split())==1: #1 soz ekenin tekseredi
        if not ("0" in msg.text or 
            "1" in msg.text or 
            "2" in msg.text or 
            "3" in msg.text or 
            "4" in msg.text or 
            "5" in msg.text or 
            "6" in msg.text or 
            "7" in msg.text or 
            "8" in msg.text or 
            "9" in msg.text ): # san joq ekenligin tekseredi 
                async with state.proxy() as data:
                    data['name'] = msg.text
                await msg.answer(f"Atiniz qabil qilindi✅.\n\n{msg.text}")
                await msg.answer("Telefon nomerinizdi kiritin:")
                await newArza.next()     
        else: await msg.answer("Atin'izda san qatnasiwi mumkin emes!❌") 
    else: await msg.answer("Magan tek atinizdi jiberin.") 

@dp.message_handler(state=newArza.phone)
async def newArza_phone(msg:types.Message,state:FSMContext):
    if len(msg.text)==13 and msg.text.startswith("+998") and  msg.text[4:].isdigit():
        async with state.proxy() as data:
            data['phone'] = msg.text
        await msg.answer(f"Telefon nomeriniz qabil qilindi✅\n\n{msg.text}")
        # data = await state.get_data()
        arza = (f"Arza beriwshi:{data.get('name')}\n"
            f"Username:@{msg.from_user.username}\n"
            f"Telefon nomeri:{data.get('phone')}")  
        await msg.answer(arza) 
        await msg.answer("Magliwmatlar Durisba ya'ki qa'telik barma?",reply_markup=yesorno)
        await newArza.next()
    else:
        await msg.answer("Siz nomerinizde qa'telik bar.Iltimas nomerinizdi duris kiritin‼️") 
    
@dp.message_handler(state=newArza.magliwmat)
async def newArza_phone(msg:types.Message,state:FSMContext):  
    if msg.text == "✅Duris✅":
        async with state.proxy() as data:
            data['magliwmat'] = msg.text
        arza = (f"Arza beriwshi:{data.get('name')}\n"
        f"Username:@{msg.from_user.username}\n"
        f"Telefon nomeri: {data.get('phone')}")
        ad = get_admin_us_data()
        for i in ad:
            await bot.send_message(chat_id=i,text=f"Oqiw Ushin Taza Arza kelip Tu'sti:\n\n{arza}")
            await msg.answer("Arzaniz qabil qilindi.✅")  
            arzalar_add_datas(data['name'],msg.from_user.full_name,msg.from_user.username,data['phone'])
            await state.finish() 
    elif msg.text == "❌Qa'te❌":
        await msg.answer("Basinan Baslawiniz mu'mkin‼️",reply_markup=inlinemarkup)  
        await state.finish()
    else:
        await msg.answer("To'mendegi tuymeshelerden birin saylan‼️",reply_markup=yesorno)
            

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)  




