def reader():
    def to_number(n):
        if n.isdigit():
            return int(n)
        else:
            try:
                return float(n)
            except ValueError:
                return n

    return tuple(map(to_number, input().split()))


def convert(value, _unit):
    if _unit in ('kg', 'l'):
        value *= 1000
    elif _unit == 'tens':
        value *= 10
    return value


all_ingredients = {}
dishes = {}
price_menu = {}
food_menu = {}
dishes_qty = {}
dish_number, = reader()
for _ in range(dish_number):
    dish, friends, ingredients_number, = reader()
    dishes[dish] = {}
    for _ in range(ingredients_number):
        ingredient, qty, unit, = reader()
        qty = convert(qty, unit) * friends
        dishes_qty[dish] = friends
        dishes[dish][ingredient] = qty
        prev_value = all_ingredients.setdefault(ingredient, 0)
        all_ingredients[ingredient] = prev_value + qty
ingredients_number_in_price_menu, = reader()
for _ in range(ingredients_number_in_price_menu):
    ingredient_name, price, qty, unit, = reader()
    qty = convert(qty, unit)
    price_menu[ingredient_name] = {'price': price, 'qty': qty, 'unit': unit}
ingredients_number_in_food_menu, = reader()
for _ in range(ingredients_number_in_food_menu):
    ingredient_name, qty, unit, pr, f, ch, fv, = reader()
    # pr, f, ch, fv = convert(pr, unit), convert(f, unit), convert(ch, unit), convert(fv, unit)
    food_menu[ingredient_name] = {'qty': convert(qty, unit), 'unit': unit, 'pr': pr, 'f': f, 'ch': ch, 'fv': fv}

sum_price = 0
shopping_list = {}
dish_specification = {}
for ing, qty in all_ingredients.items():
    packs_number = (qty // price_menu[ing]['qty']) + (1 if qty % price_menu[ing]['qty'] else 0)
    shopping_list[ing] = packs_number
    sum_price += packs_number * price_menu[ing]['price']

print(sum_price)
for ing in price_menu:
    if ing not in shopping_list:
        print(ing, 0)
    else:
        print(ing, shopping_list[ing])

for dish in dishes:
    pr, f, ch, fv = 0, 0, 0, 0
    for ing, qty in dishes[dish].items():
        _qty = (qty / food_menu[ing]['qty']) / dishes_qty[dish]
        pr += _qty * food_menu[ing]['pr']
        f += _qty * food_menu[ing]['f']
        ch += _qty * food_menu[ing]['ch']
        fv += _qty * food_menu[ing]['fv']
    print(dish, round(pr, 3), round(f, 3), round(ch, 3), round(fv, 3))
