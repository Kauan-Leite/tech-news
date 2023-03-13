import re
import requests
from parsel import Selector
from time import sleep


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )

        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    url_news = selector.css('.cs-overlay-link::attr(href)').getall()
    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css('.next::attr(href)').get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('.entry-title::text').get()
    timestamp = selector.css('.meta-date::text').get()
    writer = selector.css('.author a::text').get()

    read = selector.css('.meta-reading-time::text').get()
    reading_time = ''

    for caractere in read:
        if caractere.isdigit():
            reading_time += caractere

    first_paragraph = selector.css('.entry-content p').get()
    selector_paragraph = Selector(text=first_paragraph)
    all_text = selector_paragraph.css('*::text').getall()
    summary = ''
    for text in all_text:
        summary += text

    title = re.sub('<.*?>', '', title).strip()
    summary = re.sub('<.*?>', '', summary).strip()

    category = selector.css('.category-style .label::text').get()
    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': int(reading_time),
        'summary': summary,
        'category': category,
        }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
