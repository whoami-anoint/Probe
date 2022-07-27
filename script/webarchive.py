# curl -s "http://web.archive.org/cdx/search/cdx?url=*.$name/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | sort -u | tee WaybackSub.txt
import pycurl 
from io import BytesIO
from os import system as bash
bash('rm /tmp/sub4.txt /tmp/webarchive.txt 2>/tmp/null')


get_body = ''
def curl(target):
    global get_body
    b_obj = BytesIO()
    crl = pycurl.Curl()
    crl.setopt(crl.URL, target)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    get_body = get_body.decode('utf8')


#Target portion
file = '/tmp/targets.txt'
#opening target file
with open(file, 'r') as domains:
    targets = domains.readlines()
    
    for target in targets:
        target = target.strip()
        bash('clear')
        bash('echo [*]Finding archives for '+target+'.... | pv -qL 30')
        link = 'http://web.archive.org/cdx/search/cdx?url=*.'+target+'/*&output=text&fl=original&collapse=urlkey'
        curl(link) 

        #Writing data in file 
        with open('/tmp/webarchive.txt', 'a') as subdomain:
            subdomain.write(get_body)
        
        bash('echo [Completed] '+target+ '..... | pv -qL 30')
        bash('clear')
domains.close

#Filtering out the data obtained after curl
cmd = 'cat /tmp/webarchive.txt | sed -e \'s_https*://__\' -e \"s/\/.*//\" | sort -u | tee -a /tmp/sub4.txt '
bash(cmd)

