from pyrogram import Client
from config import TeleInfo

bot = Client(
    "WHOIS",
    bot_token= TeleInfo.BOT_TOKEN,
    api_id= TeleInfo.API_ID,
    api_hash= TeleInfo.API_HASH,
    plugins={
        "root":"bot/helpers"
    }
)

bot.run()