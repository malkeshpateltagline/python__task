
#5th
val=1
for i in range(0,6):
    for j in range(i):
        print(val, end=' ')
        val+=1
    print('')
    
print('\n')

#4th
for i in range(0,6):
    for j in range(i):
        if i==3 and j==1 or i==4 and (j==1 or j==2):
            print(' ',end=' ')
        else:
            print('*', end=' ')
    print('')

print('\n')
    
# for i in range(1,6):
#     for j in range(1,6):
#         if j==1 or i==5 or i==j:
#             print('*',end=' ')
#         else:
#             print(' ', end=' ')
#     print('')

print('\n')

#3rd
for i in range(1,6):
    for j in range(1,6):
        if (i==1 or j==1 or j==5 or i==5):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')
    
print('\n') 

#2nd
num = 5
m = (num + 1) // 2 
for i in range(1, num + 1):
    und_sco = abs(i - m)
    stars = num - 2 * und_sco 
    print(' ' * und_sco + '*' * stars + ' ' * und_sco)

print('\n') 

#1nd
num = 5
m = (num + 1) // 2 
for i in range(1, num + 1):
    und_sco = abs(i - m)
    stars = num - 2 * und_sco 
    print('*' * und_sco + ' ' * stars + '*' * und_sco)

print('\n') 