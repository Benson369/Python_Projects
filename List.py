# Exercise List - Add list sum and largest number

numbers = [7, 22, 3, 15, 9, 41, 18,]
number_five = [5]
negative_numbers = [-3, -8 ,-1]
no_numbers = []

total = 0
negative_total = 0

for n in numbers:
    total = total + n

print(total)

for n in negative_numbers:
    negative_total = negative_total + n

print(negative_total)

if len(numbers) == 0:
    print('No numbers')
else:
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    print(largest)

if len(negative_numbers) == 0:
    print('No numbers')
else:
    largest = negative_numbers[0]
    for n in negative_numbers:
        if n > largest:
            largest = n
    print(largest)

for n in no_numbers:
    print(n)
if len(no_numbers) == 0:
    print('No numbers')
else:
    largest = no_numbers[0]
    for n in no_numbers:
        if n > largest:
            largest = n
    print(largest)

if len(number_five) == 0:
    print('No numbers')
else:
    largest = number_five[0]
    for n in number_five:
        if n > largest:
            largest = n
    print(largest)