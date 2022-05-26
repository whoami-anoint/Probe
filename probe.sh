#!/bin/bash
pv -qL 70 .banner.txt
 
echo "Welcome to bug automation tool"

echo -n "Enter  target site  link : "
read target_link
echo -n "Enter output file_name for subfinder: "
read output_file_subfinder
echo -n "Enter output file_name for Amass: "
read output_file_amass

subfinder -d  $target_link -t 200 -v -o $output_file_subfinder.txt

amass enum -src -ip -brute -d $target_link -o $output_file_amass.txt

sort $output_file_amass.txt $output_file_subfinder.txt | uniq -u finalsubdomain.txt

cat finalsubdomain.txt |httpx -threads 200| tee -a subdomains.txt

cat subdomain.txt | waybackurls | tee -a waybackurls.txt

nmap -iL finalsubdomain.txt -p --open -sV -oG nmap.txt

cat waybackurls.txt | gf xss | tee -a gfxss.txt
cat waybackurls.txt | gf sqli | tee -a gfsqli.txt
cat waybackurls.txt | grep js | tee -a jsfiles.txt

echo "You might be fan of Superman,Batman,Shaktiman,Spiderman,Iron Man but I'm fan of Pacman" | pv -qL 8
