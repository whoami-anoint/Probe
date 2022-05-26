#!/bin/bash

#Root check 
if [ "$EUID" -ne 0 ]
then
    echo "*********************************************"
    echo "* * * Please run the command as root  * * * *"
    echo "* * * * * * \$sudo ./install.sh * * * * * * *"
    echo "*********************************************"
    exit
fi
# OS Check
os_type=`uname -r`
if [[ $os_type == *"arch1"* ]];
then
    pkg_manager="yay -S "
else 
    pkg_manager="apt-get install"
fi
pv -qL 70 .banner.txt
echo -e "\n[*]Installing Probe....." | pv -qL 8
$pkg_manager dirsearch 
$pkg_manager nmap 
$pkg_manager go 

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/OWASP/Amass/v3/...@master
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/tomnomnom/waybackurls@latest
mv ~/go/bin/* /bin/
