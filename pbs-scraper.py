from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

article_number1 = 19
article_number2 = 1
link_list = []
with urlopen("https://www.pbs.org/newshour/") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for article in soup.find_all("a",{"class":"card-sm__title"}):
       link_list.append(article.get('href','/')) 

number_tmp = 0
for links in link_list:
    write_article_row = []
    number_tmp += 1
    print(number_tmp)
    
    with urlopen(link_list[number_tmp]) as fp2:
        soup_too = BeautifulSoup(fp2, "html.parser")
        article_title_list = soup_too.find_all('h1',class_='post__title')
          
        for article in article_title_list:
            write_article_row.append(article.get_text())

            with open('training_dataset.csv', 'a', newline='') as f:
               writer = csv.writer(f)
               writer.writerow(write_article_row)