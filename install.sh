#!/bin/bash

# OS Check
os_type=`uname -r`
if [[ $os_type == *"arch1"* ]];
then
    pkg_manager="yay -S ";
    # go_lang = "go"
else 
    pkg_manager="sudo apt-get install";
    go_lang = "golang"
fi
#Before running banner or other text pv is required

$pkg_manager pv
clear
pv -qL 100 .banner.txt
echo -e "\n\n[*]Installing Probe....." | pv -qL 8

#Installing basic package
$pkg_manager dirsearch 
$pkg_manager nmap
$pkg_manager $go_lang


go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/OWASP/Amass/v3/...@master
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/tomnomnom/waybackurls@latest
go get -u github.com/tomnomnom/gf >/dev/null
clear

echo -e "[*]GF with good nature make life easy..." | pv -qL 8
echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
echo -e "[*]Proposing gf...."|pv -qL 8
echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
echo -e "[*]Building Relation......"|pv -qL 8
sudo mv ~/go/bin/* /bin/
echo -e "\n[*]Probe is ready to use...."|pv -qL 8
cat .thanks.txt
