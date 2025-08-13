# 1. Create and Access List Elements
fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']
print("Third fruit:", fruits[2])
#2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)
#3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("Extracted elements:", new_list)
#4. Convert List to Tuple
movies = ['Inception', 'Interstellar', 'Matrix', 'Avatar', 'Gladiator']
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)
#5. Check Element in a List
cities = ['Tashkent', 'New York', 'Paris', 'Tokyo']
if 'Paris' in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")
  #6. Duplicate a List Without Using Loops

nums = [1, 2, 3]
duplicated = nums * 2
print("Duplicated list:", duplicated)
#7. Swap First and Last Elements of a List
nums = [5, 10, 15, 20, 25]
nums[0], nums[-1] = nums[-1], nums[0]
print("After swapping:", nums)
#8. Slice a Tuple
numbers = tuple(range(1, 11))
sliced = numbers[3:8]
print("Sliced tuple:", sliced)
#9.Count Occurrences in a List
colors = ['blue', 'red', 'blue', 'green', 'blue']
count = colors.count('blue')
print("Number of times 'blue' appears:", count)
#10. Find the Index of an Element in a Tuple
animals = ('cat', 'dog', 'lion', 'tiger')
index = animals.index('lion')
print("Index of 'lion':", index)
#11. Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("Merged tuple:", merged)
#12. Find the Length of a List and Tuple
my_list = [10, 20, 30]
my_tuple = (100, 200, 300, 400)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))
#13. Convert Tuple to List
numbers = (1, 2, 3, 4, 5)
converted = list(numbers)
print("Converted list:", converted)
#14. Find Maximum and Minimum in a Tuple
nums = (10, 5, 25, 1, 8)
print("Max:", max(nums))
print("Min:", min(nums))
#15. Reverse a Tuple
words = ('hello', 'world', 'python', 'code')
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)
