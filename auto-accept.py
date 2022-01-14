# Free Tool, By Lynch AKA Null
try:
    import requests
    import time
    import uuid
    import json
    import os
    from os import system
    system("title " + "Programmed By Lynch - Instagram Auto Accept")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()

logo = """
  _                     _     
 | |   _   _ _ __   ___| |__  
 | |  | | | | '_ \ / __| '_ \ 
 | |__| |_| | | | | (__| | | |
 |_____\__, |_| |_|\___|_| |_|
       |___/                                    
"""

print(Fore.CYAN+logo)
title = ("Made w Love By Lynch, [i]: @l7up")
print(Fore.RED+title)                              
username = str(input(f"[{Fore.GREEN}?{Fore.RESET}] Username: "))
password = str(input(f"[{Fore.GREEN}?{Fore.RESET}] Password: "))
slee = int(input(f"[{Fore.GREEN}?{Fore.RESET}] Sleep: "))
uid = str(uuid.uuid4())
cok = ""
hh = ""
hd_login = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com'
}
checked = 0
acceptdone = 0
unaccepted = 0


def get_challenge_choices(last_json):
    choices = []

    if last_json.get("step_name", "") == "select_verify_method":
        choices.append("Challenge received")
        if "phone_number" in last_json["step_data"]:
            choices.append("0 - Phone")
        if "email" in last_json["step_data"]:
            choices.append("1 - Email")

    if last_json.get("step_name", "") == "delta_login_review":
        choices.append("Login attempt challenge received")
        choices.append("0 - It was me")
        choices.append("0 - It wasn't me")

    if not choices:
        choices.append(
            '"{}" challenge received'.format(last_json.get("step_name", "Unknown"))
        )
        choices.append("0 - Default")

    return choices


def challange(login_json):
    global cok, hh
    challenge_url = 'https://i.instagram.com/api/v1/' + login_json["challenge"]["api_path"][1:]
    try:
        b = requests.get(challenge_url, headers=hd_login, cookies=cok)
    except Exception as e:
        print("solve_challenge; {}".format(e))
        return False
    choiccc = get_challenge_choices(b.json())
    for choice in choiccc:
        print(choice)
    code = input(f"[{Fore.GREEN}?{Fore.RESET}] Insert Choice : ")
    data_c = {
        'choice': code,
        '_uuid': uid,
        '_uid': uid,
        '_csrftoken': 'missing'
    }
    send_c = requests.post(challenge_url, data=data_c, headers=hd_login, cookies=cok)
    print("We've Sent Code To {}, Please Check And Enter It.".format(send_c.json()['step_data']['contact_point']))
    code = input(f"\n[{Fore.GREEN}?{Fore.RESET}] Code You Have Got (On-Email): ").strip()
    data_co = {
        'security_code': code,
        '_uuid': uid,
        '_uid': uid,
        '_csrftoken': 'missing'
    }
    send_o = requests.post(challenge_url, data=data_co, headers=hd_login, cookies=cok)
    send_coj = send_o.json()
    if 'logged_in_user' in send_coj:
        print(f"\n[{Fore.GREEN}L{Fore.RESET}] We've Successfully Logged > @{username}")
        hh = send_o.cookies
        if 'is_private":false,' in send_o.text:
            print(f"[{Fore.RED}-{Fore.RESET}] Account Isn't Private, We'll Set It..")
            private()
        ggtt()
        return True
    return False


def login_api():
    global hd_login, cok, hh
    login_url = "https://i.instagram.com/api/v1/accounts/login/"
    data_login = {'uuid': uid,
                  'password': password,
                  'username': username,
                  'device_id': uid,
                  'from_reg': 'false',
                  '_csrftoken': 'missing',
                  'login_attempt_count': '0'}
    loginc = requests.post(login_url, data=data_login, headers=hd_login)
    login1 = loginc.text
    if '"logged_in_user"' in login1:
        print(f"\n[{Fore.GREEN}L{Fore.RESET}] We've Logged Into / @{username}")
        hh = loginc.cookies
        if 'is_private":false,' in login1:
            print(f"[{Fore.GREEN}-{Fore.RESET}] Account Isn't Private, We'll Set It..")
            private()

        ggtt()
    elif "Hm, Seems Like Username You've Entered Does't Belong To Anyone" in login1:
        print(f"\n[{Fore.RED}-{Fore.RESET}] You've Entered Wrong Username - @{username}")
        time.sleep(3)
        exit()
    elif "Hm, Seems Like Password You've Entered Is Incorrect" in login1:
        print(f"\n[{Fore.RED}-{Fore.RESET}] You've Entered Wrong Password - @{username}")
        time.sleep(3)
        exit()
    elif '"Hm, Seems Like Username Youve Entered Is Disabled"' in login1:
        print(f"\n[{Fore.RED}-{Fore.RESET}] You've Entered Disabled Account - @{username}")
        time.sleep(3)
        exit()
    elif "checkpoint_challenge_required" in login1:
        cok = loginc.cookies
        return challange(loginc.json())
    elif 'two_factor_required":true,':
        print(f"\n[{Fore.RED}!{Fore.RESET}] You Mustn't Have 2 Factor Enabled, Turn It Off Then Try Again - @{username}")
        time.sleep(3)
        exit()


def private():
    global hd_login, hh
    url = "https://i.instagram.com/api/v1/accounts/set_private/"
    data = {
        "is_private": "true"
    }
    see = requests.post(url, data=data, headers=hd_login, cookies=hh)
    if 'is_private":true,' in see.text:
        print(f"[{Fore.GREEN}+{Fore.RESET}] Done, Setting Account To Private")
        grabid()
    else:
        print(f"\n[{Fore.RED}-{Fore.RESET}] We've Got A Problem, While Setting Account To Private")
        print(see.text)


def grabid():
    global hd_login, hh, acceptdone, checked, unaccepted
    url = "https://i.instagram.com/api/v1/friendships/pending/?rank_mutual=0"
    ree = requests.get(url, headers=hd_login, cookies=hh)
    if 'users":[],' in ree.text:
        time.sleep(4)
        ggtt()
    else:
        checked += 1
        jj = json.loads(ree.text)
        userr = jj["users"][0]["username"]
        idd = jj["users"][0]["pk"]
        acceptuser(userr, idd)


def acceptuser(userr, idd):
    global hd_login, hh, checked, unaccepted, acceptdone
    url = f"https://i.instagram.com/api/v1/friendships/approve/{idd}/"
    acce = requests.post(url, headers=hd_login, cookies=hh)
    if 'status":"ok' in acce.text:
        acceptdone += 1
        print(f"[{Fore.GREEN}+{Fore.RESET}] We've Accepted: @{userr} \nDone: [{acceptdone}] Error: [{unaccepted}]")
    else:
        unaccepted += 1
        print(f"[{Fore.GREEN}-{Fore.RESET}] Error: [{unaccepted}] \nDone: [{acceptdone}] Accepted: @{userr}")


def ggtt():
    while 1:
        grabid()
        time.sleep(slee)


login_api()
