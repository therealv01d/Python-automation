'''
Author: 5m0ky

Description: When we search for a query on google the first thing we do is open the first multiple links before reading through them.
This program automates that. Just add a query (with double quotation mark if there are spaces) and it will open first random links for you to go through.
You can alias the program which will then work as a command in your terminal.

Note: Just a small tool i wrote to automate regular activities. It's not production ready or have many features.
If you want me to add some more features tell me.

MAKE SURE YOU HAVE ALL THE MODULES INSTALLED BEFORE YOU RUN THE PROGRAM !!
'''

#!/usr/bin/env python3
import webbrowser
import random
import requests
import sys
import bs4

def getlinks(final_url):
    links_to_click = []
    res = requests.get(final_url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    for link in soup.find_all('a'):
        hrefs = link.get('href')
        if "/url" in hrefs:
            links_to_click.append(hrefs)
        else:
            pass
    return links_to_click

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n[*] Usage: python main.py facebook")
        print('[*] Usage: python main.py "python programming"')
    else:
        url = "https://google.com/search?q="
        site = "".join([i for i in sys.argv[1:]])
        final_url = url + site

        # First open of web browser
        webbrowser.open(final_url)

        links_to_click = getlinks(final_url)

        counts = random.randint(0, 10)
        for i in range(counts):
            webbrowser.open("http://google.com"+links_to_click[i])
