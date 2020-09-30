from bs4 import BeautifulSoup
import requests
search = input('Enter search term:')
parameters ={'q':search}
r = requests.get('http://www.bing.com/search',params=parameters)

soup = BeautifulSoup(r.text,'html.parser')
results = soup.find('ol',{'id':'b_results'})
links = results.findAll('li',{'class':'b_algo'})
#this is the for loop
for item in links:
    item_text = item.find('a').text
    item_href = item.find('a').attrs['href']


    if item_href or item_text:

        print(item_text)
        print(item_href)
        print('parent',item.find('a').parent)
        print('description', item.find('a').parent.parent.find('p').text)
        children = item.children
        for child in children:
            print('child:', child)
        children1 = item.find('h2')
        print('next sibling is:',children1.next_sibling)
print(soup.prettify())


