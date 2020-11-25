#3.14
def trocaPU(list):
    """This function switches the first and last items in a list"""
    list[0], list[-1] = list[-1], list[0]
    return list

ingredients = []
n = eval(input("Enter the number of ingredients: "))
for i in range(n):
    item = input("Item {}: ".format(i + 1))
    ingredients.append(item)

print(trocaPU(ingredients))
