rm ~/.probe -rf 2>/dev/null
mkdir ~/.probe 2>/dev/null
mkdir ~/.probe/script 2>/dev/null
wget https://raw.githubusercontent.com/whoami-anoint/Probe/main/script/gf.sh -O ~/.probe/script/gf.sh
wget https://raw.githubusercontent.com/whoami-anoint/Probe/main/script/configNotification.py -O ~/.probe/script/configNotification.py
wget https://raw.githubusercontent.com/whoami-anoint/Probe/main/requirements.txt -O ~/.probe/requirements.txt
pip3 install -r ~/.probe/requirements.txt
clear
