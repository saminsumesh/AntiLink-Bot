from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Client = Client(
"Anti Link Bot",
bot_token=os.environ.get("BOT_TOKEN"),
api_id=int(os.environ.get("API_ID")),
api_hash=os.environ.get("API_HASH")
)


START_TEXT = """Hello {} , 
Am an simple and powerfull link remover bot,Which you can use on your groups

**@XD_Botz | @XD_BotzSupport** 
"""
START_BUTTONS = InlineKeyboardMarkup(
     [[
     InlineKeyboardButton("Add me to your groups", url="")
     ]]
)


@Client.on_message(filters.command & filters.private(["start"]))
async def start(bot, message):
    await message.reply_text(
    text=START_TXT.format(message.from_user.mention),
    reply_markup=START_BUTTONS,
    )
    
@Client.on_message(filters.forward & filters.document)
async def fwdmsg(bot, message):
    await message.delete
    
@Client.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("youtu.be") | filters.regex("com") | filters.regex("https") | filters.service)
async def delete(bot,message):
 await message.delete()

Client.run()