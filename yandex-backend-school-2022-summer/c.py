import json
from datetime import datetime

json_s = json.loads(input())
filters = dict()
for _ in range(5):
    f, value = input().split()
    filters[f] = value
filters['NAME_CONTAINS'] = filters['NAME_CONTAINS'].lower()
filters['PRICE_GREATER_THAN'] = int(filters['PRICE_GREATER_THAN'])
filters['PRICE_LESS_THAN'] = int(filters['PRICE_LESS_THAN'])
filters['DATE_AFTER'] = datetime.strptime(filters['DATE_AFTER'], '%d.%m.%Y')
filters['DATE_BEFORE'] = datetime.strptime(filters['DATE_BEFORE'], '%d.%m.%Y')
result = []
for product in json_s:
    if filters['NAME_CONTAINS'] not in product['name'].lower():
        continue
    if filters['PRICE_GREATER_THAN'] <= product['price'] <= filters['PRICE_LESS_THAN']:
        if filters['DATE_AFTER'] <= datetime.strptime(product['date'], '%d.%m.%Y') <= filters['DATE_BEFORE']:
            result.append(product)

result.sort(key=lambda item: item['id'])
print(json.dumps(result))
