import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501

NEWS_MOCK = {
    'readable': [
        {'unfilled_time': 2, 'chosen_news': [('Notícia bacana 2', 1)]}
        ],
    'unreadable': [('Notícia bacana', 4)]
    }


def test_reading_plan_group_news():
    valid = ReadingPlanService.group_news_for_available_time(3)
    assert valid == NEWS_MOCK

    assert len(valid['readable']) == 1
    assert len(valid['unreadable']) == 1

    with pytest.raises(
            ValueError,
            match="Valor 'available_time' deve ser maior que zero"):
        ReadingPlanService.group_news_for_available_time(-99)
