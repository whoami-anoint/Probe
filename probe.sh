#!/bin/bash

clear

#Some cool art stuff

bash script/art.sh

#Creating Project

echo -n "Create project [Y/n]: "
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
    echo -n "Project name : "
    read pro_name
    echo "[*]Creating project $pro_name....." | pv -qL  25
    mkdir Projects/$pro_name 2>/dev/null
fi

#Target 
python3 script/targets.py

#Probing


function subdomain(){
    subfinder -dL  /tmp/targets.txt -t 200 -v -o /tmp/sub1.txt
    echo -e "[*]This process may take some time " | pv -qL 30  
    amass enum -src -df /tmp/targets.txt -o /tmp/sub2.txt
    bash script/assestFinder.sh #It will create a file /tmp/sub3.txt
    anubis -f /tmp/targets.txt -o /tmp/sub3.txt
    python3 script/webarchive.py #It will create a file /tmp/sub4.txt
    cd Projects/$pro_name
    sort /tmp/sub1.txt /tmp/sub2.txt /tmp/sub3.txt /tmp/sub4.txt | uniq -u > sub_uniq.txt
    cat sub_uniq.txt |httpx -threads 200| tee -a subdomains.txt
    cat subdomains.txt | waybackurls | tee -a waybackurls.txt
    cat waybackurls.txt |gf xss| tee -a gfxss.txt
}

if [[ $response == "Y" || $response == "y" || $response == "yes" || $response == "Yes" ]]
then

    subdomain
    

elif [[ $response == "N" || $response == "n" || $response == "no" || $response == "No"  ]]
then
    cd Scan/Random
    subdomain

else 
    cd Projects/$pro_name
    cd ../..
    subdomain
fi
