import requests
from lxml import etree
import json
import jsonpath
from selenium import webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

for i in range(10):
    i = i*10
    header = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
        'Host': "www.zhihu.com",
    }

    url = 'https://www.zhihu.com/api/v4/columns/c_1289785392477261824/items?limit=10&offset={}'.format(i)
    res = requests.get(url,headers=header)

    html = res.text

    html = json.loads(html)

    url = jsonpath.jsonpath(html,'$..url')
    # title = jsonpath.jsonpath(html,'$..title')
    url = url[::3]

    for i in url:
        print(i)

        driver.get(i)
        html = driver.page_source

        html = etree.HTML(html)

        title = html.xpath("//h1/text()")[0]
        content = html.xpath("//div[@class='Post-RichTextContainer']//p/text()")
        content = '\n'.join(content)

        print(title,content)

        with open('poems','a+') as f:
            f.write(i+'\n')
            f.write(title+'\n')
            f.write(content+'\n')