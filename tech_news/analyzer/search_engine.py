from tech_news.database import search_news
from datetime import datetime


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
    try:
        filter = datetime.fromisoformat(date).strftime('%d/%m/%Y')
        filtered_news = search_news(
            {"timestamp": filter}
        )

        result = []

        for news in filtered_news:
            result.append((news['title'], news['url']))

        return result

    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
