#WEB SCRAPING
import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://codegnan.com"
response=requests.get(url)
print(response)
print(response.status_code)
print(response.text[:500])
#BeautifulSoup
soup=BeautifulSoup(response.text,"html.parser")
print(soup.title)
print(soup.title.text)
heading=soup.find_all("h1")
for i in heading:
    print(i.text)
url2="https://timely-sunshine-e821b3.netlify.app/"
page=requests.get(url2)
print(page.status_code)  #to check status
htmlCode=page.text
soup2=BeautifulSoup(htmlCode,"html.parser")
items = soup2.find_all('div', class_='a')
#extracting data
names=[]
prices=[]
for item in items:
    name=item.find('div',class_='name').text.strip()
    price=item.find('div',class_='price').text.strip()
    names.append(name)
    prices.append(price)
df=pd.DataFrame({
    'pname':names,
    'mrp':prices
})
print("Scrapped Data")
print(df)