import requests
from lxml import etree
import csv

def get_info():

    for i in range(1,20):
        url = 'http://grammar.izaodao.com/grammar.php?action=list&op=ajaxMoreList&level=4&page={}'.format(i)
        res = requests.get(url)

        html = etree.HTML(res.text)

        title = html.xpath("//div[@class='list']")

        for k in title:

            content = k.xpath("./a/text()")[0]
            id = k.xpath("./@onclick")[0].split(r'=')[3].split(r'&')[0]
            id = int(id)
            print(content)
            print(id)

            info_url = r'http://grammar.izaodao.com/grammar.php?action=view&id={}&level=&level=4'.format(id)

            infos = requests.get(info_url)
            html = etree.HTML(infos.text)

            title = html.xpath("//div[@class='box1']/span/text()")
            title = ''.join(title)

            content = html.xpath("//div[@class='box2']//text()")
            content = "".join(content)
            content = "".join([s for s in content.splitlines(True) if s.strip()])
            content = content.replace(' ','').replace('	','')
            print(content)

            with open('n4.csv','a',newline='',encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([title,content,'N4'])



if __name__ == "__main__":
    get_info()