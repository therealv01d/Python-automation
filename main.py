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
