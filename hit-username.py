import random , requests ,os 
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = "\033[1;97m" #ابيض
BB = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
ali = """                                                   
       
         (҂`_´)
█۞███████▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙


\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool alosh \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @darkhacker00
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @anamyws
\033[1;31m--------------------------------
 """
AL = (f"""
         (҂`_´)
█۞███████▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙


\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool alosh \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @darkhacker00
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @anamyws
\033[1;31m--------------------------------

{F}⌯ - 1 {BB}=> {X} - ####

{F}⌯ - 2 {BB}=> {X} - #####

{F}⌯ - 3 {BB}=> {X} - ###._
""")
print(AL)
Tools = input(Z+"Choice : \n"+F)
os.system('clear')
print(ali)
tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " Token TeLe"+Z+" :\n"+BB)
ID = input(Z+"["+F+"⌯"+Z+"]"+X+ " ID TeLe"+Z+" :\n"+BB)
os.system('clear')
H=0
B=0
while True:
    if Tools == "1":
        ran = "0987654321poiuytrewqasdfghjklmnvvcxz"
        rang = "".join(random.choice(ran) for I in range(4))
        User = rang
    if Tools == "2":
        ran = "0987654321poiuytrewqasdfghjklmnvvcxz"
        rang = "".join(random.choice(ran) for I in range(5))
        User = rang
    if Tools == "3":
        ran = "0987654321poiuytrewqasdfghjklmnvvcxz"
        rang = "".join(random.choice(ran) for I in range(3))
        rang1 = "".join(random.choice(ran) for I in range(1))
        User = rang+"_"+rang1
    url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
    headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '1176',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
'origin': 'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
'x-asbd-id':'198387' ,
'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
'x-instagram-ajax': '72bda6b1d047',
'x-requested-with': 'XMLHttpRequest'}   
    data = {
'email' : 'a@gmail.com',
'username': (f'{User}'),
'first_name': 'AA',
'opt_into_one_tap': 'false'
}  
    req = requests.post(url,headers=headers,data=data).text
    if ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') in req:        
        H+=1
        For = requests.post(f"""https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=
✅User True : {User}
""")
    else:
        B+=1          
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
         (҂`_´)
█۞███████▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙

\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool alosh \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @darkhacker00
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @anamyws
\033[1;31m--------------------------------

{Z}User : {C}{User}
{E}-------------------------------
{E}({BB}⌯{E}){BB} Bad : {Z}{B}  
{E}({F}⌯{E}){F} Good : {F}{H}
{E}-------------------------------
{X} TeleGarm : {F}@anamyws""")