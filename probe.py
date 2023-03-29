#!/usr/bin/python3
import distro
import os
import time
import customtkinter
from art import *
from random import choice
from colorama import Fore, Style, Back
import recon
# Variables use for different purpose

N = Style.RESET_ALL
R = Fore.RED
C = Fore.CYAN
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
Z = Back.RED


# Path to probe directory
path = '/home/'+os.getlogin()+'/probe'
whereami = ''
target = []

color = [N,R,C,G,Y,B]
arts = ['avatar','bigfig','chunky','contessa','cyberlarge',\
    'cybermedium','cybersmall','italic','larry3d','lean','pepper','standard','straight','sub-zero','']


def banner():
    print(choice(color)+text2art('Probe',font=choice(arts)))
    print(C+'.:.Everything you need as a'+Y+' Bug'+C+' hunter.:.'+N)
    print('-------------------------------------------\n'*2)
    time.sleep(.5)

def target():
    domain = command.split('push')[1].split(' ')[1]
    with open(f'project/domains.txt', 'a') as f:
        f.write(domain)


def help():
    pass

def set_target(command):
    data = command.split(' ')
    with open(f'{whereami}/domains.txt', 'w') as f:
        for target in data:
            if target == 'set' or target == 'targets' or target == 'target':
                pass
            else:
                f.write(target+'\n')

def recon_init():
    print(f'{C}.:. Select tools to start recon.:.')
    print(f'{Z}Note default is all...{N}',end="\n\n")
    print(f'{R}[{N}01{R}] {Y}Subdomains  ', end="")
    print(f'{R}[{N}03{R}] {Y}Screenshots ')
    print(f'{R}[{N}04{R}] {Y}Parameters ', end="")
    print(f'{R} [{N}05{R}] {Y}Port scan {N}',)
    print(f'{R}[{N}06{R}] {Y}All {N}',end="")
    print(f'{R}        [{N}00{R}] {Y}Exit {N}',end="\n\n")
    print('Example : 1,2,3 # To run subdomains, Screeenshots, parameters...', end="\n\n")
    cmd_to_run = input(f'{os.getlogin()}@probe-$  use ')
    recon_init_choose(cmd_to_run)

def recon_init_choose(x):
    if x == '1' or x=='01':
        recon.subdomain(whereami)

def projectManager(command):
    global whereami
    pathfinal = command.split('init')[1].split(' ')[1] # Extracting the path
    if '/' in pathfinal:
        if os.path.exists(pathfinal):
            pass
        else:
            os.system(f'mkdir {pathfinal} >/dev/null')
            whereami = pathfinal
    else:
        if os.path.exists(path):
            os.system(f'mkdir {path}/{pathfinal} >/dev/null')
            whereami = path+'/'+pathfinal
        else:
            os.system(f'mkdir {path} >/dev/null')
            if os.path.exists(f'{path}/{pathfinal}'):
                whereami = path+'/'+pathfinal
                pass
            else:
                os.system(f'mkdir {path}/{pathfinal} >/dev/null')

                whereami = path+'/'+pathfinal
    # Expanding path and making project


def command_check(command):
    command = command.lower()
    if 'exit' in command:
        exit(0)
    elif 'banner' in command:
        banner()
    elif 'help' in command:
        help()
    elif 'projectman init' in command:
        projectManager(command)
        print(whereami)
    elif 'recon init' in command:
        recon_init()
    elif 'set target' in command or 'set targets' in command:
        set_target(command)
    else:
        os.system(command)


probe_run = True





# Main function
banner()

while probe_run:
    command = input(f'{os.getlogin()}@probe-$ ')
    command_check(command)
