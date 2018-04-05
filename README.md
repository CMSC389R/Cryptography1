# Cryptography1
First Cryptography assignment for my Intro to Ethical Hacking Course at the University of Maryland

## Part 1

#### 1. What is the hashing algorithm(s) used to secure these passwords?

The hashing algorithm used is ```MD5```, I discovered this by searching for any hashes that use similar formats of those found in the shadow file. I noticed that they all begin with ```$1``` followed by two more segements starting with this ```$``` character. After searching around I found the answer in the docs for pythons ```pathlib``` library, [found here](http://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html). 

![alt text]()

#### 2. What salt is used for these passwords, if any?

The salts are the plain text segments after the 2nd ```$``` character, I found this out from the ```pathlib``` docs [found here](http://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html). So the corresponding salts for each user are:

```
root: XXv.SXDX
admin: GOpCaSQH
bob: vgy72nH3
joe: eZ5SZG9g
mnthomp22: SlJR2aEx
```


#### 3. When were the passwords changed, if at all?

In order to figure out when the passwords were last changed I created a file that would parse each hash, and decipher all the required information. I figured out how to decipher the hash from this [site](https://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html).

After running my parse.py file I recieve this output:

```
User: root
Password: $1$XXv.SXDX$GCgBecucGEarYoB2LuRme.
-------------
User: admin
Password: $1$GOpCaSQH$Obpoa/kGTZHEBprOVAJEJ0
-------------
User: bob
Password: $1$vgy72nH3$QHd91NxlO83OHMw8KUYey1
Date of last change: 1973-08-30 00:00:00
Number of days before password must be changed: 5
Number of days after password must be changed: 90
The number of days to warn the user of an expiring password: 7
The number of days after password expires that account is disabled: 7
The number of days since the account has been disabled: 20000
-------------
User: joe
Password: $1$eZ5SZG9g$7N28moxhIIu2ohiDjGgI61
Date of last change: 1971-01-25 00:00:00
Number of days after password must be changed: 120
The number of days to warn the user of an expiring password: 14
The number of days after password expires that account is disabled: 3
The number of days since the account has been disabled: 17618
-------------
User: mthomp22
Password: $1$SlJR2aEx$g6TObcH2OTrlx8MIWDZjs.
Date of last change: 1975-08-11 00:00:00
Number of days before password must be changed: 99999
Number of days after password must be changed: 0
-------------
```

So only the passwords of users bob, joe, and mnthomp22 have changed, and they changed on these dates:

```
bob: August 30th, 1973
joe: January 25th, 1971
mnthomp22: August 11th, 1975
```

#### 4. What are the restrictions each user has on changing their password, if any?

According to the findings I got after running my parse.py file on the shadow file, I was able to establish that:

```
root: No restrictions on password.

admin: No restrictions on password.

bob: Has 5 days before password must be changed
     Must change his password in 90 days
     Gets a warning 7 days before password must be changed
     Account is disabled 7 days after failing to change password
     
joe: Must change his password in 120 days
     Gets a warning 14 days before password must be changed
     Account is disabled 3 days after failing to change password
     
mnthomp22: Has to change password in 99999 days 
           Must change his password in 0 days (Oh no!)
           
```

#### 5. Have any passwords expired? If so, whose?

According to the above information the accounts of bob and joe have been disabled, bob's has been disbaled for 2000 days, while joe's has been disabled for 17618 days.

#### 6. Use one of the tools discussed in class (hashcat, JohnTheRipper) to try and recover each password and show how you used the tool.

I decided to use John The Ripper in order to recover each password, in order to get more accustomed to how the tool work and recieved all the information I needed from this [resource](https://linuxconfig.org/password-cracking-with-john-the-ripper-on-linux).

THe first step was to unshadow the passwd file using the shadow file: ```unshadow passwd shadow > unshadowed```
The second step was to run john the ripper on unshadowed file: ```john --show unshadowed'''

This last command provided me with this output:
```
root:toor:0:0:root:/root:/bin/bash
admin:etude:1:0:admin:/home/admin:/bin/bash
bob:saget:100:1000:bob:/home/bob:/bin/zsh
joe:schmo:101:1000:joe:/home/joe:/bin/csh
mthomp22:blink:102:1000:mthomp22:/home/mthomp22:/bin/briongsh

5 password hashes cracked, 0 left
```

From this output I obtained the passwords for each userL

```
root: toor
admin: etude
bob: saget
joe: schmo
mthomp22: blink
```
