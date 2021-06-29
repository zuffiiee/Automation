import requests,bs4,csv

# Creating a csv file
op_file=open('links.csv',mode='w',newline='')
csv_writer=csv.writer(op_file,delimiter=',')
csv_writer.writerow(['Rank','Name','URL Address'])



search_key=input("Enter a keyword:").strip().replace(' ', '+')

print("Googling....\n")
url = 'https://google.com/search?q=' + search_key +'&num=100'
headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
result = requests.get(url,headers=headers)

soup=bs4.BeautifulSoup(result.text,'lxml')

beeh=soup.select('a[href^="http"]')     #changed https to http

rank=0
for x in beeh:
    if x.find('h3'):
        rank+=1
        heading=x.select("h3")
        csv_writer.writerow([rank,heading[0].getText(),x['href']])
print("CSV file has been created")
op_file.close()