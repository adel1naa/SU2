##zadacha1
number = input("Enter an integer:")
print(number)

##zadacha2
import random
numbers = []
for i in range(5):
    numbers.append(random.randint(1, 10))
print("Original list:",  numbers)
new_numbers = []
for i in range(len(numbers) -1):
        new_numbers.append(numbers[i])
        new_numbers.append(numbers[i]+ numbers[i = 1])
new_numbers.append(numbers[-1])

print("New list",new_numbers)

##zadacha3
text = input("Enter text:")
count = {}
for letter in text:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print(count)

##zadacha4
n = int(input("Enter n:"))
numbers = list(range(1, n+1))
result = {}
for i in range(n):
     result[numbers[i]] = numbers[n - 1 -i]
print(numbers)
print(result)

##zadacha5
numbers = list(map(int, input("Enter numbers: ").split()))

smallest = min(numbers)
largest = max(numbers)

count_smallest = numbers.count(smallest)
count_largest = numbers.count(largest)

print("Smallest number:", smallest)
print("Largest number:", largest)
print("Count of smallest:", count_smallest)
print("Count of largest:",count_largest)

##zadacha6
import random
numbers = []
for i in range(10):
     numbers.append(random.randint(1, 10))
print("Original list:", numbers)
unique_numbers = []
for number in numbers:
     if number not in unique_numbers:
          unique_numbers.append(number)
print("List without repetition:", unique_numbers)

##zadacha7
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

x = int(input("Enter the number x: "))

indexes = []

for i in range(len(numbers)):
    if numbers[i] == x:
        indexes.append(i)

if indexes:
    print("The number", x, "was found at indexes:", indexes)
else:
    print("The number", x, "was not found in the list.")

##zdacha8
list1 = [1, 2, 3, 4, 5, 2]
list2 = [3, 4, 5, 6, 7, 3]

list3 = []

for number in list1:
    if number in list2 and number not in list3:
        list3.append(number)

print("First list:", list1)
print("Second list:", list2)
print("Common elements:", list3)

##zadacha9
numbers = tuple(map(int, input("Enter integers separated by spaces: ").split()))

total = sum(numbers)

average = total / len(numbers)

even_numbers = tuple(number for number in numbers if number % 2 == 0)

print("Original tuple:", numbers)
print("Sum of elements:", total)
print("Arithmetic mean:", average)
print("Tuple with even numbers:", even_numbers)

##zadacha10
sentence = input("Enter a sentence: ")

sentence = sentence.lower()

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:", word_count)

##zadacha11
students = {
    "John": 5.50,
    "Maria": 4.80,
    "Peter": 3.90,
    "Anna": 6.00,
    "George": 4.20
}

print("Students with grades above 4.50:")

for name, grade in students.items():
    if grade > 4.50:
        print(name, "-", grade)
average = sum(students.values()) / len(students)

print("Average grade:", round(average, 2))

##zadacha12
products1 = {
    "Apples": 10,
    "Bananas": 5,
    "Oranges": 8
}

products2 = {
    "Bananas": 7,
    "Oranges": 4,
    "Pears": 6
}

products = products1.copy()

for product, quantity in products2.items():
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

print("Merged dictionary:", products)

##zadacha13
set1 = set(map(int, input("Enter the first set: ").split()))
set2 = set(map(int, input("Enter the second set: ").split()))

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
symmetric_difference = set1 ^ set2

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric difference:", symmetric_difference)

##zadacha14
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = set(numbers)

repeated_numbers = set()

for number in numbers:
    if numbers.count(number) > 1:
        repeated_numbers.add(number)

print("Unique elements:", unique_numbers)
print("Number of different elements:", len(unique_numbers))
print("Repeated numbers:", repeated_numbers)

##zadacha15
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = set(numbers)

repeated_numbers = set()

for number in numbers:
    if numbers.count(number) > 1:
        repeated_numbers.add(number)

print("Unique elements:", unique_numbers)
print("Number of different elements:", len(unique_numbers))
print("Repeated numbers:", repeated_numbers)