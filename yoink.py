from requests import get
from bs4 import BeautifulSoup as BS
import re


print('********Use https:// or http://********')
targeturl = input('Yoink URL =')
url = targeturl

response = get(url)
targeturlwords = BS(response.content, "html.parser")
#for child in targeeturlwords.body.children:
#   if child.name == 'script':
#       child.decompose()
words = re.sub(r'\n\s*\n', r'\n\n', targeturlwords.get_text().strip(), flags=re.M)

#print(soup.body.get_text())
#print(soup.a.prettify())
#print(soup.find().get_text().stuff)
print(words)
print('*** END YOINK ***')
