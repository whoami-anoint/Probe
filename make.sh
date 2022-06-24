#!/bin/bash

# OS Check
os_type=`uname -r`
if [[ $os_type == *"arch1"* ]];
then
    pkg_manager="yay -S ";
    go_lang="go"
    $pkg_manager python-devtools
else 
    pkg_manager="sudo apt-get install";

    go_lang="golang"
    $pkg_manager python-dev-is-python3
fi
#Before running banner or other text pv is required

if [[ ! -f "/bin/pv" ]]
then
    $pkg_manager pv
fi
clear
bash script/art.sh
echo -e "\n\n[*]Installing Probe....." | pv -qL 8

#Installing basic package

$pkg_manager dirsearch 
$pkg_manager nmap
$pkg_manager $go_lang
$pkg_manager python3-pip  libssl-dev libffi-dev
$pkg_manager jq
pip3 install anubis-netsec
pip3 install pycurl
#Go install
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/OWASP/Amass/v3/...@master
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/tomnomnom/waybackurls@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/tomnomnom/gf@latest 2>/dev/null
go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest 2> /dev/null
go install github.com/OJ/gobuster/v3@latest 2> /dev/null
go install github.com/tomnomnom/assetfinder@latest 2> /dev/null
go install github.com/cgboal/sonarsearch/cmd/crobat@latest 2> /dev/null
go install github.com/lc/gau/v2/cmd/gau@latest 2> /dev/null
go install github.com/Emoe/kxss@latest 2> /dev/null
go install github.com/tomnomnom/qsreplace@latest 2> /dev/null
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest 2> /dev/null
go install github.com/hahwul/dalfox/v2@latest 2> /dev/null
go install github.com/ferreiraklet/Jeeves@latest 2> /dev/null

#Git Install
mkdir gitclone 2>/dev/null; cd gitclone
git clone https://github.com/tomnomnom/gf 2>/dev/null
git clone https://github.com/1ndianl33t/Gf-Patterns 2>/dev/null
clear
#Setup Git tools
#For GF
mkdir ~/.gf 2>/dev/null
cp gf/examples/* ~/.gf 2>/dev/null
cp Gf-Patterns/* ~/.gf 2>/dev/null
#Back to Home 
cd ..
sudo cp ~/.local/bin/* /bin

#Fun Part
if [[ ! -f "/bin/gf" ]]
then
    echo -e "[*]GF with good nature make life easy..." | pv -qL 8
    echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
    echo -e "[*]Proposing gf...."|pv -qL 8
    echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
    echo -e "[*]Building Relation......"|pv -qL 8
fi

# Copying part of go
sudo mv ~/go/bin/* /bin/ 2>/dev/null

echo -e "\n[*]Probe is ready to use...."|pv -qL 8
cat art/thanks.txt
