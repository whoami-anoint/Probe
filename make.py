#!/usr/bin/python3
import distro
import os
os.system('python3 script/art.py')
try:
    from colorama import Fore, Style
except:
    STYLE = '\033[33m[\033[31m!\033[33m]\033[00m'
    print(STYLE+'\033[31m error : python \033[33mmodules\033[31m missing '+STYLE)
    print(STYLE+'\033[31m run : \033[33mpip3 install -r requirements.txt\033[00m '+STYLE)
    exit(2)

#VARIABLES

#COLORS
N = Style.RESET_ALL
R = Fore.RED
C = Fore.CYAN
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.Blue


#Directory variables
HOME_DIR = '/home'+'/'+os.listdir('/home')[0]+'/' #Go to home


DIR = '.probe' # Using a hidden directory to store all the required scripts
PROBE_PATH = os.path.join(HOME_DIR, DIR) #creating a path to make a directory
print(PROBE_PATH)
#File exists or not


BIN_CHECK = False  #True means found in /bin and False means not found in /bin 
GOBIN_CHECK = False #True means found in ~/go/bin and False means not found in ~/go/bin


#Creating a hidden directory to store files.
try :
    os.mkdir(PROBE_PATH) # Created a hidden directory 
except:
    pass


#Copying files to appropriate place
def copy(file,location='',destination=''):
    if location != '':
        os.system(f'cp -r {location}+\'/\'+{file} {destination}')
    else:
        os.system(f' cp -r {file} {destination}')


#Copying script file to its destination
if not os.path.exists(PROBE_PATH+'/script'):
    
    copy(file='script',destination='~/.probe/')
    print('Hello')


#Linux Distro check; [Arch, Debian etc....]
DISTRO = distro.id()
print(CYAN+'['+GREEN+'*'+CYAN+f'] Distro detected {DISTRO}'+NC)
#Setting up package manager and GO package because installer is different
if 'arch' in DISTRO:
    PKG_MNGR = 'yay -s'
    GO = 'go'
else :
    PKG_MNGR = 'sudo apt install '
    G0 = 'golang'


#BSIC package checkups;

#Golang check
if os.path.exists('/bin/go'):
    pass
else:
    os.system(PKG_MNGR +' '+GO)


print('Execuation completed M7')


#Nmap check

if os.path.exists('/bin/nmap'):
    pass
else:
    os.system(PKG_MNGR + ' nmap')

#Subfinder check

BIN_CHECK =  os.path.exists('/bin/subfinder') #False means not found , True means found
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/subfinder') # False means not found , True means found
    if GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/subfinder /bin') # {HOME_DIR}go/bin/subfinder -> ~/go/bin/subfinder
    else:
        os.system('go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest')
        os.system(f'sudo mv {HOME_DIR}go/bin/subfinder /bin')


#Amasss check 

BIN_CHECK = os.path.exists('/bin/amass')
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/amass') # False means not found , True means found
    if GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/amass /bin') # {HOME_DIR}go/bin/amass -> ~/go/bin/amass
    else:
        os.system('go install -v github.com/OWASP/Amass/v3/...@master')
        os.system(f'sudo mv {HOME_DIR}go/bin/amass /bin')


#HTTPX check

BIN_CHECK = os.path.exists('/bin/httpx')
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/httpx') # False means not found , True means found
    if GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/httpx /bin')
    else:
        os.system('go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest')
        os.system(f'sudo mv {HOME_DIR}go/bin/httpx /bin')



#Waybackurls check 
BIN_CHECK = os.path.exists('/bin/waybackurls')
if not BIN_CHECK:
    GOBIN_CHECK = os.path.exists(HOME_DIR+'go/bin/waybackurls') # False means not found , True means found
    if GOBIN_CHECK :
        os.system(f'sudo mv {HOME_DIR}go/bin/waybackurls /bin') 
    else:
        os.system('go install github.com/tomnomnom/waybackurls@latest')
        os.system(f'sudo mv {HOME_DIR}go/bin/waybackurls /bin')


