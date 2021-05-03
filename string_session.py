# PROJECT LETHAL USERBOT 
#   APACHE LICENSED / COPYRIGHT RESERVED BY LETHAL ARMY
print("\n\n\n\n\nHello sir!!, I'm Here To Help u to Generate Telethon String Session")
print("\n\n LETHAL USERBOT")

print("\n\nProperly Fill APP_ID ,HASH and Number.\n")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as hehe:
	UB_SESSION = hehe.session.save()
	LETHAL = hehe.send_message(
	    "me",
	    f"`{UB_SESSION}`\n\n**Your LETHAL-USERBOT String Session Here Sir😁😎😎\nClick on above Code to Copy it\n\nJOIN @LETHAL_OT"
	)

print("\n\n############################\n")
print(
    "HUI HUI ... HO GYA SAVED MSG KHOLO YA NEECHE DIA H STRING AB DEPLOY MAARO")

print("\n############################\n")


print(f"{UB_SESSION}")

Print(" ")
