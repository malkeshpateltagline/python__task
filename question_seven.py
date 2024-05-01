import re

emails = ['abc@gmail.com', '123$tt*@xyz.com', 'good@bad@uk.in', 
          'nasa@usa12.space', 'no-reply@domain.in', 'ramhanuman@saketa.lok', 
          'ruhi.mohan@exter123.123', 'fake@fake123.fakercom']

regex = r'\b[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,5}\b'
res=[]

def check(email):
    for i in email:
        if re.fullmatch(regex, i):
            res.append(i)      

check(emails)

print(f'\n{emails}\n')
print(f'\n{res}\n')