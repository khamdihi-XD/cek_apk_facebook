
import os, sys, time, re, requests, bs4
from  bs4 import BeautifulSoup as parser

os.system("clear")
kukiz = input(" Masukan cookie : ")
try:
	#- aktif
	ses = requests.Session()
	url = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kukiz})
	psot = parser(url.text,"html.parser")
	fick = psot.find("form", {"method":"post"})
	game = [memek.text for memek in fick.find_all("h3")]
	if len(game) == 0:
		print("\n× Tidak ada aplikasi aktif")
	else:
		for kontol in range(len(game)):
			print("\n- mengechek aplikasi aktif")
			print("%s %s "%(kontol+1, game[kontol].replace(" Di akses pada ", "Di tambahkan pada")));time.sleep(1)
	#- Kadarluarsa
	link = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie":kukiz})
	post = parser(link.text,"html.parser")
	cari = post.find("form",{"method":"post"})
	game = [kontol_.text for kontol_ in cari.find_all("h3")]
	if len(game) == 0:
		print("\n× Tidak ada aplikasi kadarluarsa")
	else:
		for aplikasi in range(len(game)):
			print("\n- mengechek aplikasi kadarluarsa")
			print("\n%s %s"%(aplikasi+1, game[aplikasi].replace("Kadarluarsa pada","Tidak di akses pada")));time.sleep(1)
	#- Di hapus
	try:
		link = ses.get("https://free.facebook.com/settings/apps/tabbed/?tab=removed", cookies={"cookie":kukiz})
		post = parser(link.text,"html.parser")
		cari = post.find("form",{"method":"post"})
		game = [_kontol_.text for _kontol_ in cari.find_all("h3")]
		if len(game) == 0:
			print("\n× Tidak ada aplikasi di yanh hapus")
		else:
			for khamdihiXD in range(len(game)):
				print("× Mengechek aplikasi yang di hapus")
				print("\n%s %s"%(khamdihiXD+1, game[khamdihiXD].replace("Di hapus pada","Di hapus")))
	except AttributeError:
		print("× Tidak ada aplikasi yang di hapus/cokie invalid!")


except AttributeError:
	print(" × cokie invalid")


"""

DateTime   : sabtu 18 juni 2022: 13.40
Made in    : Indonesia
Code by    : KhamdihiXD

"""
