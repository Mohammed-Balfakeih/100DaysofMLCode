import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import json

url_a = 'https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q=a+mouse'
url_b = '\&tbm=isch&ved=0ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ&start={}'
url_c = '\&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg'
url_d = '\.i&ijn=1'
url_base = ''.join((url_a, url_b, url_c, url_d))
print(url_base)

headers = {'User-Agent': 'Chrome/69.0.3497.100'}

def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name, 0)
    request = ulib.Request(url, data=None, headers=headers)
    json_string = ulib.urlopen(request).read()
    print(json_string)
    page = json.loads(json_string)
    new_soup = Soup(page[1][1], 'lxml')
    images = new_soup.find_all('img')
    links = [image['src'] for image in images]
    return links

if __name__ == '__main__':
    search_name = 'Thumbs up'
    links = get_links(search_name)

    for link in links:
        print(link)