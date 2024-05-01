#Create a recursive function which returns the n-th Fibonacci number. [Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]

def memoize(k): 
    fast = {}  
    def partner(l): 
        if l not in fast: 
            fast[l] = k(l) 
        return fast[l] 
    return partner 

def fibonacci(n): 
    if (n<=1): 
        return n  
    return (fibonacci(n-1) + fibonacci(n-2))  
fibonacci = memoize(fibonacci)

nterms = int(input('\nEnter Number : '))

if nterms <= 0:
    print("Plese Enter a Positive Number")
else:
    print("Fibonacci Result: "+str(fibonacci(nterms)))
    #for i in range(nterms):


#Create a recursion function that calculate the sum of numbers present in the list.

def getSum(lst):
    
    if len(lst)==0:
        return 0
    else:
        return lst[0] + getSum(lst[1:])
    
print(f'\n{getSum([23, 44, 5, 67, 1, 1, 2, 4, 5])}\n')
