from itertools import combinations

numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
numbers.sort()

num=int(input('Enter Number : '))
 
def getpairs(num):
     
    return [pair for pair in combinations(numbers, 2) if sum(pair) == num]

print(set(getpairs(num)))