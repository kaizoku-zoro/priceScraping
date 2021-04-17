import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

HTMLcontent = requests.get(url).content
# print(HTMLcontent)

soup = BeautifulSoup(HTMLcontent,'html.parser')

containers = soup.find_all(class_="_2kHMtA")
price=[]
name=[]
for box in containers:
    name.append(box.find(class_="_4rR01T").get_text())
    price.append(box.find(class_="_30jeq3 _1_WHN1").get_text())
# print(name[0])
# print(price[0])
df = pd.DataFrame({'Laptop Name':name,'Price':price})
df.to_csv('laptops.csv',index=False,encoding='utf-8')