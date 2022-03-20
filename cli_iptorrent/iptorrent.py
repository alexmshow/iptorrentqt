import requests

from prettytable import PrettyTable
from bs4 import BeautifulSoup
from sys import argv

user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              'Gecko/20100101 Firefox/50.0')

SITE = "https://iknowwhatyoudownload.com/ru/peer/?ip="


if len(argv) != 2:
    print("Usage:", __file__.split("\\")[-1], "<ipaddress>")
elif len(argv[1].split(".")) == 4:
    r = requests.get(SITE + argv[1], headers={'User-Agent':user_agent})
    soup = BeautifulSoup(r.text, 'html.parser')
    s=soup.find_all("td")
    ptable = PrettyTable()
    ptable.field_names = ["Torrent", "Category", "Size"]
    for i in range(len(s)-1):
        if i%5 == 2:
            try:
                ptable.add_row([s[i+1].text.encode("ISO-8859-1").decode("UTF8").strip(), s[i].text.encode("ISO-8859-1").decode("UTF8"), s[i+2].text.encode("ISO-8859-1").decode("UTF8")])
            except Exception:
                pass
    print(ptable)
        
else:
    print("Usage:", __file__.split("\\")[-1], "<ipaddress>")