from colorama import Fore, init
import colorama
import random
import requests
import time
import sys
import json
import os
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from pypresence import Presence 
table = PrettyTable()
table.field_names = ["Key", "Value"]
init(convert=True)
class stat():

    valid = 0
    invalid = 0
    proxy_rate = 0
    

def printt(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.009)
try:            
    with open("config.json") as config:
        data = json.load(config)
        numb = data["numbers"]
        lng = data["user_length"]
        menu = data["menu"]
        cooldown = data["cooldown"]
        checker = data["checker"]
        rcp = data["RCP"]
except:
    print(Fore.LIGHTRED_EX + "")
    printt("\nCannot Open config.json File!")
    time.sleep(2)
    exit()
    

if rcp == True:
    RPC = Presence("1002246872477466756")
    RPC.connect()
    print("RCP conected!")
    start = time.time()
    RPC.update(
                large_image = "1658612291010", #name of your asset
                large_text = "Triple_A#2644",
                details = "Triple_A#2644 Username Gen",
                state = f"Main Menu",
                start = start,
            )

if checker == True:
    try:
        with open("usernames.txt") as file:
            file.close()
    except:
        print(Fore.LIGHTRED_EX + "")
        printt("\nCannot Open usernames.txt File!")
        time.sleep(2)
        exit()
        
        
text = """ _______ _____  _____ _____  _      ______          
|__   __|  __ \|_   _|  __ \| |    |  ____|   /\    
   | |  | |__) | | | | |__) | |    | |__     /  \   
   | |  |  _  /  | | |  ___/| |    |  __|   / /\ \  
   | |  | | \ \ _| |_| |    | |____| |____ / ____ \ 
   |_|  |_|  \_\_____|_|    |______|______/_/    \_\ """
   
bad_colors = ['BLACK', 'WHITE',  'RESET', 'BLUE', 'GREEN', 'RED', 'YELLOW',]
codes = vars(colorama.Fore)
colors = list(codes[color] for color in codes if color not in bad_colors)
colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))

time.sleep(2)
if menu == True:
    print(Fore.LIGHTBLUE_EX + "")
    printt(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    printt(">>>>>>>>>>>>>>>>>>>>>>> Triple_A Valid Username Gen <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    printt(">>>>>>>>>>>>>>>>>>>>>>>         1 = Roblox          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    printt(">>>>>>>>>>>>>>>>>>>>>>>         2 = Twitch          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    printt(">>>>>>>>>>>>>>>>>>>>>>>         3 = Github          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    printt(">>>>>>>>>>>>>>>>>>>>>>>         4 = Minecraft       <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    printt(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
else:
    print(Fore.LIGHTBLUE_EX + "")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>>>>>>>> Triple_A Valid Username Gen <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>>>>>>>>         1 = Roblox          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>>>>>>>>         2 = Twitch          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>>>>>>>>         3 = Github          <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>>>>>>>>         4 = Minecraft       <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    

time.sleep(1)
num1 = int(input("\nWhat Do u select?: "))

time.sleep(1)

print(Fore.LIGHTYELLOW_EX + "")
num = int(input("How many nicknames do u want to gen?: "))
time.sleep(1)

#gen a randon number for the file name
rn = random.randint(2,1000)


#check the txt with the proxies
try:
    with open("proxy.txt") as f:
        lineas = f.readlines()
        print(Fore.MAGENTA + "")
        printt(f"Imported {len(lineas)} proxies\n")
except:
    print(Fore.LIGHTRED_EX + "")
    printt("\nCannot Open proxy.txt File!")
    time.sleep(2)
    exit()
    
    
     
letters = [
                'a', 'e', 'i', 'o', 'u',
                'b', 'c', 'd', 'f', 'g',
                'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'q', 'r', 's',
                't', 'v', 'w', 'x', 'z'
                ]
if numb == True:
    i = 0
    for c in range(10):
        g = str(i)
        letters.append(g)
        i += 1


L = lng
time.sleep(2)
valid = []
start = int(time.time())
#roblox
if num1 == 1:
    print(Fore.LIGHTCYAN_EX + "")
    printt("Before Start Remember that could be false positives if the username contain: 69, fuk, fuck...")
    time.sleep(1)


    def Rcheck():
        os.system(f'title Roblox username Gen ^| Valid - {stat.valid} ^| Invalid - {stat.invalid} ^| Proxy Rate Limited - {stat.proxy_rate}')
        with open("proxy.txt") as f:
            lineas = f.readlines()
            proxy = random.choice(lineas)
            proxies = {
            'http': f'http://{proxy}',
            'https':f'http://{proxy}'
                        }
        if checker == True:
            f = open("usernames.txt", "r")
            line = f.readlines()
            username = random.choice(line)
        else:  
            username = "".join(random.choices(letters,k = L))
        print(Fore.MAGENTA + f"\nChecking Username : {username} | With proxy : {proxy}\n")
        url = f"https://api.roblox.com/users/get-by-username?username={username}"
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
                print(f"""{Fore.CYAN}Username Taken: 
                            {Fore.LIGHTYELLOW_EX}Username: {user}
                            Id : {id}
                            Online : {onf}
                            AvatarFinal : {av}{Fore.RESET}""")
                stat.invalid += 1
        elif r.status_code == 429:
                print(Fore.LIGHTYELLOW_EX + "")
                printt("Proxy Rate Limited!!\n")
                stat.proxy_rate += 1
                time.sleep(cooldown)
        else:
                print(Fore.LIGHTGREEN_EX + "Username its avaible" + Fore.RESET)
                valid.append(f"{username}\n")
                print("[ + ]    Name saved")
                stat.valid += 1
        if rcp == True:
            vl = stat.valid
            inv = stat.invalid
            RPC.update(
                large_image = "1658612291010", #name of your asset
                large_text = "Triple_A#0026",
                details = "Roblox Username Gen",
                state = f"Valid - {vl} | Invalid - {inv}",
                start = start,
            )
    for i in range(num):
        Rcheck()
    z = "".join(valid)
    if z == (""):
        print(Fore.LIGHTRED_EX + "")
        printt("You didnt gen any valid name!!")
    else:
        if checker == False:
            with open(f"RValidNames{rn}.txt", "w")as file:
                file.write(z)
            print(Fore.LIGHTGREEN_EX + "")
            printt(f"Valid Names saved in RValidUsernames{rn}.txt File!")
    
    
#twitch
elif num1 == 2:
    valid = []
    def Tcheck():
        os.system(f'title Roblox username Gen ^| Valid - {stat.valid} ^| Invalid - {stat.invalid} ^| Proxy Rate Limited - {stat.proxy_rate}')
        with open("proxy.txt") as f:
                    lineas = f.readlines()
                    proxy = random.choice(lineas)
                    proxies = {
        'http': f'http://{proxy}',
        'https':f'http://{proxy}'
        }
        if checker == True:
            f = open("usernames.txt", "r")
            line = f.readlines()
            username = random.choice(line)
        else:  
            username = "".join(random.choices(letters,k = L))
        print(Fore.MAGENTA + f"Now checking: {username} | With proxy: {proxy}\n")
        try:
            r = requests.head(f"https://passport.twitch.tv/usernames/{username}",
                        headers={'Connection':'close'}, proxies=proxies, timeout=30)
        except:
            print(Fore.LIGHTYELLOW_EX + "Cannot Connect with the proxy!")
            r = requests.head(f"https://passport.twitch.tv/usernames/{username}",
                        headers={'Connection':'close'})
        if r.status_code == 200:
            print(Fore.RED + "Username its not Avaible\n" + Fore.RESET)
            stat.invalid += 1
        
        elif r.status_code == 429:
            print(Fore.LIGHTYELLOW_EX + "")
            printt("Proxy Rate Limited!!\n")
            stat.proxy_rate += 1
            time.sleep(cooldown)
        else:
            rn1 = "".join(random.choices(letters,k = 12))
            url=f'https://www.twitch.tv/{rn1}'
            response = requests.get(url, proxies=proxies, timeout=30)
            soup = BeautifulSoup(response.text, 'html.parser')
            ur = f"https://www.twitch.tv/{username}"
            response2 = requests.get(ur, proxies=proxies, timeout=30)
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            if soup == soup2:
                print(Fore.LIGHTGREEN_EX + "Username its avaible\n" + Fore.RESET)
                valid.append(f"{username}\n")
                print("[ + ]    Username Saved")
                stat.valid += 1
            else:
                print(f"\n{Fore.LIGHTRED_EX}The {username} account is disabled.{Fore.RESET}\n")
        if rcp == True:
            vl = stat.valid
            inv = stat.invalid
            RPC.update(
            large_image = "1658612291010", #name of your asset
            large_text = "Triple_A#0026",
            details = "Twitch Valid Username Gen",
            state = f"Valid - {vl} | Invalid - {inv}",
            start = start,
        )
            
    for i in range(num):
        Tcheck()
        
    a = "".join(valid)
    
    if a == "":
        print(Fore.LIGHTRED_EX + "")
        printt("You didnt gen any valid username!!")
    else:
        if checker == False:
            with open(f"TValidUsernames{rn}.txt", "w") as f:
                f.write(a)
            print(Fore.LIGHTGREEN_EX + "")
            printt(f"Names Saved in TValidUsernames{rn}.txt")
        
#github
elif num1 == 3:
    def Gcheck():
        os.system(f'title Roblox username Gen ^| Valid - {stat.valid} ^| Invalid - {stat.invalid} ^| Proxy Rate Limited - {stat.proxy_rate}')
        with open("proxy.txt") as f:
                    lineas = f.readlines()
                    proxy = random.choice(lineas)
                    proxies = {
        'http': f'http://{proxy}',
        'https':f'http://{proxy}'
        }
        if checker == True:
            f = open("usernames.txt", "r")
            line = f.readlines()
            username = random.choice(line)
        else:  
            username = "".join(random.choices(letters,k = L))
        print(Fore.MAGENTA + f"Now checking: {username} | With proxy: {proxy}\n")
        url = f"https://api.github.com/users/{username}"
        try:
            r = requests.get(url, proxies=proxies, timeout=5)
        except:
            print(Fore.LIGHTYELLOW_EX + "Cannot Connect with the proxy!")
            r = requests.get(url)
        data = r.json()
        print(r)
        if r.status_code == 404:
            print(Fore.LIGHTGREEN_EX + "Username its avaible\n" + Fore.RESET)
            valid.append(f"{username}\n")
            print("[ + ]    Username Saved")
            stat.valid += 1
        
        elif r.status_code == 429:
            print(Fore.LIGHTYELLOW_EX + "")
            printt("Proxy Rate Limited!!\n")
            stat.proxy_rate += 1
            time.sleep(cooldown)
        
        else:
            #I skidded it from here (https://www.techgeekbuzz.com/blog/how-to-use-github-api-in-python/) ngl (the table, not if the username its avaible xd)
            table = PrettyTable()
            table.field_names = ["Key", "Value"]

            for key, value in data.items():
                table.add_row([key, value])
            print(Fore.LIGHTYELLOW_EX + "")
            print(f"{table}")
            stat.invalid += 1
        if rcp == True:
            vl = stat.valid
            inv = stat.invalid
            RPC.update(
                large_image = "1658612291010", #name of your asset
                large_text = "Triple_A#0026",
                details = "Github Username Gen",
                state = f"Valid - {vl} | Invalid - {inv}",
                start = start,
            )
    
    for i in range(num):     
        Gcheck()
    a = "".join(valid)
    
    if a == "":
        print(Fore.LIGHTRED_EX + "")
        printt("You didnt gen any valid username!!")
    else:
        if checker == False:
            with open(f"GValidUsernames{rn}.txt", "w") as f:
                f.write(a)
            print(Fore.LIGHTGREEN_EX + "")
            printt(f"Names Saved in GValidUsernames{rn}.txt")
            
#minecraft
elif num1 == 4:
    def Mcheck():
        os.system(f'title Minecraft username Gen ^| Valid - {stat.valid} ^| Invalid - {stat.invalid} ^| Proxy Rate Limited - {stat.proxy_rate}')
        with open("proxy.txt") as f:
                    lineas = f.readlines()
                    proxy = random.choice(lineas)
                    proxies = {
        'http': f'http://{proxy}',
        'https':f'http://{proxy}'
        }
                    
        if checker == True:
            f = open("usernames.txt", "r")
            line = f.readlines()
            username = random.choice(line)
            
        else:  
            username = "".join(random.choices(letters,k = L))
            
        url = f"https://api.mojang.com/users/profiles/minecraft/{username}?at=0"
        
        
            
        print(Fore.MAGENTA + f"Now checking: {username} | With proxy: {proxy}\n")
        
        try:
            r = requests.get(url, proxies=proxies, timeout=5)
        except:
            print(Fore.LIGHTYELLOW_EX + "Cannot Connect with the proxy!")
            r = requests.get(url)
            
            
        if r.text.__contains__("id"):
            a = r.json()["id"]
            print(f"{Fore.LIGHTRED_EX}Username Taken, {Fore.LIGHTYELLOW_EX}UUID: {Fore.LIGHTBLUE_EX}{a}\n{Fore.RESET}")
            stat.invalid += 1
            
            
        elif r.status_code == 429:
            print(Fore.LIGHTYELLOW_EX + "")
            printt("Proxy Rate Limited!!\n")
            stat.proxy_rate += 1
            time.sleep(cooldown)
            
            
        else:
            print(Fore.GREEN + "Username its Avaible\n" + Fore.RESET)
            valid.append(f"{username}\n")
            print("[ + ]    Username Saved")
            stat.valid += 1
        if rcp == True:
            vl = stat.valid
            inv = stat.invalid
            RPC.update(
                large_image = "1658612291010", #name of your asset
                large_text = "Triple_A#0026",
                details = "Minecraft Username Gen",
                state = f"Valid - {vl} | Invalid - {inv}",
                start = start,
            )
    
    for i in range(num):     
        Mcheck()
    a = "".join(valid)
    
    if a == "":
        print(Fore.LIGHTRED_EX + "")
        printt("You didnt gen any valid username!!")
    else:
        if checker == False:
            with open(f"GValidUsernames{rn}.txt", "w") as f:
                f.write(a)
            print(Fore.LIGHTGREEN_EX + "")
            printt(f"Names Saved in GValidUsernames{rn}.txt")

            

print(Fore.LIGHTYELLOW_EX + "")
input("Press Enter For Exit...")
