import requests
from lxml import etree

url = 'https://grammar.izaodao.com/grammar.php?action=list&cat=%時点・場面&level=1'
# header = {
#         'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
#         'Host': "https://grammar.izaodao.com/",
# }
res = requests.get(url)

print(res.text)