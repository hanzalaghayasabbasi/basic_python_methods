import requests
import json

v=input("Enter new which you are intersted : ")
url=f"https://newsapi.org/v2/everything?q={v}&from=2023-06-09&to=2023-06-09&sortBy=popularity&apiKey=81cf0a0d47db47a78d4bead2a5f6b7e7"

r=requests.get(url)
news= json.loads(r.text)

#soup=BeautifulSoup(r.text,"html.parser")
#print(soup.prettify())
k=1
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print(f"---------------NEWS{k}---------------------")
  print("--------------------------------------------")
  print("--------------------------------------------")
  k+=1

#soup=BeautifulSoup(r.text,"html.parser")

#i=1
#for heading in soup.find_all("li"):
 # print("News {0}".format(i)) 
  #i=i+1
  #print(heading.text,"\n\n\n")

