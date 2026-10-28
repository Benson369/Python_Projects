# Exercise List - Add list sum and largest number

numbers = [7, 22, 3, 15, 9, 41, 18, 5, -3, -8 ,-1]
total = 0

for n in numbers:
    total = total + n

print(total)

if len(numbers) == 0:
    print('No numbers')
else:
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    print(largest)
