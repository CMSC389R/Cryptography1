from datetime import datetime
from datetime import timedelta

file = open("shadow.txt", "r")

for line in file:
	split = line.split(":")
	print "User: " +split[0]
	print "Password: " + split[1]

	if(split[2]):
		print "Date of last change: " + str(datetime.strptime('01 Jan 1970', '%d %b %Y') + timedelta(days=int(split[2])))
	if(split[3]):
		if (split[3] == "0"):
			print "Password may be changed at any time."
		else:
			print "Number of days before password must be changed: " + split[3]
	if(split[4]):
		if (split[4] == "99999"):
			print "User can keep password unchanged."
		else:
			print "Number of days after password must be changed: " + split[4]
	if(split[5]):
		print "The number of days to warn the user of an expiring password: " + split[5]
	if(split[6]):
		print "The number of days after password expires that account is disabled: " + split[6]
	if(split[7]):
		print "The number of days since the account has been disabled: " + split[7]


	print "-------------"