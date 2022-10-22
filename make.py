#!/usr/bin/python3
import distro
import os
import time
from random import choice


try:
    from art import *
    from colorama import Fore, Style
except:
    STYLE = '\033[33m[\033[31m!\033[33m]\033[00m'
    print(STYLE+'\033[31m error : python \033[33mmodules\033[31m missing '+STYLE)
    print(STYLE+'\033[31m run : \033[33mpip3 install -r requirements.txt\033[00m '+STYLE)
    exit()


#VARIABLES

#COLORS

N = Style.RESET_ALL
R = Fore.RED
C = Fore.CYAN
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE


#Downloading required files
os.system('wget https://raw.githubusercontent.com/whoami-anoint/Probe/main/script/download.sh')
os.system('chmod +x download.sh')
os.system('bash download.sh')
os.system('rm download.sh')


#Directory variables
HOME_DIR = '/home'+'/'+os.listdir('/home')[0]+'/' #Go to home


DIR = '.probe' # Using a hidden directory to store all the required scripts
PROBE_PATH = os.path.join(HOME_DIR, DIR) #creating a path to make a directory
#File exists or not


BIN_CHECK = False  #True means found in /bin and False means not found in /bin
GOBIN_CHECK = False #True means found in ~/go/bin and False means not found in ~/go/bin

#Banner

color = [N,R,C,G,Y,B]
arts = ['avatar','bigfig','chunky','contessa','cyberlarge',\
    'cybermedium','cybersmall','italic','larry3d','lean','pepper','standard','straight','sub-zero','']
print(choice(color)+text2art('Probe',font=choice(arts)))
print(C+'.:.Everything you need as a'+Y+' Bug'+C+' hunter.:.'+N)
print('-------------------------------------------\n'*2)
time.sleep(.5)


#Linux Distro check; [Arch, Debian etc....]

DISTRO = distro.id()
print('['+G+'+'+N+'] Distro '+Y+DISTRO+N+' detected...'+N)
print('['+Y+'+'+N+'] Setting up '+Y+DISTRO+N+' package manager...')
time.sleep(0.5)



#Setting up package manager and GO package because installer is different

if 'arch' in DISTRO:
    PKG_MNGR = 'yay -s'
    GO = 'go'
else :
    PKG_MNGR = 'sudo apt install '
    GO = 'golang'
print('['+G+'+'+N+'] Package manager '+G+'setup'+N+' completed...')
time.sleep(.5)

#BSIC package checkups;

print('['+Y+'+'+N+'] Initilized '+Y+'Golang'+N+' check up ...')
time.sleep(.5)

#Golang check

if  os.path.exists('/bin/go'):
    print('['+G+'+'+N+'] Package already satisfied ...')
    print(Y+'Skipping '+C+' Golang'+Y+' installation ....'+N)
    time.sleep(.5)
else:
    print('['+Y+'!'+N+'] Package missing ...')
    print(Y+'Started '+C+' Golang'+Y+' installation ....')
    os.system(PKG_MNGR +' '+GO)
    print(G+'Golang installation completed ....'+N)
print('---------------------------------------------')

#Nmap check

print('['+Y+'+'+N+'] Initilized '+Y+'nmap'+N+' check up ...')
time.sleep(.5)
if os.path.exists('/bin/nmap'):
    print('['+G+'+'+N+'] Package already satisfied ...')
    print(Y+'Skipping '+C+' nmap'+Y+' installation ....'+N)
    time.sleep(.5)
else:
    print('['+Y+'!'+N+'] Package missing ...')
    print(Y+'Started '+C+' Nmap'+Y+' installation ....')
    os.system(PKG_MNGR + ' nmap')
    print(G+'Nmap installation completed ....'+N)
print('---------------------------------------------')

if os.path.exists('/bin/pv'):
    pass
else:
    os.system(PKG_MNGR+' pv')
#Subfinder check

print('['+Y+'+'+N+'] Initilized '+Y+'subfinder'+N+' check up ...')
time.sleep(.5)
BIN_CHECK =  os.path.exists('/bin/subfinder') #False means not found , True means found
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/subfinder') # False means not found , True means found
    if  GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/subfinder /bin')
    else:
        print('['+Y+'!'+N+'] Package missing ...')
        print(Y+'Started '+C+' Subfinder'+Y+' installation ....')
        os.system('go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest')
        os.system(f'sudo mv {HOME_DIR}go/bin/subfinder /bin')
        print(G+'subfinder installation completed ....'+N)
else :
    print('['+G+'+'+N+'] Package already satisfied ...')
    print(Y+'Skipping '+C+' subfinder'+Y+' installation ....'+N)
    time.sleep(.5)
print('---------------------------------------------')


#Amasss check
print('['+Y+'+'+N+'] Initilized '+Y+'Amass'+N+' check up ...')
time.sleep(.5)
BIN_CHECK = os.path.exists('/bin/amass')
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/amass') # False means not found , True means found
    if GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/amass /bin') # {HOME_DIR}go/bin/amass -> ~/go/bin/amass
    else:
        print('['+Y+'!'+N+'] Package missing ...')
        print(Y+'Started '+C+' Amass'+Y+' installation ....')
        os.system('go install -v github.com/OWASP/Amass/v3/...@master')
        os.system(f'sudo mv {HOME_DIR}go/bin/amass /bin')
        print(G+'amass installation completed ....'+N)
else:
    print('['+G+'+'+N+'] Package already satisfied ...')
    print(Y+'Skipping '+C+' Amass'+Y+' installation ....'+N)
    time.sleep(.5)
print('---------------------------------------------')


#HTTPX check
print('['+Y+'+'+N+'] Initilized '+Y+'Httpx'+N+' check up ...')
time.sleep(.5)
BIN_CHECK = os.path.exists('/bin/httpx')
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/httpx') # False means not found , True means found
    if GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/httpx /bin')
    else:
        print('['+Y+'!'+N+'] Package missing ...')
        print(Y+'Started '+C+' Httpx'+Y+' installation ....')
        os.system('go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest')
        os.system(f'sudo mv {HOME_DIR}go/bin/httpx /bin')
        print(G+'httpx installation completed ....'+N)
else:
    print('['+G+'+'+N+'] Package already satisfied ...')
    print(Y+'Skipping '+C+' HTTPX'+Y+' installation ....'+N)
    time.sleep(.5)
print('---------------------------------------------')




#Waybackurls check
print('['+Y+'+'+N+'] Initilized '+Y+'waybackruls'+N+' check up ...')
time.sleep(.5)
BIN_CHECK = os.path.exists('/bin/waybackurls')
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/waybackurls') # False means not found , True means found
    if GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/waybackurls /bin')
    else:
        print('['+Y+'!'+N+'] Package missing ...')
        print(Y+'Started '+C+' Waybackurls'+Y+' installation ....')
        os.system('go install github.com/tomnomnom/waybackurls@latest')
        os.system(f'sudo mv {HOME_DIR}go/bin/waybackurls /bin')
        print(G+'waybackurls installation completed ....'+N)
else:
    print('['+G+'+'+N+'] Package already satisfied ...')
    print(Y+'Skipping '+C+' WayBackUrls'+Y+' installation ....'+N)
    time.sleep(.5)
print('---------------------------------------------')

BIN_CHECK = os.path.exists('/bin/gf')
if not BIN_CHECK:
    os.system('chmod +x ~/.probe/script/gf.sh')
    os.system('bash ~/.probe/script/gf.sh')
else:
    pass

check = input('Enable notification [y/n]: ')
if str(check) == 'y' or str(check) =='Y' or  str(check) == 'yes' or str(check) == 'Yes':
    os.system('python3 ~/.probe/script/configNotification.py')
else:
    pass

print('Hold on a second compiling the requirements of probe....')
time.sleep(1)
os.system('echo "Installation completed...." | pv -qL 20')
time.sleep(.5)
print(C+'>.<    .:.Welcome to Probe.:.    >.<')
