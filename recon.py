from os import system

def subdomain(target):
    #amass
    system('mkdir recon')
    system(f'amass enum -src -df {target}/domains.txt -o {target}/recon/domain1.txt')
    #Subfinder
    system(f'subfinder -dL {target}/domains.txt| tee -a {target}/recon/domain2.txt')
    #Anubis
    system(f'anubis -f {target}/domains.txt -o {target}/recon/domain3.txt')
    #Alive domains
    system(f'cat {target}/recon/domain1.txt {target}/recon/domain2.txt {target}/recon/domain3.txt  | httpx -status-code| grep 200| cut -d " "| tee -a {target}/recon/aliveDomain.txt')
