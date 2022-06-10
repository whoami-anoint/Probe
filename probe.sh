#!/bin/bash

pv -qL 100 .banner.txt
echo -e "\nEvery thing you need as a bug hunter" | pv -qL 25   

#Creating Project 
echo -n "Create project [y/N]"
read response
if [[ $response == "Y" || $response == "y" || $response == "yes" || $response == "Yes" ]]
then
    echo -n "Project name : "
    read pro_name
    echo "[*]Creating project $pro_name....." | pv -qL  25
    mkdir Projects/$pro_name
elif [[ $response == "N" || $response == "n" || $response == "no" || $response == "No"  ]]
then
    echo "[*] Using Scan directory as project "
    mkdir Scan 2>>/dev/null
else 
    echo "*********************************************"
    echo "* * * You fool! Its like GIGO ;)  * * * * * *"
    echo "* * * * * * Invaild Input * * * * * * * * * *"
    echo "*********************************************"
    exit
fi

echo -n "Target : "
read target_link
echo "Provide subdomain output file name to store.... "
echo -n "[1] SubDomain Filename : "
read sub1
echo -n "[2] SubDomain Filename : "
read sub2
echo "Provide Directory search output file name to store.... "
echo -n "[*] Dirsearch : "
read dir_file

subdomain(){
    subfinder -d  $target_link -t 200 -v -o $sub1.txt
    amass enum -src -ip -brute -d $target_link -o $sub2.txt
    sort $sub1.txt $sub2.txt | uniq -u > sub_uniq.txt
    cat sub_uniq.txt |httpx -threads 200| tee -a subdomain.txt
    cat subdomain.txt | waybackurls | tee -a waybackurls.txt
    notify -bulk -data waybackurls.txt -id subdomain
}


if [[ $response == "Y" || $response == "y" || $response == "yes" || $response == "Yes" ]]
then
    cd $pro_name
    subdomain
    

elif [[ $response == "N" || $response == "n" || $response == "no" || $response == "No"  ]]
then
    cd Scan
    subdomain
    

else 
    echo "*********************************************"
    echo "* * * You fool! Its like GIGO ;)  * * * * * *"
    echo "* * * * * * Invaild Input * * * * * * * * * *"
    echo "*********************************************"
    exit
fi
