# Libraries
import requests
import json

# Globals
_COLOR = {
	'Red': '\033[0;31m',
	'Green': '\033[0;32m',
	'Blue': '\033[0;34m',
	'Purple': '\033[0;35m',
	'Yellow': '\033[1;33m',
	'End': '\033[0m'
}
web_url = "http://127.0.0.1:8000"
username = ""
password = ""

_CONTENT_SEPERATOR = "*********************************"

# Functions
def general_interface():
	exit_status = 1
	login_status = 0
	access_token = ""
	refresh_token = ""

	global username
	global password
	
	while exit_status:
		option = 0
		if login_status == 0:
			option = print_login()
		else:
			option = print_logout()
		if option < 1 or option > 6:
			print_wrong_option_selected()
		elif option == 6:
			exit_status = 0
			print(f"{_COLOR['Red']}Exitted{_COLOR['End']} Successfully.")
		else:
			print(f"Option You selected {_COLOR['Purple']}{option}{_COLOR['End']}")
			if option == 1:
				if login_status == 1:
					login_status = 0
					username = ""
					password = ""
					access_token = ""
					refresh_token = ""
				else:
					login_status = 1
					get_user()
			elif option == 2:
				resp = requests.get(f"{web_url}/api/test_api/")
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					for i in response_dict:
						print(f"{i} :\t\t{response_dict[i]}")
			elif option == 3:
				resp = requests.get(f"{web_url}/api/test_api_auth/", headers={"Authorization": f"Bearer {access_token}"})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					for i in response_dict:
						print(f"{i} :\t\t{response_dict[i]}")
			elif option == 4:
				resp = requests.post(f"{web_url}/auth/token/refresh/", data={"refresh":refresh_token})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					access_token = response_dict['access']
					refresh_token = response_dict['refresh']
					print(f"Tokens Are {_COLOR['Green']}Refreshed{_COLOR['End']}")		
			elif option == 5:
				resp = requests.post(f"{web_url}/auth/token/", data={"username":username, "password":password})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					access_token = response_dict['access']
					refresh_token = response_dict['refresh']
					print(f"Tokens Are {_COLOR['Yellow']}Setted{_COLOR['End']}")

def print_login():
	print(f"""{_CONTENT_SEPERATOR}
	1. {_COLOR['Green']}Log In{_COLOR['End']}
	2. {_COLOR['Blue']}Call API{_COLOR['End']}
	3. {_COLOR['Blue']}Call API{_COLOR['End']} with {_COLOR['Purple']}Authentication {_COLOR['End']}
	4. {_COLOR['Blue']}Refresh Token{_COLOR['End']}
	5. {_COLOR['Blue']}Get Token{_COLOR['End']}
	6. {_COLOR['Red']}Exit{_COLOR['End']}
{_CONTENT_SEPERATOR}""")
	
	try :
		return int(input("Option >>> : "))
	except ValueError:
		return 0
def print_logout():
	print(f"""{_CONTENT_SEPERATOR}
	1. {_COLOR['Red']}Log Out{_COLOR['End']}
	2. {_COLOR['Blue']}Call API{_COLOR['End']}
	3. {_COLOR['Blue']}Call API{_COLOR['End']} with {_COLOR['Purple']}Authentication {_COLOR['End']}
	4. {_COLOR['Blue']}Refresh Token{_COLOR['End']}
	5. {_COLOR['Blue']}Get Token{_COLOR['End']}
	6. {_COLOR['Red']}Exit{_COLOR['End']}
{_CONTENT_SEPERATOR}""")
	
	try :
		return int(input("Option >>> : "))
	except ValueError:
		return 0

def print_wrong_option_selected():
	print(f"{_COLOR['Red']}Wrong Option{_COLOR['End']} has been selected.")

def get_user():
	global username
	global password
	print(_CONTENT_SEPERATOR)
	username = input("Please Enter the Username\t:")
	password = input("Please Enter the Password\t:")
	print(f"{_COLOR['Yellow']}Username{_COLOR['End']} and {_COLOR['Yellow']}Password{_COLOR['End']} setted successfully.")

# Main
if __name__ == '__main__':
	general_interface()
