# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="SonaAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="SonaAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="SonaAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="SonaAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="SonaAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"sᴛᴀʀᴛɪɴɢ ᴀssɪsᴛᴀɴᴛs...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("kriti_bot_update")
                await self.one.join_chat("kriti_bot_update")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ")
            except:
                LOGGER(__name__).error(
                    "ᴀssɪsᴛᴀɴᴛ ᴀccᴏᴜɴᴛ 1 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ. ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴀs ᴀᴅᴍɪɴ!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"ᴀssɪᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ ᴀs {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("kriti_bot_update")
                await self.one.join_chat("kriti_bot_update")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ")
            except:
                LOGGER(__name__).error(
                    "ᴀssɪsᴛᴀɴᴛ ᴀccᴏᴜɴᴛ 2 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ. ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴀs ᴀᴅᴍɪɴ!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"ᴀssɪᴛᴀɴᴛ ᴛᴡᴏ sᴛᴀʀᴛᴇᴅ ᴀs {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("kriti_bot_update")
                await self.one.join_chat("kriti_bot_update")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ")
            except:
                LOGGER(__name__).error(
                    "ᴀssɪsᴛᴀɴᴛ ᴀccᴏᴜɴᴛ 3 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ!"
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"ᴀssɪᴛᴀɴᴛ ᴛʜʀᴇᴇ sᴛᴀʀᴛᴇᴅ ᴀs {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("kriti_bot_update")
                await self.one.join_chat("kriti_bot_update")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ")
            except:
                LOGGER(__name__).error(
                    "ᴀssɪsᴛᴀɴᴛ ᴀccᴏᴜɴᴛ 4 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ!"
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"ᴀssɪᴛᴀɴᴛ ғᴏᴜʀ sᴛᴀʀᴛᴇᴅ ᴀs {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("kriti_bot_update")
                await self.one.join_chat("kriti_bot_update")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "❖ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ")
            except:
                LOGGER(__name__).error(
                    "ᴀssɪsᴛᴀɴᴛ ᴀccᴏᴜɴᴛ 5 ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ!"
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"ᴀssɪᴛᴀɴᴛ ғɪᴠᴇ sᴛᴀʀᴛᴇᴅ ᴀs {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"sᴛᴏᴘᴘɪɴɢ ᴀssɪsᴛᴀɴᴛs...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass    
                

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/REVANGEMUSIC
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
