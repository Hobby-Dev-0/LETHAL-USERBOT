
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd, sudo_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/e763c648ab93aae019e31.png"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LETHAL USER"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**🔱LETHAL IS Awake🔱 \n\n\n**"
   ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
   ALIVE_MESSAGE += f"`Telethon: TELETHON-1.21.0 \n\n`"
   ALIVE_MESSAGE += f"`Python: PYTHON-3.9.4 \n\n`"
   ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n\n`"
   ALIVE_MESSAGE += f"`Support Channel` : @LETHAL_SUPPORT \n\n"
   ALIVE_MESSAGE += f"`MY BOSS🤗`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
@borg.on(sudo_cmd(pattern=r"awake")allow_sudo=True)
#@bot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
