from googlesearch import search
import requests
from bs4 import BeautifulSoup
#Stores the Url
def meaning(n):
    url = "https://www.urbandictionary.com/define.php?term="+ n
    resp = requests.get(url)
    parser = BeautifulSoup(resp.text, 'html.parser') #parses the HTML file
    clss = parser.find("div", {"class" : "meaning"}) #looks for the class meaning in the HTML code
    for i in clss.findAll("a"):                      #Finds all anchor elements in the HTML code
        print(i.text)                                #Prints all the text corresponding the meaning class
while True:
    UserInput = input()
    if UserInput == "quit":
        break
    else:
        meaning(UserInput)
        continue
