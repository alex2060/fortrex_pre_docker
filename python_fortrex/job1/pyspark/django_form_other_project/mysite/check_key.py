

import sys
import requests
import hashlib
import random
#path = ""
#url = "https://www.google.com/"
#x = requests.get(url)
#string="pythonpool.com"
#encoded=string.encode()
#result = hashlib.sha256(encoded)


import hashlib

#passwordCandidate = "1766c4dabad85b74b49c98ec25f613962d3ee1cf8a6ca8a26ff4654612ec9204"
#print(hashlib.sha256(passwordCandidate.encode()).hexdigest())

# print : 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08


#print(x.content)

#PATH/change_key.php?name=KeyName&key=KeySolution&Nkey=NewKey
#PATH/check_key.php?name=KeyName


#alexhaussmann.com/adhaussmann/a_final/check_key.php?name=d304d6c42b7f6ac9ee3a90804cf89f5c637d7f72f93c3dcdad8a69a0924c5a7d



#name of key:d304d6c42b7f6ac9ee3a90804cf89f5c637d7f72f93c3dcdad8a69a0924c5a7d
#key: 1766c4dabad85b74b49c98ec25f613962d3ee1cf8a6ca8a26ff4654612ec9204 


#http://alexhaussmann.com/adhaussmann/a_final/add_key.php

#ptest_led pass

#ledgername ptest_led hash 9cf3c7066769ea0ecf9b0c6fa721177d8c2338d9c7493b250b0f475382358cce solution key time 2021-09-07 09:52:42
def get_key(path,ledgure_name,keyname,password):
	#check key by name
	#get password
	#
	x = requests.get(path+"check_key.php?name="+keyname)
	getarray = str(x.content)

	out = getarray.split(" ")
	print(out)
	print(len(out))



	if len(out)==9:
		print("passed_leddgure")
	else:
		return [False,"",""]

	if ledgure_name==out[1]:
		print("passed_leddgure")
	else:
		return [False,"",""]


	passwordCandidate = password
	val = hashlib.sha256(passwordCandidate.encode()).hexdigest()
	if val==out[3]:
		print("passed_key")
	else:
		return [False,"",""]
	#http://alexhaussmann.com/adhaussmann/a_final/output2.php?key=1766c4dabad85b74b49c98ec25f613962d3ee1cf8a6ca8a26ff4654612ec9204&name=d304d6c42b7f6ac9ee3a90804cf89f5c637d7f72f93c3dcdad8a69a0924c5a7d&entery_name=ptest_led&uname=ptest
	random_string=""
	for _ in range(100):
	    random_integer = random.randint(65, 80)
	    # Keep appending random characters using chr(x)
	    random_string += (chr(random_integer))

	passwordCandidate = random_string

	newkey = hashlib.sha256(passwordCandidate.encode()).hexdigest()


	keyhash = hashlib.sha256(newkey.encode()).hexdigest()
	newname = ""

	x = requests.get(path+"change_key.php?name="+keyname+"&key="+password+"&Nkey="+keyhash)
	#print()
	#print(x.content)
	myval = str(x.content)[14:78]
	#print()
	#print()

	stingout = path+"output2.php?key="+newkey+"&name="+myval+"&entery_name="+ledgure_name 
	#print(stingout)
	#print()
	#print()
	return [True,stingout,path+ledgure_name]






print(get_key("http://alexhaussmann.com/adhaussmann/a_final/","ptest_led","f22f4a373dbf667dcd607cddec0cd6c10f3618cdc03dc1a02f428d15ab881669","6526e8aa10b29a08ac46cc0bec9590ee3e95f92eb37436ea94d34003f93770af"))
#http://alexhaussmann.com/adhaussmann/a_final/"change_key.php?name=fe4e9fa1e8924fdf9668bcf5a731eec2b9997b1296f83d5761dc7fd2571e83c6&key=eef90b2a4223ef8d8a1d641cdc71451dd82a68b6ad6efe2eae445ac3f29a52a7&Nkey=12131"+keyhash

#http://alexhaussmann.com/adhaussmann/a_final/change_key.php?name=fe4e9fa1e8924fdf9668bcf5a731eec2b9997b1296f83d5761dc7fd2571e83c6&key=eef90b2a4223ef8d8a1d641cdc71451dd82a68b6ad6efe2eae445ac3f29a52a7&Nkey=12131



#http://alexhaussmann.com/adhaussmann/a_final/output2.php?key=ada857dfcb9d0cfa6ace483b4b0563a19fee9b2d02af32bb5cd7685075e778bd&name=nabc82d4a651d9270ba9ba610ee8c0a1cf6e005c7afa06c17f827c3e8d3463f9e&entery_name=ptest_led&uname=ptest




