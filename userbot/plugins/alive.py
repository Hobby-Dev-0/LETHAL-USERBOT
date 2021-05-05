# LETHAL CO-ORPERATION (C) 2021 
# GNU LICENSED PROJECT 
# RIGHTS RECERVED BY LETHAL (c) 2021
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LETHAL"


global ghanti
ghanti = borg.uid
edit_time = 5
file1 = "https://telegra.ph/file/f3cc12961473cafac688c.jpg"
file2 = "https://telegra.ph/file/facc5d79ceb51d6ccd3fc.jpg"
file3 = "https://telegra.ph/file/e3b40c104c8080275c27e.jpg"
file4 = "https://telegra.ph/file/18d0a83bdb8eada63bfc8.jpg"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "**𝐋𝐄𝐓𝐇𝐀𝐋 𝐈𝐒 𝐖𝐎𝐑𝐊𝐈𝐍𝐆**\n\n"
    pm_caption += "**уєѕ мαѕтєя, αм αℓινє αη∂ ѕуѕтєм ιѕ ωσякιηg ρєяƒє¢тℓу αѕ ιт ѕнσυℓ∂ вє...**\n\n"
    pm_caption += "✘ 𝕬𝖇𝖔𝖚𝖙 𝕸𝖞 𝕾𝖞𝖘𝖙𝖊𝖒 ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/lethal_userbot_official)\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [𝚃𝙴𝙰𝙼 𝙲𝙾𝙱𝚁𝙰](https://github.com/LETHAL-ARMY/LETHAL-USERBOT)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [ℓєтнαℓ](https://github.com/LETHAL-ARMY/LETHAL-USERBOT)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    

