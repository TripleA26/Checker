from colorama import Fore, init
import colorama
import random
import requests
import time
import sys
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Key", "Value"]
init(convert=True)
              


def printt(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.7 / 50000)
        
        
text = """                                                                                                _______ _____  _____ _____  _      ______          
                                                                                               |__   __|  __ \|_   _|  __ \| |    |  ____|   /\    
                                                                                                  | |  | |__) | | | | |__) | |    | |__     /  \   
                                                                                                  | |  |  _  /  | | |  ___/| |    |  __|   / /\ \  
                                                                                                  | |  | | \ \ _| |_| |    | |____| |____ / ____ \ 
                                                                                                  |_|  |_|  \_\_____|_|    |______|______/_/    \_\ """
   
bad_colors = ['BLACK', 'WHITE',  'RESET', 'BLUE', 'GREEN', 'RED', 'YELLOW',]

codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))

time.sleep(2)


print(Fore.LIGHTBLUE_EX + "")
printt("                                                                                 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
printt("                                                                                 >>>>>>>>>>>>>>>>>>>>>>> Triple_A Valid Username Gen <<<<<<<<<<<<<<<<<<<<<<<<<<<")
printt("                                                                                 >>>>>>>>>>>>>>>>>>>>>>>         1 = Roblox          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
printt("                                                                                 >>>>>>>>>>>>>>>>>>>>>>>         2 = Twitch          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
printt("                                                                                 >>>>>>>>>>>>>>>>>>>>>>>         3 = Github          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
printt("                                                                                 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

time.sleep(1)
num1 = int(input("\n                                                                                 What Do u select?: "))

time.sleep(1)

print(Fore.LIGHTYELLOW_EX + "")
num = int(input("                                                                                 How many nicknames do u want to gen?: "))
time.sleep(1)

#gen a randon number for the file name
rn = random.randint(2,1000)


#check the txt with the proxies
try:
    with open("proxy.txt") as f:
        lineas = f.readlines()
        print(Fore.MAGENTA + "")
        printt(f"                                                                                 Imported {len(lineas)} proxies\n")
except:
    print(Fore.LIGHTRED_EX + "")
    printt("\n                                                                                 Cannot Open proxy.txt File!")
    time.sleep(2)
    exit()
    

letters = [
            'a', 'e', 'i', 'o', 'u',
            'b', 'c', 'd', 'f', 'g',
            'h', 'j', 'k', 'l', 'm',
            'n', 'p', 'q', 'r', 's',
            't', 'v', 'w', 'x', 'z',
            '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0',
            ]
MIN_LEN = 4
MAX_LEN = 4


L = random.randint(MIN_LEN, MAX_LEN)
time.sleep(2)
valid = []

#roblox
if num1 == 1:
    print(Fore.LIGHTCYAN_EX + "")
    printt("                                                                                 Before Start Remember that could be false positives if the username contain: 69, fuk, fuck...")
    time.sleep(1)


    def Rcheck():
        with open("proxy.txt") as f:
            lineas = f.readlines()
            proxy = random.choice(lineas)
            proxies = {
            'http': f'http://{proxy}',
            'https':f'http://{proxy}'
                        }
        nickname = "".join(random.choices(letters,k = L))
        print(Fore.MAGENTA + f"\n                                                                                 Checking Username : {nickname} | With proxy : {proxy}\n")
        url = f"https://api.roblox.com/users/get-by-username?username={nickname}"
        try:
            r = requests.get(url, proxies=proxies, timeout=5)
        except:
            print(Fore.MAGENTA + "Cannot Connect with the proxy!")
            r = requests.get(url)
        if r.text.__contains__('Id'):
                id = r.json()["Id"]
                onf = r.json()["IsOnline"]
                user = r.json()["Username"]
                av = r.json()["AvatarFinal"]
                print(f"""{Fore.CYAN}                                                                                 Username Taken: 
                            {Fore.LIGHTYELLOW_EX}                                                                                 Username: {user}
                                                                                                             Id : {id}
                                                                                                             Online : {onf}
                                                                                                             AvatarFinal : {av}{Fore.RESET}""")
        elif r.status_code == 429:
                print(Fore.LIGHTYELLOW_EX + "")
                printt("                                                                                 Proxy Rate Limited!!\n")
                time.sleep(15)
        else:
                valid.append(f"{nickname}\n")
                print(Fore.LIGHTGREEN_EX + "                                                                                 Username its avaible" + Fore.RESET)
                print("                                                                                  [ + ]    Name saved")
    z = "".join(valid)
    for i in range(num):
        Rcheck()
    if z == (""):
        print(Fore.LIGHTRED_EX + "")
        printt("                                                                                 You didnt gen any valid name!!")
    else:
        with open(f"ValidNames{rn}.txt", "w")as file:
            print(Fore.LIGHTGREEN_EX + "")
            file.write(z)
            print(Fore.LIGHTGREEN_EX + "")
            printt(f"                                                                                 Valid Names saved in RValidUsernames{rn}.txt File!")
    
    
#twitch
elif num1 == 2:
    valid = []
    def Tcheck():
        with open("proxy.txt") as f:
                    lineas = f.readlines()
                    proxy = random.choice(lineas)
                    proxies = {
        'http': f'http://{proxy}',
        'https':f'http://{proxy}'
        }
        username = "".join(random.choices(letters, k = L ))
        print(Fore.MAGENTA + f"                                                                                 Now checking: {username} | With proxy: {proxy}\n")
        try:
            r = requests.head(f"https://passport.twitch.tv/usernames/{username}",
                        headers={'Connection':'close'}, proxies=proxies, timeout=5)
        except:
            print(Fore.YELLOW + "                                                                                 Cannot Connect with the proxy!")
            r = requests.head(f"https://passport.twitch.tv/usernames/{username}",
                        headers={'Connection':'close'})
        if r.status_code == 200:
            print(Fore.RED + "                                                                                 Username its not Avaible\n" + Fore.RESET)
        
        elif r.status_code == 429:
            print(Fore.LIGHTYELLOW_EX + "")
            printt("                                                                                 Proxy Rate Limited!!\n")
            time.sleep(15)
        else:
            print(Fore.LIGHTGREEN_EX + "                                                                                 Username its avaible\n" + Fore.RESET)
            valid.append(f"{username}\n")
            print("                                                                                 [ + ]    Username Saved")
            
    for i in range(num):
        Tcheck()
        
    a = "".join(valid)
    
    if a == "":
        print(Fore.LIGHTRED_EX + "")
        printt("                                                                                 You didnt gen any valid username!!")
    else:
        with open(f"TValidUsernames{rn}.txt", "w") as f:
            f.write(a)
        print(Fore.LIGHTGREEN_EX + "")
        printt(f"                                                                                 Names Saved in TValidUsernames{rn}.txt")
        
#github
elif num1 == 3:
    def Gcheck():
        with open("proxy.txt") as f:
                    lineas = f.readlines()
                    proxy = random.choice(lineas)
                    proxies = {
        'http': f'http://{proxy}',
        'https':f'http://{proxy}'
        }
        username = "".join(random.choices(letters, k = L ))
        print(Fore.MAGENTA + f"                                                                                 Now checking: {username} | With proxy: {proxy}\n")
        url = f"https://api.github.com/users/{username}"
        try:
            r = requests.get(url, proxies=proxies, timeout=5)
        except:
            print(Fore.YELLOW + "Cannot Connect with the proxy!")
            r = requests.get(url)
        data = r.json()
        print(r)
        if r.status_code == 404:
            print(Fore.LIGHTGREEN_EX + "                                                                                 Username its avaible\n" + Fore.RESET)
            valid.append(f"{username}\n")
            print("                                                                                 [ + ]    Username Saved")
        
        elif r.status_code == 429:
            print(Fore.LIGHTYELLOW_EX + "")
            printt("                                                                                 Proxy Rate Limited!!\n")
            time.sleep(15)
        
        else:
            #I skidded it from here (https://www.techgeekbuzz.com/blog/how-to-use-github-api-in-python/) ngl (the table, not if the username its avaible xd)
            table = PrettyTable()
            table.field_names = ["Key", "Value"]

            for key, value in data.items():
                table.add_row([key, value])
            print(Fore.LIGHTYELLOW_EX + "")
            print(f"{table}")
    
    for i in range(num):
        Gcheck()
    a = "".join(valid)
    
    if a == "":
        print(Fore.LIGHTRED_EX + "")
        printt("You didnt gen any valid username!!")
    else:
        with open(f"GValidUsernames{rn}.txt", "w") as f:
            f.write(a)
        print(Fore.LIGHTGREEN_EX + "")
        printt(f"                                                                                 Names Saved in GValidUsernames{rn}.txt")
            

print(Fore.LIGHTYELLOW_EX + "")
input("                                                                                 Press Enter For Exit...")