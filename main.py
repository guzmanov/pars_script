import os
import requests
from termcolor import colored


f = open("file.txt", "r")
l = []
for x in f:
    l.append(x.rstrip())

for x in l:
    try:
        response = requests.get("https://"+x)
    except requests.exceptions.SSLError as err:
        print(x + colored(" --- BAD SSL", "red"))
        continue

    response = requests.get("https://"+x)
    if response.status_code == 404 and 400:
        print(x + colored(" --- NOT FOUND", "red"))
    elif response.status_code == 500 and 502 and 503 and 504:
        print(x + colored(" --- SERVER ERROR", "red"))
    elif response.status_code == 301 and 302:
        print(x + colored(" --- REDIRECT", "yellow"))
    else:
        print(x +colored("---"+ str(response.status_code), "green"))

print(colored("TOTAL LINKS: " + str(len(l)), "green"))
