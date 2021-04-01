import requests, os, platform, time
from colorama import Fore, Back, Style


print(Fore.YELLOW + """
         ,-.-.     ,----.             ,--.-,,-,--,   _,.---._       _,.---._    ,--.-.,-.      ,----.               
,-..-.-./  \==\ ,-.--` , \   _..---. /==/  /|=|  | ,-.' , -  `.   ,-.' , -  `. /==/- |\  \  ,-.--` , \  .-.,.---.   
|, \=/\=|- |==||==|-  _.-` .' .'.-. \|==|_ ||=|, |/==/_,  ,  - \ /==/_,  ,  - \|==|_ `/_ / |==|-  _.-` /==/  `   \  
|- |/ |/ , /==/|==|   `.-./==/- '=' /|==| ,|/=| _|==|   .=.     |==|   .=.     |==| ,   /  |==|   `.-.|==|-, .=., | 
 \, ,     _|==/==/_ ,    /|==|-,   ' |==|- `-' _ |==|_ : ;=:  - |==|_ : ;=:  - |==|-  .|  /==/_ ,    /|==|   '='  / 
 | -  -  , |==|==|    .-' |==|  .=. \|==|  _     |==| , '='     |==| , '='     |==| _ , \ |==|    .-' |==|- ,   .'  
  \  ,  - /==/|==|_  ,`-._/==/- '=' ,|==|   .-. ,\\==\ -    ,_ / \==\ -    ,_ //==/  '\  ||==|_  ,`-._|==|_  . ,'.  
  |-  /\ /==/ /==/ ,     /==|   -   //==/, //=/  | '.='. -   .'   '.='. -   .' \==\ /\=\.'/==/ ,     //==/  /\ ,  ) 
  `--`  `--`  `--`-----```-._`.___,' `--`-' `-`--`   `--`--''       `--`--''    `--`      `--`-----`` `--`-`--`--'  
""")
print("\n")




#defining
if platform.system() == "Windows":
    clearcmd = "cls"
else:
    clearcmd = "clear"
data = {}




choice = input(Fore.RED +">> Do you want to send an Embed or a normal message?\n1:Embed\n2:normal message:\n")

if choice == '1':
    username = input(">>What should be the Username?:\n")
    header = input(">>What should be the title?:\n")
    desc = input(">>What should be the description?:\n")
    footer = input(">>What should be the Footer?:\n")


    embed = {
        "embeds": [
            {

                "author": {
                    "name": username,
                    "url": "https://github.com/Blcksoda",
                    "icon_url": "https://avatars.githubusercontent.com/u/76162892?v=4"
                },
                "title": header,
                "description": desc,
                "footer": {"text": footer +"\n© github.com/Blcksoda "}
            }
        ]
    }

    data = embed
elif choice == '2':
    username = input(">> What should be the Username?:\n")
    message = input(">> What should be the message?:\n")

    msg = {

        "author": {
            "name": username,
            "url": "https://github.com/Blcksoda",
            "icon_url": "https://avatars.githubusercontent.com/u/76162892?v=4"
        },
        "content": message

    }
    data = msg
else:
    print(Fore.RED+ ">> Please select a valid input")
    exit(420.69)


webhook = input(Fore.RED +">> Please enter the Webhook:\n")

os.system(clearcmd)

loop = input(Fore.RED+">> Select an Amount of webhooks to be send:\n" )

headers = {
    "Content-Type": "application/json"
}

i = 0
def send(i):
    res = requests.post(webhook, json=data) # sends data to webhook
    try:
        print(Fore.RED + 'Ratelimit of: ' + Fore.WHITE +  str(res.json()["retry_after"]) + ' 1ms.')
        time.sleep(res.json()["retry_after"]/1000)
        res = 'Waited: ' + Fore.RED + str(res.json()["retry_after"]) + ' ms.'
        print(res)
    except:
        i += 1
        res = Fore.YELLOW + "Webhook " + Fore.WHITE +  str(i) + " of " + loop + " sent."
        print(res)
    return i

while i < int(loop):
   i = send(i)