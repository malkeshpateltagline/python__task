import re

str = 'PQRQRQRQ' 
substr = 'QRQ'

res= len(re.findall(f'(?=({substr}))', str))
 
print("Substring Count :", res)