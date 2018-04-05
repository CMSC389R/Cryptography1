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


