from utils import refactor_date, mask_card, format_data, filter_sort
import pytest


@pytest.mark.parametrize('str_date, corr_date', [('2018-10-14T08:21:33.419441', '14.10.2018')])


def test_ref_date(str_date, corr_date):
    assert refactor_date(str_date) == corr_date


@pytest.mark.parametrize('str_card, mask', [('Maestro 4598300720424501', 'Maestro 4598 30** **** 4501'),
                                            ('Счет 43597928997568165086', 'Счет **5086')])
def test_ref_date(str_card, mask):
    assert mask_card(str_card) == mask


def test_format_data():
    data = {
        "id": 542678139,
        "state": "EXECUTED",
        "date": "2018-10-14T22:27:25.205631",
        "operationAmount": {
          "amount": "90582.51",
          "currency": {
            "name": "USD",
            "code": "USD"
           }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 2256483756542539",
        "to": "Счет 78808375133947439319"
      }

    result = '14.10.2018 Перевод организации\nVisa Platinum 2256 48** **** 2539 -> Счет **9319\n90582.51 USD'
    assert format_data(data) == result


def test_filter_sort():
    data = [
        {
            'id': 3,
            'state': 'Open',
            'date': '2019-11-05T12:04:13.781725'
        },
        {
            'id': 23,
            'state': 'EXECUTED',
            'date': '2023-11-05T12:04:13.781725'
        },
        {
            'id': 5,
            'state': 'EXECUTED',
            'date': '2022-11-05T12:04:13.781725'
        }
    ]

    result = [
        {
            'id': 5,
            'state': 'EXECUTED',
            'date': '2022-11-05T12:04:13.781725'
        },
        {
            'id': 23,
            'state': 'EXECUTED',
            'date': '2023-11-05T12:04:13.781725'
        }
    ]

    assert filter_sort(data) == result

