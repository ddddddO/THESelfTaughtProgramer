import os
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        self.urls = []
    
    def scrape(self):
        resp = urllib.request.urlopen(self.site)
        html = resp.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None or url[0] != ".":
                continue
            #print("https://news.google.com" + url.lstrip("."))
            self.urls.append("https://news.google.com" + url.lstrip("."))

    def output(self, file_name):
        path = os.path.join(os.getcwd(), file_name)
        with open(path, "w") as f:
            for url in self.urls:
                f.write(url + "\n")

print("start")
news = "https://news.google.com"
scrp = Scraper(news)
scrp.scrape()
scrp.output("urls.txt")
print("end")