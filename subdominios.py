import requests

def response(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    
targer_url = "google.com"
with open('dicc.txt', 'r') as file:
    for line in file.readlines():
        word = line.strip()
        new_url = word + "." + targer_url
        
        data = response("http://" + new_url)
        
        if data:
            print ("[+]Subdominio encontrado ---> " + new_url)
        else:
            print("no se encontro subdominio")
            pass