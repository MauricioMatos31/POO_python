import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Requisição bem-sucedida!")
print(response.status_code)
print(response.json())