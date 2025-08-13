my_dict = {'a': 3, 'b': 1, 'c': 2}
ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending:", ascending)
descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", descending)
# 2. Add a Key to a Dictionary
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Updated Dictionary:", my_dict)
#3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
merged = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", merged)
# 4. Generate a Dictionary with Squares (1 to n)
n = 5
squares = {}
for x in range(1, n + 1):
    squares[x] = x * x
print("Squares Dictionary:", squares)
# 5. Dictionary of Squares (1 to 15)
squares_15 = {x: x * x for x in range(1, 16)}
print("Squares from 1 to 15:", squares_15)

# 1. Create a Set
my_set = {1, 2, 3, 4, 5}
print("Yaratilgan set:", my_set)
# 2. Iterate Over a Set
for item in my_set:
    print("Set element:", item)
# 3. Add Member(s) to a Set
my_set.add(6)
my_set.update([7, 8])
print("Yangilangan set:", my_set)
# 4. Remove Item(s) from a Set
my_set.remove(3)
print("3 o‘chirildi:", my_set)
# 5. Remove an Item if Present in the Set
item_to_remove = 4
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"{item_to_remove} setdan o‘chirildi")
else:
    print(f"{item_to_remove} setda yo‘q")
