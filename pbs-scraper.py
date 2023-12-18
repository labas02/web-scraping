from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd
article_number1 = 19
article_number2 = 1
link_list = []

data = pd.read_csv('training_dataset.csv')

title_check = data['title'].tolist()
def check_titles(current_title):
    for x in title_check:
      if current_title == x:
        return True  
    return False   

with urlopen("https://www.pbs.org/newshour/latest/") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for article in soup.find_all("a",{"class":"card-timeline__title"}):
       link_list.append(article.get('href','/')) 

number_tmp = 0
for links in link_list:
    write_article_row = []
    article_body_text = ""
    number_tmp += 1
    print(number_tmp)
    
    with urlopen(link_list[number_tmp]) as fp2:
        soup_too = BeautifulSoup(fp2, "html.parser")
        article_title_list = soup_too.find_all('h1',class_='post__title')
        article_body_list = soup_too.find_all('div',class_='body-text')

        for article in article_title_list:
          title = article.get_text()
          if check_titles(title) == False:
                for articles in article_body_list:
                    article_body_tmp = articles.find_all('p')
                    for x in article_body_tmp:
                        article_body_text = article_body_text + x.get_text()

                write_article_row.append(article.get_text())
                write_article_row.append(article_body_text)

                with open('training_dataset.csv', 'a', newline='') as a:
                          writer = csv.writer(a)
                          writer.writerow(write_article_row) 
          else:
            break
