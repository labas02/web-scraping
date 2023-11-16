from bs4 import BeautifulSoup

h2 = "cc"
with open('index.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")

    print(soup.h2)
    print(soup.p)
    print(soup.li)
    h2 = soup.h2
    f.close()

    with open("text.txt", "w") as f:
        f.writelines("**********star of scrape**********\n")
        f.writelines(h2)
        f.writelines("\n")
        f.writelines("***********end of scrape**********\n")