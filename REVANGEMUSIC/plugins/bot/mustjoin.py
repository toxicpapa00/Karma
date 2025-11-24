# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from REVANGEMUSIC import app

#--------------------------

MUST_JOIN = "kriti_bot_update"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://files.catbox.moe/fu6jk3.jpg", caption=f"๏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ [๏ sᴜᴘᴘᴏʀᴛ ๏]({link}) ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴄʜᴇᴀᴋ ᴍʏ ғᴇᴀᴛᴜʀᴇs.\n\nᴀғᴛᴇʀ ᴊᴏɪɴ ᴛʜᴇ [๏ ᴄʜᴀɴɴᴇʟ ๏]({link}) ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴛʏᴘᴇ /start ᴀɢᴀɪɴ !! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("• ᴊᴏɪɴ •", url="https://t.me/KRITI_SUPPORT_GROUP"),
                                InlineKeyboardButton("• ᴊᴏɪɴ •", url="https://t.me/kriti_bot_update"),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
