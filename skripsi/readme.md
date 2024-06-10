## ping
   >> ping -c 5 elearning.smansa.link
   -- IP : 198.252.98.81

## dig
   >> dig elearning.smansa.link
   -- IP : 198.252.98.81

## nslookup
   >> nslookup elearning.smansa.link
   -- Server: 103.19.180.211
   -- Address: 103.19.180.211#53
   -- IP : 198.252.98.81

## Shodan
   >> https://www.shodan.io/host/198.252.98.81
   -- Output in screenshot

## whois
   >> whois elearning.smansa.link

## theHarvester
   >> theHarvester -d elearning.smansa.link -b urlscan

## nmap
   >> nmap -sC -sV -oN scan_nmap 192.252.98.81
      -sC	=	same as --script=default
      -sV	=	version detection

## Open Port
   o) 21		ftp				Pure-FTPd
   o) 22		ssh 			OpenSSH 7.4 (protocol 2.0)
   o) 25 		smtp?	
   o) 53 		domain			PowerDNS Authoritative Server 4.7.3
   o) 80 		tcpwrapped	
   o) 110		pop3?
   o) 143 		imap?
   o) 443		ssl/https		LiteSpeed
   o) 465		ssl/smtp   		Exim smtpd 4.96.2
   o) 587	  	smtp     	  	Exim smtpd 4.96.2
   o) 993		ssl/imap  		Dovecot imapd
   o) 995		ssl/pop3   		Dovecot pop3d