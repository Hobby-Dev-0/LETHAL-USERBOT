# LETHAL COBRA IMPROVED EDITION
# GNU LICENSED APPLICATION
# ALL COPYRIGHTS RESERVED BY LETHAL CO-ORPERATION (C) 2021
# SAFE APPLICATION CERTIFIED BY G.N.U ORGANISATION (c) 2021
from math import ceil
import asyncio
import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from userbot import CMD_LIST, CMD_HELP
import io
from userbot.utils import remove_plugin,load_module
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
   
    async def opner(event):
            if event.query.user_id == bot.uid :
                current_page_number=0
                dc = paginate_help(current_page_number, CMD_LIST, "helpme")
                await event.edit("`>>>\n\nReopened The Main Menu of \n©LETHAL_USERBOT` ", buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot,for more info visit @LETHAL_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            dc = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article("© lethal Userbot Help",text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),buttons=dc,link_preview=False)
            await event.answer([result] if result else None)
        else:
              reply_pop_up_alert = "Please get your own Userbot😁😁,for more info visit @LETHAL_SUPPORT! 😎😎"
              await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))#hehe
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
          
            await event.edit(buttons=dc)
        else:
            Cobra = "Please get your own Userbot, and don't use mine for more info visit @LETHAL_SUPPORT!"
            await event.answer(Cobra, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            
            await event.edit(buttons=dc)
        else:
              TheLETHAL = "GET UR OWN USERBOT AND JOIN @LETHAL_SUPPORT "
              await event.answer(TheLETHAL, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            bro = custom.Button.inline("◤✞ 𝕺𝖕𝖊𝖓 𝕸𝖆𝖎𝖓 𝕸𝖊𝖓𝖚 𝕬𝖌𝖆𝖎𝖓 ✞◥", data="open")
            await event.edit("`Main Menu Has Been Closed`", buttons=bro)
        else:
            reply_pop_up_alert = "GET UR OWN USERBOT AND JOIN @LETHAL_SUPPORT FOR ANY HELP"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

  
    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            atul= "GET UR OWN USERBOT AND JOIN @LETHAL_SUPPORT FOR HELP"
            await event.answer(atul, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        global shivam_sh1vam
        shivam_sh1vam="{}".format(plugin_name)
        help_string = "Commands found in {}:\n".format(plugin_name)
        k = "💠🔮💎"
        u = 0
        for i in CMD_LIST[plugin_name]:
            u += 1
            help_string += str(k[u % 3]) + " " + i + "\n\n"
        if plugin_name in CMD_HELP:
            help_string += (
                f"**📤 PLUGIN NAME 📤 :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
            )
        else:
            help_string += "😁"

        reply_pop_up_alert = help_string
        reply_pop_up_alert += (
            "\n\n __Click on buttons below to load or unload them..report us if you find any bug__\n\n **©LETHAL USERBOT**".format(plugin_name)
        )
        try:
            if event.query.user_id == bot.uid :
                dc = [custom.Button.inline(" 𝕭𝖆𝖈𝖐 ",data="back({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                await event.edit(reply_pop_up_alert, buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot, and don't use mine for more info visit @LETHAL_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)#hehe
        except: 
            if event.query.user_id == bot.uid :
                sh1vam = [custom.Button.inline("◤✞ 𝕲𝖔 𝕭𝖆𝖈𝖐 ✞◥",data="back({})".format(shivam)),custom.Button.inline("◤✞ 𝕮𝖑𝖔𝖘𝖊 ✞◥", data="close")]
                halps = "Do .help {} to get the list of commands.".format(plugin_name)
                await event.edit(halps,buttons=sh1vam)
            else:
                reply_pop_up_alert = "Please get your own Userbot, and don't use mine for more info visit @LETHAL_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"load\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              if event.query.user_id == bot.uid :
                    
                    
                    try:
                        fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="back({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                        load_module(event.data_match.group(1).decode("UTF-8"))# kyu sir kang krne m musil aa rhi h kya ... Bolo help kr du kya 😂😂😂
                        await event.edit( "`Your LETHAL_USERBOT Has Successfully loaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e))+ "LETHAL_USERBOT Has Successfully loaded" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="back({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot,for more info visit @LETHAL_SUPPORT!"
                    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"unload\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              if event.query.user_id == bot.uid :
                    
                    
                    try:
                        fcix = [custom.Button.inline(" 𝕭𝖆𝖈𝖐 ",data="back({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),custom.Button.inline(" 𝕷𝖔𝖆𝖉 ",data="load({})".format(shivam_sh1vam))]
                        remove_plugin(event.data_match.group(1).decode("UTF-8"))#kyu sir kang krne m muskil ho rhi h kya bologe toh help krdu 😂😂
                        await event.edit( "`Your LETHAL_USERBOT Has Successfully unloaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e)) +"LETHAL_USERBOT Has Successfully unloaded"+ str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="back({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),custom.Button.inline(" 𝕷𝖔𝖆𝖉 ",data="load({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot,for more info visit @LETHAL_SUPPORT!"
                    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)#hehehe
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
            
            if event.query.user_id == bot.uid :
                try:
                    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                    buttons = paginate_help(current_page_number-2, CMD_HELP, "helpme")
                    await event.edit("`>>> Here Is The Main Menu of\n\n©LETHAL_USERBOT`", buttons=buttons)
                except:
                    buttons = paginate_help(0, CMD_HELP, "helpme")
                    await event.edit("`>>> Here Is The Main Menu Of\n\n©LETHAL_USERBOT`", buttons=buttons)
            else:
                reply_pop_up_alert = "Please get your own Userbot,for more info visit @LETHAL_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    multi = Config.EMOJI_TO_DISPLAY_IN_HELP
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {}".format(random.choice(list(multi)), x),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    global shivam
    modulo_page = page_number % max_num_pages
    shivam=modulo_page
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("•PREVIOUS•", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("•CLOSE•", data="close"),
             custom.Button.inline("•NEXT•", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs
