import requests
import json

query = '回锅肉'


def download(src, name):
    file = './images/%s.jpg' % (str(name),)
    try:
        pic = requests.get(src, timeout=10)
        fp = open(file, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('can not download')


for i in range(0, 22471, 20):
    url = 'https://www.douban.com/j/search_photo?q=%s&limit=20&start=%s' % (query, str(i))
    html = requests.get(url).text
    response = json.loads(html, encoding='utf-8')
    for image in response['images']:
        print(image['src'])
        download(image['src'], image['id'])
