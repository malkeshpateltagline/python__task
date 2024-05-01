numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

print('\nA. Length of the list \nB. Display first 3 numbers \nC. Display sum of odd numbers \nD. Number of duplicate numbers \nE. Display list without duplicate numbers\n\nSelect Option (A,B,C,D,E) to Continue.....')

option=input().capitalize()
    
def listLenght():
    print('Length of The List : '+ str(len(numbers)))        
    
def firstThreeNumbers():
    #print('1: {}, 2: {}, 3: {}'.format(numbers[0],numbers[1],numbers[2]))
    print('First 3 Numbers : '+str(numbers[:3]))

def oddNumberSum():
    oddsum = sum(i for i in numbers if i%2)
    print('Sum of Odd Numbers : '+str(oddsum))
    
def countDupNumbers():
    dup = {x for x in numbers if numbers.count(x) > 1}       
    print('Number of Duplicate Numbers : '+str(len(dup)))
        
def listWithoutDupNumers():
    res=[]
    [res.append(x) for x in numbers if x not in res]
    print('List Without Duplicate Numbers : '+str(res))

def identifier(option) :
    if option == 'A':
        listLenght()
    elif option=='B':
        firstThreeNumbers()
    elif option=='C':
        oddNumberSum()
    elif option=='D':
        countDupNumbers()
    elif option=='E':
        listWithoutDupNumers()
    else : print('Please Select Correct Option....')
    
identifier(option)
