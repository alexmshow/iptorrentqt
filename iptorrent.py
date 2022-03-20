import requests

from bs4 import BeautifulSoup

def main(ipaddress):
    user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
                'Gecko/20100101 Firefox/50.0')

    SITE = "https://iknowwhatyoudownload.com/ru/peer/?ip="

    r = requests.get(SITE + ipaddress, headers={'User-Agent':user_agent})
    soup = BeautifulSoup(r.text, 'html.parser')
    s=soup.find_all("td")

    for i in range(len(s) - 1):
        if i%5 == 2:
            try:
                yield (s[i+1].text.encode("ISO-8859-1").decode("UTF8").strip(), s[i].text.encode("ISO-8859-1").decode("UTF8"), s[i+2].text.encode("ISO-8859-1").decode("UTF8"))
            except Exception: pass