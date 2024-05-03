numbers = [2, 5, 6, 1, 3, 8, 9, 10]

for i in range(len(numbers)):
    for j in range(i, len(numbers)):

        if numbers[i] > numbers[j]:
           numbers[i], numbers[j] = numbers[j], numbers[i]

print (numbers)