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
sudo mv ~/go/bin/* /bin/ 2>/dev/null
