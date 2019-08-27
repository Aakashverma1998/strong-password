 # strong password program
x=input('enter the password\n')
if 15>len(x)>8:
	if x in  "@" or "#" :
		if  x in "1" or "2" or "3" or "4":
			print ("strong password")
		else:
			print("weak password")
	else:
		print("weak password")
else:
	print("weak password")