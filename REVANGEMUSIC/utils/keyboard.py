# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .functions import get_urls_from_text as is_url


def keyboard(buttons_list, row_width: int = 2):
    """
    buttons_list example:
    [
        ("Button Text", "callback_or_url"),
        ("Next", "callback_or_url")
    ]
    """
    data = []
    temp = []

    for i in buttons_list:
        if not is_url(i[1]):
            btn = InlineKeyboardButton(text=str(i[0]), callback_data=str(i[1]))
        else:
            btn = InlineKeyboardButton(text=str(i[0]), url=str(i[1]))

        temp.append(btn)

        if len(temp) == row_width:
            data.append(temp)
            temp = []

    if temp:
        data.append(temp)

    return InlineKeyboardMarkup(data)


def ikb(data: dict, row_width: int = 2):
    """
    data example:
    {
        "Button Text": "callback",
        "Google": "https://google.com"
    }
    """
    buttons = list(data.items())
    return keyboard(buttons, row_width=row_width)
# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
