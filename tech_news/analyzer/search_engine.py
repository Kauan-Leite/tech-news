from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    data = search_news(
        {"title": {"$regex": title, "$options": "i"}})

    result = []

    for info in data:
        result.append((info['title'], info['url']))

    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
