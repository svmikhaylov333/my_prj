from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_data_processing: list[dict]) -> None:
    """Тест фильтрации"""
    result = filter_by_state(test_data_processing, "EXECUTED")
    assert len(result) == 2
    for item in result:
        assert item["state"] == "EXECUTED"


def test_sort_by_date(test_data_processing: list[dict]) -> None:  #
    """Тест сортировки по убыванию"""
    result = sort_by_date(test_data_processing)
    assert result[0]["date"] == "2026-06-14T08:21:33.419441"
    assert result[-1]["date"] == "2018-06-30T02:08:58.425572"


def test_sort_by_date_reverse(test_data_processing: list[dict]) -> None:  #
    """Тест сортировки по возрастанию"""
    result = sort_by_date(test_data_processing, False)
    assert result[0]["date"] == "2018-06-30T02:08:58.425572"
    assert result[-1]["date"] == "2026-06-14T08:21:33.419441"
