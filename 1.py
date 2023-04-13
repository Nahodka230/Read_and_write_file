from pprint import pprint
with open('cook_book.txt', 'rt', encoding='utf-8') as file:
    dishes = {}
    for line in file:
        dish_name = line.strip()
        ingred_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingred_count):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            ingredients.append(
                {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
                }
            )
        file.readline()
        dishes[dish_name] = ingredients
    #pprint(dishes, sort_dicts=False)
    def get_shop_list_by_dishes(dishes_list, person_count):
        ingredient_dict = {}
        for dish in dishes_list:
            ingredient_list = dishes[dish]
            for ingredient in ingredient_list:
                count_ing_to_per = person_count * int(ingredient['quantity'])
                name_ingredient = ingredient['ingredient_name']
                keys = list(ingredient_dict.keys())
                if name_ingredient in keys:
                    a_dict = ingredient_dict[name_ingredient]
                    new_count = int(a_dict['quantity'])+count_ing_to_per
                    ingredient_dict[name_ingredient] = {'measure': ingredient['measure'], 'quantity': new_count}
                else:
                    ingredient_dict[name_ingredient] = {'measure': ingredient['measure'], 'quantity': count_ing_to_per}
        pprint(ingredient_dict)


    get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5)