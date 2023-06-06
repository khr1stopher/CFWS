import requests as r
import lxml.html as html

HOME_URL = 'https://www.larepublica.co'

XPATH_LINKS = '//text-fill/a/@href'
XPATH_TITLE_ARTICLES = '//h2/span/text()'
XPATH_DESCRIPTION_ARTICLES = '//div[@class="lead"]/p/text()'
XPATH_CONTENT_ARTICLES = '//div[@class="html-content"]/p[not(@class)]/text()'

def parce_home():
    try:
        response = r.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_articles = parsed.xpath(XPATH_LINKS)
            print(links_to_articles)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parce_home()

if __name__ == '__main__':
    run()