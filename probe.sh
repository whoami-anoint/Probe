#!/bin/bash
clear
# bash script/art.sh
function error(){
    echo "*********************************************"
    echo "* * * You fool! Its like GIGO ;)  * * * * * *"
    echo "* * * * * * Invaild Input * * * * * * * * * *"
    echo "*********************************************"
}

#Creating Project
echo -n "Create project [y/N]"
read response
if [[ $response == "Y" || $response == "y" || $response == "yes" || $response == "Yes" ]]
then
    echo -n "Project name : "
    read pro_name
    echo "[*]Creating project $pro_name....." | pv -qL  25
    mkdir Projects/$pro_name 2>/dev/null
elif [[ $response == "N" || $response == "n" || $response == "no" || $response == "No"  ]]
then
    echo "[*] Using Scan directory as project "
    mkdir Scan
else 
    error
    exit
fi

#Target 
python3 script/targets.py

#Probing
#assestfinder

function subdomain(){
    #subfinder -dL  /tmp/targets.txt -t 200 -v -o /tmp/sub1.txt
    #amass enum -src -ip -brute -df /tmp/targets.txt -o /tmp/sub2.txt
    bash script/assestFinder.sh
    # sort sub1.txt sub2.txt | uniq -u > sub_uniq.txt
    # cat sub_uniq.txt |httpx -threads 200| tee -a subdomains.txt
    # cat subdomains.txt | waybackurls | tee -a waybackurls.txt
    # cat waybackurls.txt |gf xss| tee -a gfxss.txt
}

if [[ $response == "Y" || $response == "y" || $response == "yes" || $response == "Yes" ]]
then
    cd Projects/$pro_name
    cd ../..
    subdomain
    

elif [[ $response == "N" || $response == "n" || $response == "no" || $response == "No"  ]]
then
    cd Scan/Random
    subdomain

else 
    error
    exit
fi
