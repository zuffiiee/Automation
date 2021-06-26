import requests,bs4

search_key=input("Enter a keyword:").strip().replace(' ', '+')

print("Googling....\n")
url = 'https://google.com/search?q=' + search_key
headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
result = requests.get(url,headers=headers)

soup=bs4.BeautifulSoup(result.text,'lxml')

beeh=soup.select('a[href^="https"]')
for x in beeh:
    if x.find('h3'):
        heading=x.select("h3")
        print(heading[0].getText())
        print(x['href']+'\n')
