import requests
from lxml import etree
import csv
url = 'https://grammar.izaodao.com/grammar.php?action=list&level=1'

# 一级菜单
'''//div[@class='tableft']/div[@id='TabTab03Con2']//span/a'''

# 二级菜单
'''//div[@class='tableft']/div[@id='TabTab03Con2']/div[@class='sdmenu1']/div/a'''
def grammar_list_get(url):
    res = requests.get(url)
    html = etree.HTML(res.text)

    grammar_list = html.xpath("//div[@class='tableft']/div[@id='TabTab03Con2']//span/a")

    for i in grammar_list:
        title = i.xpath('./text()')[0]
        href = i.xpath('./@href')[0]

        print(title)
        print(href)

        # if href == 'javascript:void(0)':
        # # print(title)
        #     print(href)

        with open('./grammar.csv','a',newline='',encoding='utf-8-sig') as f:
            # f.write(title+'\n')
            csv_writer = csv.writer(f)
            csv_writer.writerow([title,'https://grammar.izaodao.com/grammar.php?action=list&cat={}&level=1'.format(title)])

def grammar_list_make():
    with open('grammar.csv',encoding='utf-8-sig') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            q = ''.join(i)
            href = 'https://grammar.izaodao.com/grammar.php?action=list&cat={}&level=1'.format(q)
            print(href)
            with open('grammar_urls.csv','a',newline='',encoding='utf-8-sig') as f_2:
                csv_writer = csv.writer(f_2)
                csv_writer.writerow([href])

def grammar_content():
    with open('grammar_urls.csv',encoding='utf-8-sig') as f:
        csv_reader = csv.reader(f)
        for href in csv_reader:
            href = href[0]
            print(href)

            name = href.strip('=')
            print(name)

            # '''https://grammar.izaodao.com/grammar.php?action=list&cat=%E6%99%82%E7%82%B9%E3%83%BB%E5%A0%B4%E9%9D%A2'''
            try:
                res = requests.get(href)
                html = etree.HTML(res.text)
                print(html)
            except Exception as e:
                print(e)

            title = html.xpath("//div[@class='list']")
            for k in title:
                content = k.xpath("./a/text()")[0]
                print(content)

                # with open('content.csv','a',newline='',encoding='utf-8-sig') as f:
                #     writer = csv.writer(f)



if __name__ == '__main__':
    grammar_content()