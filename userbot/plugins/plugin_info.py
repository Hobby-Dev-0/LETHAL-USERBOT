
""" Userbot plugin_info command """

from userbot import CMD_HELP
from userbot.utils import admin_cmd

@borg.on(admin_cmd(outgoing=True, pattern="plinfo(?: |$)(.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="plinfo(?: |$)(.*)"))
async def info(event):
    """ For .plinfo command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Maybe the command help or plugin info has not been set or the plugin is invalid...")
    else:
        await event.edit("Please specify which plugin do you want help for !!\
            \nUsage: .pinfo <plugin name>\n IF NEED HELP VISIT @LETHAL_SUPPORT")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
