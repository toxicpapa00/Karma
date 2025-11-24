# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from REVANGEMUSIC import app
import config
from REVANGEMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**<u>❃ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ᴧᴧʀᴜᴍɪ ʀᴇᴘᴏs ❃</u>

✼ ʀᴇᴘᴏ ɪs ɴᴏᴡ ᴘʀɪᴠᴧᴛᴇ ᴅᴜᴅᴇ 😌
 
❉  ʏᴏᴜ ᴄᴧɴ мʏ ᴜsᴇ ᴘᴜʙʟɪᴄ ʀᴇᴘᴏs !! 

✼ || ᴄᴏɴᴛᴧᴄᴛ :-  [˹ ᴧᴧʀᴜᴍɪ sᴜᴘᴘᴏʀᴛ ᴄʜᴧᴛ ˼ ](https://t.me/AarumiChat) ||
 
❊ ʀᴜɴ 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
    [
        InlineKeyboardButton("ᴧᴧʀᴜᴍɪ ᴍᴜsɪᴄ", url="https://t.me/AarumiChat"),
        InlineKeyboardButton("sᴧɴᴧ ᴍᴜsɪᴄ", url="https://t.me/AarumiChat")
    ],
    [
        InlineKeyboardButton("sɪᴍᴘʟᴇ ᴍᴜsɪᴄ", url="https://t.me/AarumiChat"),
        InlineKeyboardButton("ᴄʜᴧᴛ ʙᴏᴛ", url="https://t.me/AarumiChat")
    ],
    [
        InlineKeyboardButton("ᴜsᴇʀ ʙᴏᴛ", url="https://t.me/AarumiChat"),
        InlineKeyboardButton("sᴘᴧᴍ ʙᴏᴛ", url="https://t.me/AarumiChat")
    ],
    [
        InlineKeyboardButton("sᴇssɪᴏɴ ʙᴏᴛ", url="https://t.me/AarumiChat"),
        InlineKeyboardButton("sᴇssɪᴏɴ ʜᴧᴄᴋ", url="https://t.me/AarumiChat")
    ],
    [
        InlineKeyboardButton("ʙᴧɴᴧʟʟ ʙᴏᴛ", url="https://t.me/AarumiChat"),
        InlineKeyboardButton("ᴧɴʏ ɪssᴜᴇ", user_id=config.OWNER_ID)
    ],
    [
        InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ✙", url=f"https://t.me/{app.username}?startgroup=true")
    ]
]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/7enu2i.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
