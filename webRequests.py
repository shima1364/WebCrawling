import requests
from bs4 import BeautifulSoup

url_site = "https://www.ebay.de/sch/i.html?_from=R40&_nkw=iphone+14+pro+max&_sacat=0&Speicherkapazit%25C3%25A4t=256%2520GB&_dcat=9355"

site = requests.get(url_site)
soup = BeautifulSoup(site.text, 'html.parser')

div1 = soup.find('div', {'class': 'srp-river-results clearfix'})

div2 = div1.find_all('div', {'class': "s-item__detail s-item__detail--primary"})

for item in div2:
    title_span = item.find('span', {'class': 's-item__price'})
    if title_span:
        title_text = title_span.text.strip()
        print(title_text)
    else:
        print("Title not found")
#
#print(div2)
# # print('--------------------------------')
#print(div2)
#print(div2[1])

print(div2[0].find('span').text)
# print(len(div2))
#titles = []
#descriptions = []
#prices = []
# # #
# for item in range(len(div2)):
#   title = div2[item].find('h2').text
#  titles.append(title.replace('\n', '').replace(',', ' '))

#  description = div2[item].find_all('div', {'kt-post-card__description'})[0].text
# descriptions.append(description.replace('\n', '').replace(',', ' '))
#
# price = div2[item].find_all('div', {'kt-post-card__description'})[1].text
# prices.append(int(price.replace('\n', '').replace(',', '').replace('تومان', '')))
#
# print(titles)
# print(descriptions)
# print(prices)
# #
# myDictionary = {
#   'Title': titles,
#  'Description': descriptions,
# 'Price': prices
# }
# df = pd.DataFrame(myDictionary)
# df.to_csv('divarMobileList.csv')
# # # #
# divarDataList = pd.read_csv('divarMobileList.csv')
# print(divarDataList.columns)
# print(divarDataList.shape)
# print(divarDataList.head())
# print(divarDataList.to_string())
# print('-------------------------------------------------------------')
