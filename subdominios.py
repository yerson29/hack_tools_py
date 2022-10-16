import requests

def response(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
<<<<<<< HEAD

lista = []
=======
>>>>>>> 520ce34a7f867c1d64d429132ca9bbec89672d87
    
targer_url = "google.com"
with open('dicc.txt', 'r') as file:
    for line in file.readlines():
        word = line.strip()
        new_url = word + "." + targer_url
        
        data = response("http://" + new_url)
        
        if data:
<<<<<<< HEAD
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
        pass
=======
            print ("[+]Subdominio encontrado ---> " + new_url)
        else:
            print("no se encontro subdominio")
            pass
>>>>>>> 520ce34a7f867c1d64d429132ca9bbec89672d87
