from bs4 import BeautifulSoup
import requests
import re
from googlesearch import search
import time

blocked_URLS = [
    "yelp.com",
    'maps.google.com',
    "facebook.com",
    "instagram.com",
    "twitter.com",
    "linkedin.com",
    "yellowpages.com",
    "bbb.org",
]
queries = ["metal fabrication orlando"]
def scrapeEmails(URL):
    assert isinstance(URL, str), "TYPE ERROR: expected string"
    pageToScrape = requests.get(URL)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    raw_refs = soup.find_all('a', href=True)
    for raw_ref in raw_refs:
        found_email = raw_ref.find_all(string=re.compile(r"@"))
        #potential_emails = found.parent
        if len(found_email) > 0:
            print(found_email[0])
        if "tel:" in raw_ref["href"]:
            print(str(raw_ref["href"]).replace("tel:", ""))
def scrapeURLs(queries, amount_to_collect):
    """Scrapes for URLs for a given list of queries. NOTE: If amount_to_collect is greater than 100, Google may block"""
    urls = set()
    for query in queries:
        print(f"Searching: {query}")
        for url in search(query, num_results=amount_to_collect, sleep_interval=2, timeout=5):
            print("found", url)
            urls.add(url)
    return urls

if __name__ == "__main__":
    urls = scrapeURLs(queries, 10)
    print(urls)