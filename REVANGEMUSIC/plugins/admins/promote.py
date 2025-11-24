# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions
from functools import wraps
from REVANGEMUSIC import app

def mention(user_id, name):
    return f"[{name}](tg://user?id={user_id})"


def admin_required(*privileges):
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
            if not message.from_user:
                await message.reply_text("**⋟ ʏᴏᴜ ᴀʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ. ᴘʟᴇᴀsᴇ ᴜɴʜɪᴅᴇ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.**")
                return

            member = await message.chat.get_member(message.from_user.id)

            if member.status == enums.ChatMemberStatus.OWNER:
                return await func(client, message)

            elif member.status == enums.ChatMemberStatus.ADMINISTRATOR:
                missing = []
                for priv in privileges:
                    if not getattr(member.privileges, priv, False):
                        missing.append(priv)

                if missing:
                    await message.reply_text(f"**⋟ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴs :-** {', '.join(missing)}")
                    return

                return await func(client, message)

            else:
                await message.reply_text("**⋟ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ.**")
                return

        return wrapper
    return decorator


async def extract_user_and_title(message, client):
    user = None
    title = None

    cmd = message.text.split()[0]
    text = message.text[len(cmd):].strip()

    if message.reply_to_message:
        user = message.reply_to_message.from_user
        if not user:
            await message.reply_text("**⋟ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴜsᴇʀ ɪɴ ʀᴇᴘʟy.**")
            return None, None, None
        title = text

    else:
        args = text.split(maxsplit=1)
        if not args:
            await message.reply_text("**⋟ sᴘᴇᴄɪꜰʏ ᴀ ᴜsᴇʀ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ.**")
            return None, None, None

        try:
            user = await client.get_users(args[0])
        except:
            await message.reply_text("**⋟ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ.**")
            return None, None, None

        title = args[1] if len(args) > 1 else None

    return user.id, user.first_name, title


def format_msg(chat, user_m, admin_m, action):
    txt = "PROMOTING" if action == "promote" else "ᴅᴇᴍᴏᴛɪɴɢ"
    return (
        f"**⋟ {txt} A USER IN {chat}\n"
        f"USER :- {user_m}\n"
        f"ADMIN :- {admin_m}**"
    )


@app.on_message(filters.command("promote"))
@admin_required("can_promote_members")
async def promote_cmd(client, message):
    user_id, name, title = await extract_user_and_title(message, client)
    if not user_id:
        return

    try:
        member = await client.get_chat_member(message.chat.id, user_id)
        if member.status == enums.ChatMemberStatus.ADMINISTRATOR:
            await message.reply_text("**⋟ ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴀᴅᴍɪɴ.**")
            return

        await client.promote_chat_member(
            message.chat.id,
            user_id,
            privileges=member.privileges
        )

        if title:
            await client.set_administrator_title(message.chat.id, user_id, title)

        await message.reply_text("**⋟ ᴜsᴇʀ ᴘʀᴏᴍᴏᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.**")

    except ChatAdminRequired:
        await message.reply_text("**⋟ ᴵ ᴺᴱᴱᴰ ᴾᴿᴼᴹᴼᵀᴱ ᴾᴱᴿᴹᴵˢˢᴵᴼᴺ.**")
    except Exception as e:
        await message.reply_text(f"**⋟ ERROR :- {e}**")


@app.on_message(filters.command("demote"))
@admin_required("can_promote_members")
async def demote_cmd(client, message):
    user_id, name, _ = await extract_user_and_title(message, client)
    if not user_id:
        return

    try:
        member = await client.get_chat_member(message.chat.id, user_id)

        if member.status != enums.ChatMemberStatus.ADMINISTRATOR:
            await message.reply_text("**⋟ USER IS NOT ADMIN.**")
            return

        await client.promote_chat_member(
            message.chat.id,
            user_id,
            privileges=ChatPermissions()
        )

        await message.reply_text("**⋟ USER DEMOTED SUCCESSFULLY.**")

    except ChatAdminRequired:
        await message.reply_text("**⋟ I NEED DEMOTE PERMISSION.**")
    except Exception as e:
        await message.reply_text(f"**⋟ ERROR :- {e}**")

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
