import requests

def response(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

lista = []

    
targer_url = "google.com"
with open('dicc.txt', 'r') as file:
    for line in file.readlines():
        word = line.strip()
        #Encontrar subdominios
        #new_url = word + "." + targer_url
        
        #Encontrar folders
        new_url = targer_url + "/" + word
        
        data = response("http://" + new_url)
        
        if data:
            lista.append(new_url)
            print ("[+]Subdominio encontrado ---> " + new_url)
        else:
            print("no se encontro subdominio")
            pass


if lista:
        print("--------------------------")
        print("Subdominios encontrados:")
        print(lista)
        print("--------------------------")
else:
        print("no se encontro subdominio")
        pass
    