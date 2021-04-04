import os, sys

print ("\033[30;1mSilahkan Masukkan Username & Password Scriptnya")

print ("\033[33;1matau silahkan Hubungi Author +6282134566596 ")

username = 'SANTRI'      

password = 'CYBER'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[32;1mAkhirnya password bener juga cuk", 

			sys.exit()



		else:

			print "\033[31;1mPasswordnya salah cuk... [?]\033[33;1m"

			print "Silahkan segera log-in kembali cuk...!!\n"

			restart()



	else:

		print "\033[30;1mUsernamenya salah cuk... [?]\033[31;1m"

		print "Silahkan segera log-in kembali cuk...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
