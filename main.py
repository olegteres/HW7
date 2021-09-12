from pprint import pprint

def cookbook(file_name: str) -> dict:
    result: dict = dict()
    with open("CookBook.txt", "r", encoding="utf-8") as file:
        for line in file:
            dish_name = line.strip()
            ingredients_quantity = int(file.readline())
            ingredients_list = []
            for ingredient in range(ingredients_quantity):
                ingredient_name, quantity, measure = file.readline().strip().split("|")
                ingredients_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
            result[dish_name] = ingredients_list
            file.readline()
    return result

result_cookbook = cookbook("CookBook.txt")
pprint(result_cookbook)
print()

def get_shop_list_by_dishes(dishes, persons=int):
    menu = cookbook("CookBook.txt")
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    shopping_list.update(items_list)

        print(f"Для приготовления {dishes} на {persons} человек нужно купить:")
        pprint(shopping_list)
    except KeyError:
        print("Такого рецепта нет")

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print()

files_dict = {}

with open("1.txt", "r", encoding="utf-8") as file:
    files_dict["1.txt"] = len(file.readlines())
with open("2.txt", "r", encoding="utf-8") as file:
    files_dict["2.txt"] = len(file.readlines())
with open("3.txt", "r", encoding="utf-8") as file:
    files_dict["3.txt"] = len(file.readlines())


sorted_keys = sorted(files_dict, key=files_dict.get)
for w in sorted_keys:
    print(w)
    print(files_dict[w])
    with open(w, "r", encoding="utf-8") as file:
        print(file.read())



#for key in sorted_dict:
    #print(key)
    #with open(key, "r", encoding="utf-8") as file:
        #print(file.read())





