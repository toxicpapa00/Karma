# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from REVANGEMUSIC import app
from REVANGEMUSIC.core.call import Sona
from REVANGEMUSIC.utils import bot_sys_stats
from REVANGEMUSIC.utils.decorators.language import language
from REVANGEMUSIC.utils.inline import supp_markup
from REVANGEMUSIC.utils.inline import close_markup
from config import BANNED_USERS




@app.on_message(filters.command("ping", prefixes=["/", "!"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        video="https://files.catbox.moe/plxzb4.mp4",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Sona.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
