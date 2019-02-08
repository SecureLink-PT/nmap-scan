#!/bin/bash

while read p; do
    
    echo "Scan: $p"
    nmap -oX "outputs/$p.txt" -p- $p 
    
done < ips.txt
