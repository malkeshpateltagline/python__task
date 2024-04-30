names=['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

length=[]

for i in names:
    length.append(len(i))
    
lst = list(set(length))
lst.sort()
most_frequent=lst[:3]
least_frequent=lst[-3:]

most_frequent_names_first=[]
most_frequent_names_second=[]
most_frequent_names_third=[]

least_frequent_names_first=[]
least_frequent_names_second=[]
least_frequent_names_third=[]

for j in names:
    if most_frequent[0]==len(j):
        most_frequent_names_first.append(j)
    elif most_frequent[1]==len(j):
         most_frequent_names_second.append(j)
    elif most_frequent[2]==len(j):
         most_frequent_names_third.append(j)
         
for j in names:
    if least_frequent[0]==len(j):
        least_frequent_names_first.append(j)
    elif least_frequent[1]==len(j):
         least_frequent_names_second.append(j)
    elif least_frequent[2]==len(j):
         least_frequent_names_third.append(j)
            
print('Names : '+str(names))
print('Name lengths : '+str(length))
#print(lst)
#print(most_frequent)
#print(least_frequent)

print('\nThe three most frequent name lenghts are : ')
print('{} names of length {} : {}' .format(len(most_frequent_names_first),len(most_frequent_names_first[0]),most_frequent_names_first))
print('{} names of length {} : {}' .format(len(most_frequent_names_second),len(most_frequent_names_second[0]),most_frequent_names_second))
print('{} names of length {} : {}' .format(len(most_frequent_names_third),len(most_frequent_names_third[0]),most_frequent_names_third))

print('\nThe three least frequent name lenghts are : ')
print('{} names of length {} : {}' .format(len(least_frequent_names_first),len(least_frequent_names_first[0]),least_frequent_names_first))
print('{} names of length {} : {}' .format(len(least_frequent_names_second),len(least_frequent_names_second[0]),least_frequent_names_second))
print('{} names of length {} : {}' .format(len(least_frequent_names_third),len(least_frequent_names_third[0]),least_frequent_names_third))

