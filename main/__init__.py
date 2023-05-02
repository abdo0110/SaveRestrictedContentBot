#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 21288088
API_HASH = "b38c7a879bc3b4f0c27e2695b5536941"
BOT_TOKEN = "6018998803:AAGJoE13yjH6aPeQ_FUpbo0NtywZrN47Bm0"
SESSION = "BACfy 3eof1skknDY-3_Fq0nmVFJil0gl9MjmR4nioReJ5kWHLP3lsQxumTei6AbqWNJkad45btwy-ktQmy6YSyegU5FIr4lxsodoi5HJutoTz74yTrJrsy1A4FdsNtpJkUXfCI4_FLvux9CdYLseY0fbtqUKU40Qd6j7Oudbn59xV9t6eiQyFKZ3CnUkE2tQoXns39xs9_ri2J4JrCDChmLTZmf4wRSWKzJ70M0cFmo-2ut2J-GELF5jaqvu1Yr2UrpogVK7MdKzDzpa4GuuPAWn640WEBmZc25XRqiV9F4p5s4LYvDasyoZnGfKNiwX_AQBRzaTXvAfeZqVyuSzmy2XAAAAAXFoXs8A"
FORCESUB = "anything576"
AUTH = "6197632719"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
