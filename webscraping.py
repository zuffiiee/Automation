import requests 
from bs4 import BeautifulSoup

key=input("Enter a keyword:")
print("Googling..")

search_result= requests.get('https://www.google.com/search?q='+key)

# search_result= requests.get('https://www.google.com/search?q='+''.join(sys.argv[1:]))
# search_result.raise_for_status()

soup= BeautifulSoup(search_result.text,'html.parser')
# soup= BeautifulSoup(search_result.text,'lxml')

# aa=soup.select("div.yuRUbf a")
# for a in aa:
# 	print(a.get('href'))

# results=soup.select('a h3')
# for x in results[:10]:
# 	print(x.getText())



# search_links=soup.select('div.yuRUbf a')
# len(search_links)
# for link in search_links:
# 	print(link['href'])

all_links=soup.find_all("div", class_="yuRUbf")
# print(type(all_links))
print(all_links[0])
	



# all_links=soup.select('title')
# print(all_links[0].getText())


# for tag in soup.find_all('a',{'class':"yuRUbf"}):
# 	print(tag.get('href'))

# for link in soup.find_all('a',href=True):
# 	print(link['href'])