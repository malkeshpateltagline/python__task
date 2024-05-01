from collections import Counter
import itertools 

names=['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

length=[]

for i in names:
    length.append(len(i))
    
counter = Counter(length)

most_common_elements = counter.most_common()[-3:]
least_common_elements = counter.most_common()[:3]

print('\nNames : '+str(names))
print('Name lengths : '+str(length))
print('\nThe three most frequent name lenghts are : ')

for list in least_common_elements:
    tuplen = list[0]
    count = list[1]
    res=[]
    for name in names:
        if len(name)==tuplen:
            res.append(name)
    print(f'{count} names of length {tuplen} : {res}')


print('\nThe three least frequent name lenghts are : ')
for list in most_common_elements:
    tuplen = list[0]
    count = list[1]
    res=[]
    for name in names:
        if len(name)==tuplen:
            res.append(name)
    print(f'{count} names of length {tuplen} : {res}')
        