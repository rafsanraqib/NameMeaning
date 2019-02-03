from googlesearch import search
import requests
from bs4 import BeautifulSoup
#Stores the Url
def meaning(n):
    url = "https://www.urbandictionary.com/define.php?term="+ n
    resp = requests.get(url)
    parser = BeautifulSoup(resp.text, 'html.parser')
    clss = parser.find("div", {"class" : "meaning"})
    for i in clss.findAll("a"):
        print(i.text)
while True:
    UserInput = input()
    if UserInput == "quit":
        break
    else:
        meaning(UserInput)
        continue
