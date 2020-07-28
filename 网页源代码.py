import requests
url = input()
strhtml = requests.get(url)
print(strhtml.text)