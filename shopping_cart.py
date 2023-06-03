import datetime

greetings = "Welcome to May's shopping cart application"
print(greetings)

current_datetime = datetime.datetime.now()
print(current_datetime)
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
print('Current date and time: {}-{} \ {}:{}'.format(month, day, hour, minute))

# print("{}-{} \ {}:{}" .format(month, day, hour, minute))
# print(str(month) + "/" + str(day) +  str(hour) + "/" + str(minute))

shopping_list = ["Cheese", "Meat"]

while len(shopping_list) < 6:
    new_items = input("Add more items to your list: \n").title()
    shopping_list.append(new_items)
print("Your shopping list:\n", shopping_list)

shopping_list.sort()
shopping_item = len(shopping_list)
print("Items added to cart is :" + " " + str(len(shopping_list)) + " and they include " + str(shopping_list))
# print("Items added to cart is", len(shopping_list), "and they include", shopping_list)
#
# output = "Items added to cart: is {} {}".format(len(shopping_list), " ".join(shopping_list))
# print("Items added to cart is", len(shopping_list), "and they include :\n", ", ".join(sorted(shopping_list)))

# print(output)

shopping_order = "My items bought arranged in alphabetical order: \n" + str(shopping_list)
print(shopping_order)
# shopping_order = "my items items bought arranged in alphabetical order: " + str(shopping_list)
# shopping_order = "My items bought arranged in alphabetical order: \n" + ", ".join(sorted(shopping_list))


shopping_budget = input("enter items on the shopping cart you will like to remove: \n").title()
shopping_list.remove(shopping_budget)
items_remaining = "These are the items remaining: \n"
print(items_remaining + str(shopping_list))

# shopping_list.remove("Beans")
# shopping_budget = "Cutting cost by subtracting an item from my list: " + ", ".join(sorted(shopping_list))
# # shopping_budget = "Cutting cost by subtracting an item from my list: " + str(shopping_list)
# print(shopping_budget)

# shopping_budget = shopping_list.copy()
# shopping_budget.remove("beans")
# print("Cutting cost by subtracting certain items from my list:", shopping_budget)

# shopping_budget = "Cutting cost by subtracting an  item from my list: " + str(shopping_list.remove("beans"))
# print(shopping_budget)
# shopping_budget.remove("beans")
# print("Cutting cost by subtracting certain items from my list:", sorted(shopping_budget))
