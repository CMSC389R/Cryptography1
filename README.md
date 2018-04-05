# Cryptography1
First Cryptography assignment for my Intro to Ethical Hacking Course at the University of Maryland

## Part 1

#### 1. What is the hashing algorithm(s) used to secure these passwords?

The hashing algorithm used is ```MD5```, I discovered this by searching for any hashes that use similar formats of those found in the shadow file. I noticed that they all begin with ```$1``` followed by two more segements starting with this ```$``` character. After searching around I found the answer in the docs for pythons ```pathlib``` library, [found here](http://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html). 

![alt text](https://github.com/yreiss1/Cryptography1/blob/master/pathlib.png)

#### 2. What salt is used for these passwords, if any?

The salts are the plain text segments after the 2nd ```$``` character, I found this out from the ```pathlib``` docs [found here](http://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html). So the corresponding salts for each user are:

```
root: XXv.SXDX
admin: GOpCaSQH
bob: vgy72nH3
joe: eZ5SZG9g
mthomp22: SlJR2aEx
```


#### 3. When were the passwords changed, if at all?

In order to figure out when the passwords were last changed and to save myself time and effort I wrote a program that would parse each hash, and decipher all the required information. I figured out how to decipher the hash from this [site](https://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html), and my parser can be found [here](https://github.com/yreiss1/Cryptography1/blob/master/parse.py)

After running my parse.py file I recieved this output:

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
mthomp22: August 11th, 1975
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
     
mthomp22: Has to change password in 99999 days 
           Must change his password in 0 days (Oh no!)
           
```

#### 5. Have any passwords expired? If so, whose?

According to the above information only joe's account has been disabled, Joe's account was to be disabled 17618 days after January 1st 1970, which occured on the March 28th, 2018! I found this by converting number of days to years/days and adding to January 1st, 1970. 

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

From this output I obtained the passwords for each user:

```
root: toor
admin: etude
bob: saget
joe: schmo
mthomp22: blink
```

## Part 2

My code for this part of the assignment can be found [here](https://github.com/yreiss1/Cryptography1/blob/master/part2.py). My thought process here was that for each potential password in the list, I iterated through all the lower case characters in the alphabet, appending the the characters to the beginning of the passwords and then hashing this combination. I would then check if this new hash exists in our hash file. If it existed in the hash file I would print out the salt and the password because that comprised the hash because these were apparently the correct salt and password combination. 

```
#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib

wordlist = "password_list.txt"       # download the wordlist and enter the ABSOLUTE path here
hash_file = open("hashes.txt", "r")
passwords = open(wordlist, "r")


hashes = hash_file.read()

#Creates a list of all lower case english characters
alphabet = list(map(chr, range(97, 123)))

#Every iteration of a new password, I iterate through the whole list of characters
for line in passwords:
	for character in alphabet:
		salted = character + line.strip()
		hashed = hashlib.sha512(salted).hexdigest()


		#If the newly hashed password is in the hash, then it is the right password.
		if hashed in hashes:
			print "Salt_Character: " + character + ", Password: " + line
```





When I run the code I get this output of each salt and password:
```
Salt_Character: c, Password: 888888

Salt_Character: e, Password: manchester

Salt_Character: b, Password: vfhbyf

Salt_Character: y, Password: jason1

Salt_Character: r, Password: motorola
```

## Part 3

My code for this part of the assignment can be found [here](https://github.com/yreiss1/Cryptography1/blob/master/part3.py). My thought process here was pretty simple, I realized that our friend on the other side would ask more than one question, so while they keep asking questions we'll keep evaluating them. I use python's ```eval()``` function to evaluate the line as a string, hash it using ```hashlib.sha256(answer).hexdigest()``` which converts the answer into a hash, and return it to our friend on the other side. I use a while loop to keep doing this untill there are no more questions. 

```
#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "irc.csec.umiacs.umd.edu"   # IP address or URL
port = 4444     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data)

split = data.split("\n")


answer = eval(split[1])




while (split[1]):
	hashed = hashlib.sha256(str(answer)).hexdigest()

	s.send(str(hashed) + "\n")

	data = s.recv(1024)
	print(data)
	split = data.split("\n")
	if (split[1]):
		answer = eval(split[1])

# close the connection
s.close()
```

The flag that is passed back after completing the two evaluations is: 

```You win! CMSC389R-{d0nt_pL@y_w1tH_mY_em0SHAns}```

Don't worry I wont!

