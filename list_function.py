

def find_largest(numbers):
    if len(numbers)==0:
        return "none"
    largest = numbers[0]
    for i in range(1,len(numbers)):
          if numbers[i] > largest:
             largest = numbers[i]
    return largest

print(find_largest([7, 22, 3, 15, 9, 41, 18]))