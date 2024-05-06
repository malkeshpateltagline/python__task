from functools import reduce

class Number:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get(self):
        return self.numbers
    
    def change_original_values(self, func: lambda i: i): 
        new_numbers = []
        new_numbers = list(map(func, self.numbers))
        return new_numbers
    
    def filter_values(self, filter_func: lambda x: x):

        filtered_numbers = [] 
        filtered_numbers = list(filter(filter_func, self.numbers))
        return filtered_numbers

    def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d):
        compounded_value = reduce(reduce_func, self.numbers)
        return compounded_value
    
    def sort_list(self):
        self.numbers.sort()
        return numbers
        
if __name__ == '__main__': 
    numbers = [2, 5, 1, 66, 22, 11, 10]

    n1 = Number(numbers)

    print('Numbers: ', n1.get())

    lambda_func1 = lambda i : i * 2
    print('New values:', n1.change_original_values(func=lambda_func1))

    lambda_func2 =lambda i:(i%2==0)
    print('Filtered values:', n1.filter_values(filter_func=lambda_func2))

    lambda_func3=lambda i,num:i+num
    print('Compounded value:', n1.compound_the_numbers(reduce_func=lambda_func3))

    print('Sorted list:', n1.sort_list())