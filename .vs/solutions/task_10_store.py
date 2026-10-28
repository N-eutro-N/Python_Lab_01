GOODS = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

STORE = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def stock_report(goods, store):
    report = []
    for name, code in goods.items():
        quantity = sum(lot['quantity'] for lot in store[code])
        cost = sum(lot['quantity'] * lot['price'] for lot in store[code])
        report.append(f'{name} - {quantity} шт, стоимость {cost} руб')
    return report


if __name__ == '__main__':
    for line in stock_report(GOODS, STORE):
        print(line)
