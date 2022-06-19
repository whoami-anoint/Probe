#!/bin/bash
clear
pv -qL 100 .banner.txt
echo -e "\nEvery thing you need as a bug hunter" | pv -qL 25   

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

function subdomain(){
    subfinder -d  $target_link$i -t 200 -v -o sub1.txt
    amass enum -src -ip -brute -d $target_link -o sub2.txt
    # sort sub1.txt sub2.txt | uniq -u > sub_uniq.txt
    # cat sub_uniq.txt |httpx -threads 200| tee -a subdomains.txt
    # cat subdomains.txt | waybackurls | tee -a waybackurls.txt
    # cat waybackurls.txt |gf xss| tee -a gfxss.txt
    # notify -bulk -data waybackurls.txt -id subdomain 
}

if [[ $response == "Y" || $response == "y" || $response == "yes" || $response == "Yes" ]]
then
    cd Projects/$pro_name
    subdomain
    

elif [[ $response == "N" || $response == "n" || $response == "no" || $response == "No"  ]]
then
    cd Scan
    subdomain

else 
    error
    exit
fi
