from subprocess import getoutput 
from art import text2art
from colorama import Fore,Back, Style, init
init()

#ColorFull strings 
SUCCESS = Fore.GREEN
ERROR = Fore.RED 
INFO = Fore.YELLOW
BANNER = Fore.CYAN
RESET = Style.RESET_ALL

# variables 
banner = text2art("Notification", "cybersmall")
option = ''
webHook_url = ''
api_key = ''
chat_id = ''
data_str = "{{data}}"

def logic(option):
  global webHook_url, api_key, chat_id
  if option == '1' or option =='01':
    print(ERROR+"["+BANNER+"-"+ERROR+"] "+SUCCESS+"Discord selected"+RESET,end="\n")
    print(Back.GREEN+"Example : https://discord.com/api/webhooks/XXXXXXXX",RESET,end="\n")
    print(ERROR+"["+BANNER+"~"+ERROR+"] "+BANNER+"Webhook url : "+RESET,end="")
    webHook_url = input()
    

  elif option == '2' or option == '02':
    print(ERROR+"["+BANNER+"-"+ERROR+"] "+SUCCESS+"Telegram selected"+RESET,end="\n")
    print(Back.GREEN+"Example API key: XXXXXXXXXXXX",RESET,end="\n")
    print(Back.GREEN+"Example Chat ID: XXXXXXXXXXXX",RESET,end="\n")
    print(ERROR+"["+BANNER+"~"+ERROR+"] "+BANNER+"API key : "+RESET,end="")
    api_key = input()
    print(ERROR+"["+BANNER+"~"+ERROR+"] "+BANNER+"Chat id : "+RESET,end="")
    chat_id = input()

  elif option == '3' or option == '03':
    print(ERROR+"["+BANNER+"-"+ERROR+"] "+SUCCESS+"All selected"+RESET,end="\n")
    print(ERROR+"["+BANNER+"-"+ERROR+"] "+SUCCESS+"Discord Setup"+RESET,end="\n")
    print(Back.GREEN+"Example : https://discord.com/api/webhooks/XXXXXXXX",RESET,end="\n")
    print(ERROR+"["+BANNER+"~"+ERROR+"] "+BANNER+"Webhook url : "+RESET,end="")
    webHook_url = input()

    print(ERROR+"["+BANNER+"-"+ERROR+"] "+SUCCESS+"Telegram Setup"+RESET,end="\n")
    print(Back.GREEN+"Example API key: XXXXXXXXXXXX",RESET,end="\n")
    print(Back.GREEN+"Example Chat ID: XXXXXXXXXXXX",RESET,end="\n")
    print(ERROR+"["+BANNER+"~"+ERROR+"] "+BANNER+"API key : "+RESET,end="")
    api_key = input()
    print(ERROR+"["+BANNER+"~"+ERROR+"] "+BANNER+"Chat id : "+RESET,end="")
    chat_id = input()
  elif option == '0' or option == '00':
    print(ERROR+"["+BANNER+"-"+ERROR+"] "+SUCCESS+"Notification installer skipped"+RESET,end="\n")
    pass
  else :
    print(INFO+"["+"*"+INFO+"]"+BANNER+"Error incorrect input"+RESET)
    notify_option()

def notify_option():
  # Banner portion
  global data
  print(BANNER+banner+RESET,end="")
  print(INFO+text2art("Setup")+RESET)
  print(BANNER+"["+"+"+BANNER+"] "+SUCCESS+"Tool created by whoami-anoint and selenophilem7"+RESET,end="\n\n")

  # Options portion
  print(BANNER+".:.Options to create notification system.:."+RESET)
  print(ERROR+"["+BANNER+"01"+ERROR+"] "+INFO+"Discord"+RESET)
  print(ERROR+"["+BANNER+"02"+ERROR+"] "+INFO+"Telegram"+RESET)
  print(ERROR+"["+BANNER+"03"+ERROR+"] "+INFO+"ALL"+RESET)
  print(ERROR+"["+BANNER+"00"+ERROR+"] "+INFO+"Skip notification"+RESET,end="\n\n")
  print(ERROR+"["+BANNER+"~"+ERROR+"] "+BANNER+"Select and option: "+RESET,end="")
  data = input()
  logic(data)

notify_option()
# Logical Portion

telegram = (f'\
telegram:\n\
  - id: "tel"\n\
    telegram_api_key: "{api_key}"\n\
    telegram_chat_id: "{chat_id}"\n\
    telegram_format: "{data_str}"\n\
')

discord = (f'\
discord:\n\
  - id: "crawl"\n\
    discord_channel: "crawl"\n\
    discord_username: "test"\n\
    discord_format: "{data_str}"\n\
    discord_webhook_url: "{webHook_url}"\n\
')


user = getoutput('whoami')
with open(f"/home/{user}/.config/notify/provider-config.yaml", 'w') as config:
  if data == '1':
    config.write(discord)
  elif data == '2':
    config.write(telegram)
  elif data == '3':
    config.write(discord+'\n\n'+telegram)
config.close()
print(ERROR+"["+BANNER+"-"+ERROR+"] "+SUCCESS+"Configuration file is setuped in : $HOME/.config/notify/provider-config.yaml"+RESET,end="\n")
getoutput('echo "Installation completed !!"| notify -silent >/dev/null')
