import requests
import bs4

page = requests.get('https://www.amazon.eg/s?k=fridge&crid=1MNKLE3EFWB6I&sprefix=fridge%2Caps%2C242&ref=nb_sb_noss_1')
page2 = requests.get('https://www.amazon.eg/s?k=fridge&page=2&crid=1MNKLE3EFWB6I&qid=1671308256&sprefix=fridge%2Caps%2C242&ref=sr_pg_2')
page3 = requests.get('https://www.amazon.eg/s?k=fridge&page=3&crid=1MNKLE3EFWB6I&qid=1671308263&sprefix=fridge%2Caps%2C242&ref=sr_pg_3')
page4 = requests.get('https://www.amazon.eg/s?k=fridge&page=4&crid=1MNKLE3EFWB6I&qid=1671308297&sprefix=fridge%2Caps%2C242&ref=sr_pg_4')
page5 = requests.get('https://www.amazon.eg/s?k=fridge&page=5&crid=1MNKLE3EFWB6I&qid=1671308297&sprefix=fridge%2Caps%2C242&ref=sr_pg_5')
page6 = requests.get('https://www.amazon.eg/s?k=fridge&page=6&crid=1MNKLE3EFWB6I&qid=1671308297&sprefix=fridge%2Caps%2C242&ref=sr_pg_6')
list1 = []

con = page.content + page2.content +page3.content+page4.content+page5.content+page6.content
soub = bs4.BeautifulSoup(con, "html.parser")
products_details = soub.findAll('div', {'class': 'a-section a-spacing-small puis-padding-left-small puis-padding-right-small'})
price = soub.find_all('span' , {'class' : 'a-offscreen'})
rate = soub.find_all('span' , {'class' :'a-size-base'})
product_list = []
price_list =[]
rating_list=[]
for product in range(len(price)):
    product_list.append(products_details[product].text)
    price_list.append(price[product].text)
    rating_list.append(rate[product].text)

for product in range(len(price)):
    print(price_list[product] ,'******' , product_list[product],'******' , rating_list[product])


