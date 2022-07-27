#!/bin/bash
clear
rm /tmp/sub3.txt 2>/dev/null
File="/tmp/targets.txt"
Links=$(cat $File)
echo -e "Finding assest...." | pv -qL 25  

for Link in $Links
do
	echo "[*]Finding assest from $Link" | pv -qL 25
	assetfinder --subs-only $Link >> /tmp/sub3.txt
	echo "[Completed] $Link"| pv -qL 15
	clear
done
cat /tmp/sub3.txt