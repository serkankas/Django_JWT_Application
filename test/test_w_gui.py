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
		option = -1
		if login_status == 0:
			option = print_login()
		else:
			option = print_logout()
		if option < 0 or option > 9:
			print_wrong_option_selected()
		elif option == 0:
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
				resp = requests.post(f"{web_url}/auth/token/", data={"username":username, "password":password})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					access_token = response_dict['access']
					refresh_token = response_dict['refresh']
					print(f"Tokens Are {_COLOR['Yellow']}Setted{_COLOR['End']}")
			elif option == 3:
				resp = requests.post(f"{web_url}/auth/token/refresh/", data={"refresh":refresh_token})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					access_token = response_dict['access']
					refresh_token = response_dict['refresh']
					print(f"Tokens Are {_COLOR['Green']}Refreshed{_COLOR['End']}")	
			elif option == 4:
				usern, passw, passw2 = get_user_log()
				resp = requests.post(f"{web_url}/api/create_user/", headers={"Authorization": f"Bearer {access_token}"}, data={'username':usern, 'password':passw, 'password2':passw2})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				response_dict = json.loads(resp.text)
				for i in response_dict:
					print(f"{i} :\t\t{response_dict[i]}")
			elif option == 5:
				usern = get_username()
				resp = requests.delete(f"{web_url}/api/delete_user/", headers={"Authorization": f"Bearer {access_token}"}, data={'username':usern})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				response_dict = json.loads(resp.text)
				for i in response_dict:
					print(f"{i} :\t\t{response_dict[i]}")
			elif option == 6:
				usern, group_id = get_group()
				resp = requests.put(f"{web_url}/api/change_user_group/", headers={"Authorization": f"Bearer {access_token}"}, data={'username':usern, 'group_id':group_id})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				response_dict = json.loads(resp.text)
				for i in response_dict:
					print(f"{i} :\t\t{response_dict[i]}")
			elif option == 7:
				resp = requests.get(f"{web_url}/api/test_api/")
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					for i in response_dict:
						print(f"{i} :\t\t{response_dict[i]}")
			elif option == 8:
				resp = requests.get(f"{web_url}/api/test_api_auth/", headers={"Authorization": f"Bearer {access_token}"})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				if status == 200:
					response_dict = json.loads(resp.text)
					for i in response_dict:
						print(f"{i} :\t\t{response_dict[i]}")
			elif option == 9:
				resp = requests.get(f"{web_url}/api/test_api_perm/", headers={"Authorization": f"Bearer {access_token}"})
				status = resp.status_code
				print(f"{_CONTENT_SEPERATOR}\nResponse status: \t{status}")
				response_dict = json.loads(resp.text)
				for i in response_dict:
					print(f"{i} :\t\t{response_dict[i]}")

def print_login():
	print(f"""{_CONTENT_SEPERATOR}
	1. {_COLOR['Green']}Log In{_COLOR['End']}
	2. {_COLOR['Blue']}Get Token{_COLOR['End']}
	3. {_COLOR['Blue']}Refresh Token{_COLOR['End']}
	4. {_COLOR['Green']}Create User{_COLOR['End']}
	5. {_COLOR['Red']}Delete User{_COLOR['End']}
	6. {_COLOR['Yellow']}Change user Group{_COLOR['End']}
	7. {_COLOR['Blue']}Call API{_COLOR['End']}
	8. {_COLOR['Blue']}Call API{_COLOR['End']} with {_COLOR['Purple']}Authentication {_COLOR['End']}
	9. {_COLOR['Blue']}Call API{_COLOR['End']} with {_COLOR['Purple']}Permission {_COLOR['End']}
	0. {_COLOR['Red']}Exit{_COLOR['End']}
{_CONTENT_SEPERATOR}""")
	try :
		return int(input("Option >>> : "))
	except ValueError:
		return -1

def print_logout():
	print(f"""{_CONTENT_SEPERATOR}
	1. {_COLOR['Red']}Log Out{_COLOR['End']}
	2. {_COLOR['Blue']}Get Token{_COLOR['End']}
	3. {_COLOR['Blue']}Refresh Token{_COLOR['End']}
	4. {_COLOR['Green']}Create User{_COLOR['End']}
	5. {_COLOR['Red']}Delete User{_COLOR['End']}
	6. {_COLOR['Yellow']}Change user Group{_COLOR['End']}
	7. {_COLOR['Blue']}Call API{_COLOR['End']}
	8. {_COLOR['Blue']}Call API{_COLOR['End']} with {_COLOR['Purple']}Authentication {_COLOR['End']}
	9. {_COLOR['Blue']}Call API{_COLOR['End']} with {_COLOR['Purple']}Permission {_COLOR['End']}
	0. {_COLOR['Red']}Exit{_COLOR['End']}
{_CONTENT_SEPERATOR}""")
	try :
		return int(input("Option >>> : "))
	except ValueError:
		return -1

def print_wrong_option_selected():
	print(f"{_COLOR['Red']}Wrong Option{_COLOR['End']} has been selected.")

def get_user():
	global username
	global password
	print(_CONTENT_SEPERATOR)
	username = input("Please Enter the Username\t:")
	password = input("Please Enter the Password\t:")
	print(f"{_COLOR['Yellow']}Username{_COLOR['End']} and {_COLOR['Yellow']}Password{_COLOR['End']} setted successfully.")

def get_user_log():
	username = input("Please Enter the Username\t:")
	password = input("Please Enter the Password\t:")
	password2 = input("Please Re-enter the Password\t:")
	return username, password, password2

def get_username():
	username = input("Please Enter the Username\t:")
	return username

def get_group():
	username = input("Please Enter the Username\t:")
	print("Select either group:")
	print("1: Editor Group")
	print("2. Normal Group")
	group_id = input(f"Option >>> : ")
	return username, group_id

# Main
if __name__ == '__main__':
	general_interface()
