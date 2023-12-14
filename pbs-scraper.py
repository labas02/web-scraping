from bs4 import BeautifulSoup
from urllib.request import urlopen

article_number1 = 19
article_number2 = 1
link_list = []
with urlopen("https://www.pbs.org/newshour/") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for article in soup.find_all("a",{"class":"card-sm__title"}):
       link_list.append(article.get('href','/')) 
print(link_list)