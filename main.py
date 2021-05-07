url = "https://bulb.co.uk/tariff/"

import requests

r = requests.post(url, data = {
    'postcode': 'SN8 3AH',
    }
    )
print(r.content)

# # import HTMLSession from requests_html
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
 
# # create an HTML Session object
# session = HTMLSession()
 
# # Use the object above to connect to needed webpage
# resp = session.get(url)
 
# # Run JavaScript code on webpage
# resp.html.render(sleep=2, keep_page=True)

# #print(resp.html.html)

# soup = BeautifulSoup(resp.html.html, "lxml")
# print(soup)
 
# # option_tags = soup.find_all('tr')
 
# # data = [tag.text for tag in option_tags]

# # print(data)

# import requests
# html = requests.get(url).content

# #print(html)

# import bs4
# soup = bs4.BeautifulSoup(html)

# for i in soup.find_all("modal-scroller"):
#     print(i)

# #reomve headers 
# # data = data[1:]


# # for i in range(0,len(data)):
# #     # fix formatting of spaces
# #     data[i] = data[i].replace(' %','%,').split(',')

# #     #print data row
# #     print(data[i],'ben is awesome')