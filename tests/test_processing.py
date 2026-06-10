from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(test_data_processing):
    """Тест фильтрации"""
    result = filter_by_state(test_data_processing, "EXECUTED")
    assert len(result) == 2
    for item in result:
        assert item["state"] == "EXECUTED"

def test_sort_by_date(test_data_processing):  #
    """Тест сортировки"""
    result = sort_by_date(test_data_processing)
    assert result[0]["date"] == "2026-06-14T08:21:33.419441"

def test_sort_by_date2(test_data_processing):  #
    """Тест сортировки"""
    result = sort_by_date(test_data_processing)
    assert result[1]["date"] == "2019-07-03T18:35:29.512364"