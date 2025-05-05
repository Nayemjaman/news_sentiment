import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_html(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def parse_prothomalo(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select_one("h2 a, h3 a")

def parse_kalerkantho(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select_one('h2.title') or soup.find('h1')

def parse_bd_pratidin(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('h1') or soup.find('h2')

def get_first_headline(url):
    try:
        print("-------------------------")
        print("Fetching URL:", url)
        html = fetch_html(url)

        if "prothomalo" in url:
            headline_tag = parse_prothomalo(html)
        elif "kalerkantho" in url:
            headline_tag = parse_kalerkantho(html)
        elif "bd-pratidin" in url:
            headline_tag = parse_bd_pratidin(html)
        else:
            return "Invalid or unsupported URL."

        headline = headline_tag.text.strip() if headline_tag else "No headline found."
        print("Headline:", headline)
        return headline

    except Exception as e:
        return f"Error: {str(e)}"





# headline = soup.select_one(".lead_news h2 a, .lead_news h1 a")
