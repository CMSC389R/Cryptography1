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


#### 4. What are the restrictions each user has on changing their password, if any?


#### 5. Have any passwords expired? If so, whose?

#### 6. Use one of the tools discussed in class (hashcat, JohnTheRipper) to try and recover each password and show how you used the tool.
