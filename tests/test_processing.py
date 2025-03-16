import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date

@pytest.fixture
def state_list_value():
    state_list = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                  {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                  {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                  {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                  {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
    return state_list


@pytest.mark.parametrize('state, expected',[('EXECUTED', [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                            {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]),
                                            ("CANCELED", [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}])])
def test_filter_by_state(state_list_value,expected, state):
    assert filter_by_state(state_list_value, state=state) == expected


def test_filter_by_invalid_state():
    with pytest.raises(ValueError):
        filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                  {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                  {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                  {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                  {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], state='EXsdasdaECUTEDsss')


@pytest.mark.parametrize('reverse, expected',[(True, [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                                      {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                                      {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                                      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                      {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]),
                                              (False, [ {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                        {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                                        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                                        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}])])
def test_sort_by_date(state_list_value,expected,reverse):
    assert sort_by_date(state_list_value, reverse=reverse) == expected


@pytest.mark.parametrize("invalid_date", [({"id": 41428829, "state": "EXECUTED", "date": "2025-07-03"},
                                          {"id": 615064591, "state": "CANCELED", "date": "18:35:29.512364"},
                                          {"id": 939719571, "state": "EXECUTED", "date":"03-07-2019T18:35:29"})])
def test_sort_by_invalid_date(invalid_date):
    with pytest.raises(ValueError):
        sort_by_date(invalid_date)