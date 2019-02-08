nmap scan
=========

The bash script `scan.sh` read line by line the content of the file `ips.txt` and create a XML report (in `outputs/`) for each IP scanned. This prevent the loss of resultsin case the scan crash. It also allows you to look at the results while the scan is still ongoing.

The python script `parse.py` is a simple parse for the nmap report in XML format. At the moment, the script list all IP and print the open ports. The script takes as argument the folder wher the XML reports are stored (`outputs/` by default).


Install
-------

Download the repository, edit the file `ips.txt` with the IPs you want to scan (ideally one single IP per line).


Example
-------

```
$ git clone https://github.com/SecureLink-PT/nmap-scan
$ cd nmap-scan
$ echo "1.1.2.2" > ips.txt
$ echo 8.8.8.8" >> ips.txt
$ scan.sh
...
$ parse.py
```
