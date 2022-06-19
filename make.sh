#!/bin/bash

# OS Check
os_type=`uname -r`
if [[ $os_type == *"arch1"* ]];
then
    pkg_manager="yay -S ";
    # go_lang = "go"
else 
    pkg_manager="sudo apt-get install";
    go_lang="golang"
fi
#Before running banner or other text pv is required

$pkg_manager pv
clear
bash script/art.sh
echo -e "\n\n[*]Installing Probe....." | pv -qL 8

#Installing basic package

$pkg_manager dirsearch 
$pkg_manager nmap
$pkg_manager $go_lang

#Go install
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/OWASP/Amass/v3/...@master
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/tomnomnom/waybackurls@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/tomnomnom/gf@latest >/dev/null
go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest > /dev/null
go install github.com/OJ/gobuster/v3@latest > /dev/null
go install github.com/tomnomnom/assetfinder@latest > /dev/null
go install github.com/cgboal/sonarsearch/cmd/crobat@latest > /dev/null
go install github.com/lc/gau/v2/cmd/gau@latest > /dev/null
go install github.com/Emoe/kxss@latest > /dev/null
go install github.com/tomnomnom/qsreplace@latest > /dev/null
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest > /dev/null
go install github.com/hahwul/dalfox/v2@latest > /dev/null
go install github.com/ferreiraklet/Jeeves@latest > /dev/null

#Git Install
mkdir gitclone; cd gitclone
git clone https://github.com/tomnomnom/gf 
git clone https://github.com/1ndianl33t/Gf-Patterns
cd ..
clear

#Fun Part
echo -e "[*]GF with good nature make life easy..." | pv -qL 8
echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
echo -e "[*]Proposing gf...."|pv -qL 8
echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
echo -e "[*]Building Relation......"|pv -qL 8

# Copying part
sudo mv ~/go/bin/* /bin/ 2>/dev/null
mkdir ~/.gf 2>/dev/null
cp gitclone/gf/examples/* ~/.gf
cp gitclone/Gf-Patterns/* ~/.gf
echo -e "\n[*]Probe is ready to use...."|pv -qL 8
cat art/thanks.txt