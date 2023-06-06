import requests as r
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www.larepublica.co'

XPATH_LINKS = '//text-fill/a/@href'
XPATH_TITLE_ARTICLES = '//h2/span/text()'
XPATH_DESCRIPTION_ARTICLES = '//div[@class="lead"]/p/text()'
XPATH_CONTENT_ARTICLES = '//div[@class="html-content"]/p[not(@class)]/text()'

def parce_notice(link, date):
    try:
        response = r.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)
            try:
                title = parsed.xpath(XPATH_TITLE_ARTICLES)[0]
                title = title.replace('\"', '').strip()
                summary = parsed.xpath(XPATH_DESCRIPTION_ARTICLES)[0]
                body = parsed.xpath(XPATH_CONTENT_ARTICLES)
                
                with open(f'{date}/{title}.txt', 'w', encoding='utf-8') as file:
                    file.write(title)
                    file.write('\n\n')
                    file.write(summary)
                    file.write('\n\n')
                    for p in body:
                        file.write(p)
                        file.write('\n')
            except IndexError:
                return
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parce_home():
    try:
        response = r.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_articles = parsed.xpath(XPATH_LINKS)
            # print(links_to_articles)
            today = datetime.date.today().strftime('%d-%m-%y')
            if not os.path.isdir(today):
                os.mkdir(today)
                for link in links_to_articles:
                    parce_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parce_home()

if __name__ == '__main__':
    run()