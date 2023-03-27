from utils import refactor_date, mask_card, format_data, filter_sort


def test_ref_date():
    assert refactor_date('2019-07-03T18:35:29.512364') == '03.07.2019'
    assert refactor_date('2018-06-30T02:08:58.425572') == '30.06.2018'


def test_mask_card():
    assert mask_card('Счет 75106830613657916952') == 'Счет **6952'
    assert mask_card('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert mask_card(None) == ''


def test_format_data():
    data = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
          "amount": "9824.07",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
      }
    result = '30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD'

    assert format_data(data) == result


def test_filter_sort():
    data = [
        {
            'id': 3,
            'state': 'Open',
            'date': '2018-06-30T02:08:58.425572'
        },
        {
            'id': 23,
            'state': 'EXECUTED',
            'date': '2023-06-30T02:08:58.425572'
        },
        {
            'id': 5,
            'state': 'EXECUTED',
            'date': '2022-06-30T02:08:58.425572'
        }
    ]

    result = {
            'id': 3,
            'state': 'Open',
            'date': '2018-06-30T02:08:58.425572'
        },\
        {
            'id': 5,
            'state': 'EXECUTED',
            'date': '2022-06-30T02:08:58.425572'
        }
    assert filter_sort(data) == result
